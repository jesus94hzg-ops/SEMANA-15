import json
from pathlib import Path


class ArchivoServicio:
    def __init__(self) -> None:
        base = Path(__file__).resolve().parent.parent / "datos"
        self.ruta_productos = base / "productos.json"
        self.ruta_usuarios = base / "usuarios.json"
        self.ruta_ventas = base / "ventas.json"

    def _cargar_json(self, ruta: Path) -> list[dict]:
        try:
            with ruta.open("r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
            return datos if isinstance(datos, list) else []
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            return []

    def _guardar_json(self, ruta: Path, datos: list[dict]) -> None:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with ruta.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)

    def cargar_productos(self) -> list[dict]:
        return self._cargar_json(self.ruta_productos)

    def guardar_productos(self, productos: list[dict]) -> None:
        self._guardar_json(self.ruta_productos, productos)

    def cargar_usuarios(self) -> list[dict]:
        return self._cargar_json(self.ruta_usuarios)

    def cargar_ventas(self) -> list[dict]:
        return self._cargar_json(self.ruta_ventas)

    def guardar_ventas(self, ventas: list[dict]) -> None:
        self._guardar_json(self.ruta_ventas, ventas)
