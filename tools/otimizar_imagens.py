"""Gera as imagens otimizadas do site a partir da pasta fontes/.
Uso: python3 tools/otimizar_imagens.py"""
from pathlib import Path
from PIL import Image, ImageOps

RAIZ = Path(__file__).resolve().parent.parent
FONTES, DESTINO = RAIZ / "fontes", RAIZ / "assets" / "img"

# nome de saída: (arquivo de origem, recorte (esquerda, topo, direita, base) ou None, largura máxima)
IMAGENS = {
    "fachada": ("fachada.png", (0, 0, 481, 440), 1000),
    "socios-trabalhando": ("socios-trabalhando.jpg", None, 1600),
    "socios-poltrona": ("socios-poltrona.jpg", None, 1000),
    "anderson-retrato": ("anderson-retrato.jpg", (500, 0, 3700, 3264), 1000),
    "roberta-retrato": ("roberta-retrato.jpg", None, 846),
    "roberta-trabalhando": ("roberta-trabalhando.jpg", None, 846),
    "roberta-poltrona": ("roberta-poltrona.jpg", None, 885),
    "anderson-janela": ("anderson-janela.jpg", None, 1600),
    "anderson-cafe": ("anderson-cafe.jpg", None, 1600),
    "sala-convivencia": ("sala-convivencia.jpg", None, 1280),
    "espaco-atendimento": ("espaco-atendimento.jpg", None, 1280),
    "area-convivencia": ("area-convivencia.png", (78, 4, 772, 571), 900),
}

def main() -> None:
    DESTINO.mkdir(parents=True, exist_ok=True)
    for nome, (origem, recorte, largura) in IMAGENS.items():
        im = ImageOps.exif_transpose(Image.open(FONTES / origem)).convert("RGB")
        if recorte:
            im = im.crop(recorte)
        if im.width > largura:
            im = im.resize((largura, round(im.height * largura / im.width)), Image.LANCZOS)
        im.save(DESTINO / f"{nome}.webp", "WEBP", quality=78, method=6)
        im.save(DESTINO / f"{nome}.jpg", "JPEG", quality=80, optimize=True, progressive=True)
        print(f"{nome}: {im.width}x{im.height}")

if __name__ == "__main__":
    main()
