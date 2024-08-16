# DIRECTORIOS

from pathlib import Path

path = Path("directorio")
path.exists()
path.mkdir()
path.rmdir()
path.rename("pepa")

archivos = [p for p in path.interdir() if not p.is_dir()]
archivos = [p for p in path.glob("01-*.py")]
archivos = [p for p in path.glob("**/*.py")]
archivos = [p for p in path.glob("**/*.py")]
print(archivos)