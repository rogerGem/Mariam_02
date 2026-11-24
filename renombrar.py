from pathlib import Path

# Cambia esta ruta por la de tu carpeta de imágenes
CARPETA = Path(r"C:\Users\daniel\Downloads\pagiina web de nelvy\img\ninos")

EXTENSIONES_IMAGEN = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".webp",
    ".bmp",
    ".tiff",
}


def renombrar_imagenes(carpeta: Path) -> None:
  if not carpeta.is_dir():
    print(f"La carpeta no existe: {carpeta}")
    return

  # Filtrar y ordenar las imágenes existentes
  imagenes = sorted(
      [
          archivo
          for archivo in carpeta.iterdir()
          if archivo.is_file()
          and archivo.suffix.lower() in EXTENSIONES_IMAGEN
      ],
      key=lambda p: p.name.lower(),
  )

  if not imagenes:
    print("No se encontraron imágenes en la carpeta.")
    return

  # Paso 1: Renombrar a nombres temporales para evitar conflictos
  # (por ejemplo, si ya existe "1.jpg" y otro archivo quiere llamarse "1.jpg")
  temporales = []
  for i, archivo in enumerate(imagenes, start=1):
    temp_path = carpeta / f"__temp_{i}__{archivo.suffix.lower()}"
    archivo.rename(temp_path)
    temporales.append(temp_path)

  # Paso 2: Renombrar a 1, 2, 3...
  for i, temp_path in enumerate(temporales, start=1):
    nuevo_path = carpeta / f"{i}{temp_path.suffix}"
    temp_path.rename(nuevo_path)
    print(f"Renombrado -> {nuevo_path.name}")

  print(f"\nListo: {len(temporales)} imágenes renombradas.")


if __name__ == "__main__":
  renombrar_imagenes(CARPETA)