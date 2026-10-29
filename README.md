# Convertir WebP a GIF

Este script convierte archivos WebP a GIF. Busca imágenes `.webp` en la carpeta
de origen y sus subcarpetas, y guarda cada GIF en la carpeta de destino,
conservando la estructura de subcarpetas.

## Requisitos

- Python 3
- Dependencias indicadas en `requirements.txt`

Instala las dependencias con:

```powershell
python -m pip install -r requirements.txt
```

## Uso

Indica las dos rutas al ejecutar el script:

```powershell
python convertir_webp_a_gif.py --origen "RUTA_DE_LA_CARPETA_CON_IMAGENES" --destino "RUTA_DE_LA_CARPETA_DE_RESULTADO"
```

- `--origen`: ruta de la carpeta donde están las imágenes WebP.
- `--destino`: ruta de la carpeta donde se guardarán los GIF. Se crea si no
  existe.

No hay rutas predefinidas en el script: reemplaza ambos textos entre comillas
por las rutas de tus carpetas. Por ejemplo:

```powershell
python convertir_webp_a_gif.py --origen "C:\Mis imágenes\WebP" --destino "C:\Mis imágenes\GIF"
```
