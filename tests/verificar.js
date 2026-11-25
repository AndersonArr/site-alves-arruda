// Verificação automática do site. Uso: node tests/verificar.js [pasta-de-capturas]
// Sobe um servidor local na raiz do projeto e confere cada página em celular e computador.
const { chromium } = require("playwright");
const http = require("http");
const fs = require("fs");
const path = require("path");

const RAIZ = path.resolve(__dirname, "..");
const CAPTURAS = process.argv[2];
const PAGINAS = ["/", "/familia/", "/direito-medico/", "/saude-autismo-inclusao/", "/civil-consumidor/", "/empresarial/", "/privacidade/", "/404.html"];
const LARGURAS = [360, 1366];
const NUMEROS = ["5562985109393", "5562982624401"];
const PROIBIDAS = [/\bAv\.\s/, /\bEd\.\s/, /\bnº/, /\bart\.\s/i, /\bCPC\b/, /\bCF\b/, /\bDra?\.\s/, /\bSeg\b/, /\bSTJ\b/, /\bSTF\b/];
const TIPOS = { ".html": "text/html; charset=utf-8", ".css": "text/css", ".js": "text/javascript", ".png": "image/png", ".jpg": "image/jpeg", ".webp": "image/webp", ".xml": "application/xml", ".txt": "text/plain" };

function servidor() {
  return http.createServer((req, res) => {
    let p = decodeURIComponent(req.url.split("?")[0]);
    if (p.endsWith("/")) p += "index.html";
    const arquivo = path.join(RAIZ, p);
    if (!arquivo.startsWith(RAIZ) || !fs.existsSync(arquivo) || fs.statSync(arquivo).isDirectory()) {
      res.writeHead(404, { "Content-Type": "text/html; charset=utf-8" });
      return res.end(fs.readFileSync(path.join(RAIZ, "404.html")));
    }
    res.writeHead(200, { "Content-Type": TIPOS[path.extname(arquivo)] || "application/octet-stream" });
    res.end(fs.readFileSync(arquivo));
  });
}

(async () => {
  const srv = servidor().listen(0);
  const base = `http://localhost:${srv.address().port}`;
  const navegador = await chromium.launch();
  const falhas = [];
  const falhar = (msg) => { falhas.push(msg); console.log("FALHA:", msg); };

  // Imagens pesadas
  for (const f of fs.readdirSync(path.join(RAIZ, "assets/img"))) {
    const kb = fs.statSync(path.join(RAIZ, "assets/img", f)).size / 1024;
    if (kb > 400) falhar(`imagem pesada: ${f} (${kb.toFixed(0)} KB)`);
  }

  for (const largura of LARGURAS) {
    const pagina = await navegador.newPage({ viewport: { width: largura, height: largura < 800 ? 780 : 860 } });
    for (const caminho of PAGINAS) {
      const resp = await pagina.goto(base + caminho, { waitUntil: "load" });
      if (resp.status() !== 200) falhar(`${caminho}: status ${resp.status()}`);
      // Rola até o fim para carregar imagens e revelar elementos
      await pagina.evaluate(async () => {
        for (let y = 0; y < document.body.scrollHeight; y += 500) { window.scrollTo(0, y); await new Promise((r) => setTimeout(r, 60)); }
        window.scrollTo(0, 0);
      });
      await pagina.evaluate(() => document.querySelectorAll("img[loading=lazy]").forEach((i) => i.removeAttribute("loading")));
      await pagina.waitForFunction(() => [...document.images].every((i) => i.complete), null, { timeout: 15000 }).catch(() => {});
      const info = await pagina.evaluate(() => ({
        larguraRolagem: document.documentElement.scrollWidth,
        larguraJanela: window.innerWidth,
        imagensQuebradas: [...document.images].filter((i) => !i.complete || i.naturalWidth === 0).map((i) => i.getAttribute("src")),
        semAlt: [...document.images].filter((i) => !i.hasAttribute("alt")).map((i) => i.getAttribute("src")),
        links: [...document.querySelectorAll("a[href]")].map((a) => a.href),
        texto: document.body.innerText,
        h1: document.querySelectorAll("h1").length,
      }));
      const id = `${caminho} @${largura}`;
      if (info.larguraRolagem > info.larguraJanela) falhar(`${id}: rolagem horizontal (${info.larguraRolagem} > ${info.larguraJanela})`);
      if (info.imagensQuebradas.length) falhar(`${id}: imagens quebradas ${info.imagensQuebradas.join(", ")}`);
      if (info.semAlt.length) falhar(`${id}: imagens sem texto alternativo`);
      if (info.h1 !== 1) falhar(`${id}: ${info.h1} títulos principais (h1)`);
      for (const re of PROIBIDAS) { const m = info.texto.match(re); if (m) falhar(`${id}: abreviação proibida "${m[0]}"`); }
      for (const href of info.links) {
        if (href.startsWith("https://wa.me/") && !NUMEROS.some((n) => href.startsWith(`https://wa.me/${n}`))) falhar(`${id}: WhatsApp com número errado ${href}`);
        if (href.startsWith(base)) {
          const alvo = href.split("#")[0];
          const r = await pagina.request.get(alvo);
          if (r.status() !== 200) falhar(`${id}: link quebrado ${href}`);
          const ancora = href.split("#")[1];
          if (ancora && alvo.replace(base, "") === caminho && !(await pagina.$(`#${ancora}`))) falhar(`${id}: âncora inexistente #${ancora}`);
        }
      }
      if (largura < 800 && caminho === "/") {
        await pagina.click(".alternar-menu");
        await pagina.waitForTimeout(400);
        if (!(await pagina.isVisible(".menu a[href='#atuacao']"))) falhar("menu do celular não abriu");
        await pagina.click(".menu a[href='#atuacao']");
        await pagina.waitForTimeout(400);
        if (await pagina.evaluate(() => document.body.classList.contains("menu-aberto"))) falhar("menu do celular não fechou após clique");
      }
      if (CAPTURAS) {
        fs.mkdirSync(CAPTURAS, { recursive: true });
        const nome = (caminho.replace(/\//g, "_").replace(/^_|_$/g, "") || "inicio").replace(".html", "");
        await pagina.evaluate(() => document.querySelectorAll(".revelar").forEach((e) => e.classList.add("visivel")));
        await pagina.evaluate(() => Promise.all([...document.images].map((i) => { i.removeAttribute("decoding"); return i.decode().catch(() => {}); })));
        await pagina.waitForTimeout(900);
        await pagina.screenshot({ path: path.join(CAPTURAS, `${nome}-${largura}.png`), fullPage: true });
      }
    }
    await pagina.close();
  }
  await navegador.close();
  srv.close();
  console.log(`${falhas.length} falhas`);
  process.exit(falhas.length ? 1 : 0);
})();
