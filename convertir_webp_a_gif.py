import argparse
from pathlib import Path

from PIL import Image, ImageSequence


def convertir(origen: Path, destino: Path) -> None:
    destino.parent.mkdir(parents=True, exist_ok=True)
    fotogramas = []
    duraciones = []
    try:
        with Image.open(origen) as imagen:
            repeticiones = imagen.info.get("loop", 0)
            for fotograma in ImageSequence.Iterator(imagen):
                fotogramas.append(fotograma.convert("RGBA"))
                duraciones.append(fotograma.info.get("duration", 100))
            fotogramas[0].save(
                destino,
                format="GIF",
                save_all=True,
                append_images=fotogramas[1:],
                duration=duraciones,
                loop=repeticiones,
                disposal=2,
                optimize=False,
            )
    finally:
        for fotograma in fotogramas:
            fotograma.close()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convierte cada WebP en un GIF, incluyendo las subcarpetas."
    )
    parser.add_argument(
        "--origen",
        type=Path,
        required=True,
        help="Carpeta que contiene las imágenes WebP.",
    )
    parser.add_argument(
        "--destino",
        type=Path,
        required=True,
        help="Carpeta donde se guardarán los GIF.",
    )
    argumentos = parser.parse_args()
    if not argumentos.origen.is_dir():
        parser.error(f"No existe la carpeta: {argumentos.origen}")
    archivos = sorted(
        archivo for archivo in argumentos.origen.rglob("*")
        if archivo.is_file() and archivo.suffix.lower() == ".webp"
    )
    if not archivos:
        print("No se encontraron archivos WebP.")
        return 1
    fallidos = 0
    for archivo in archivos:
        relativo = archivo.relative_to(argumentos.origen).with_suffix(".gif")
        destino = argumentos.destino / relativo
        try:
            convertir(archivo, destino)
            print(f"OK: {relativo}")
        except Exception as error:
            fallidos += 1
            print(f"ERROR: {archivo}: {error}")
    print(f"Convertidos: {len(archivos) - fallidos}. Fallidos: {fallidos}.")
    return 1 if fallidos else 0


if __name__ == "__main__":
    raise SystemExit(main())