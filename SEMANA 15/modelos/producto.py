class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int = 0) -> None:
        codigo = codigo.strip()
        nombre = nombre.strip()
        categoria = categoria.strip()

        if not codigo:
            raise ValueError("El código no puede estar vacío.")
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if not categoria:
            raise ValueError("La categoría no puede estar vacía.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)
        self.stock = int(stock)

    def __str__(self) -> str:
        return (
            f"{self.codigo} | {self.nombre} | {self.categoria} | "
            f"${self.precio:.2f} | Stock: {self.stock}"
        )
