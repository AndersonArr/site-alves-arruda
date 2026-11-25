// Alves & Arruda Advogados — comportamento do site
(function () {
  document.documentElement.classList.remove("sem-js");

  // Menu no celular
  var botao = document.querySelector(".alternar-menu");
  if (botao) {
    botao.addEventListener("click", function () {
      var aberto = document.body.classList.toggle("menu-aberto");
      botao.setAttribute("aria-expanded", aberto ? "true" : "false");
    });
    document.querySelectorAll(".menu a").forEach(function (link) {
      link.addEventListener("click", function () {
        document.body.classList.remove("menu-aberto");
        botao.setAttribute("aria-expanded", "false");
      });
    });
    document.addEventListener("keydown", function (evento) {
      if (evento.key === "Escape" && document.body.classList.contains("menu-aberto")) {
        document.body.classList.remove("menu-aberto");
        botao.setAttribute("aria-expanded", "false");
        botao.focus();
      }
    });
  }

  // Cabeçalho muda ao rolar
  var cabecalho = document.querySelector(".cabecalho");
  function aoRolar() {
    if (cabecalho) cabecalho.classList.toggle("rolado", window.scrollY > 40);
  }
  window.addEventListener("scroll", aoRolar, { passive: true });
  aoRolar();

  // Elementos surgem suavemente ao rolar
  var elementos = document.querySelectorAll(".revelar");
  if ("IntersectionObserver" in window) {
    var observador = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (entrada) {
        if (entrada.isIntersecting) {
          entrada.target.classList.add("visivel");
          observador.unobserve(entrada.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    elementos.forEach(function (el) { observador.observe(el); });
  } else {
    elementos.forEach(function (el) { el.classList.add("visivel"); });
  }

  // Ano atual no rodapé
  document.querySelectorAll("[data-ano]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
