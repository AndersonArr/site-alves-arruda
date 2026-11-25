"""Extrai a logomarca dourada com fundo transparente, sem alterar o desenho.
Calcula a transparência de cada pixel pela distância entre o fundo marrom e o dourado."""
from pathlib import Path
import numpy as np
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
LOGO = RAIZ / "assets" / "logo"
FUNDO = np.array([0x32, 0x26, 0x20], float)
DOURADO = np.array([0xFF, 0xB9, 0x80], float)

def extrair(origem: str, destino: str, escala: int = 2) -> None:
    im = Image.open(LOGO / origem).convert("RGB")
    im = im.resize((im.width * escala, im.height * escala), Image.LANCZOS)
    px = np.asarray(im, float)
    d = DOURADO - FUNDO
    alfa = np.clip(((px - FUNDO) @ d) / (d @ d), 0, 1)
    saida = np.zeros((*alfa.shape, 4), np.uint8)
    saida[..., :3] = DOURADO.astype(np.uint8)
    saida[..., 3] = (alfa * 255).round().astype(np.uint8)
    img = Image.fromarray(saida, "RGBA")
    img = img.crop(img.getbbox())
    img.save(LOGO / destino, optimize=True)
    print(destino, img.size)

if __name__ == "__main__":
    extrair("logo-completa-quadrada.png", "logo-dourada.png")
    extrair("simbolo.png", "simbolo-dourado.png")
