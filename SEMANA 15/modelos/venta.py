class Venta:
    def __init__(self, usuario_id: str, producto_codigo: str, fecha: str) -> None:
        usuario_id = usuario_id.strip()
        producto_codigo = producto_codigo.strip().upper()
        fecha = fecha.strip()
        if not usuario_id:
            raise ValueError("La identificación del usuario es obligatoria.")
        if not producto_codigo:
            raise ValueError("El código del producto es obligatorio.")
        if not fecha:
            raise ValueError("La fecha de la venta es obligatoria.")
        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.fecha = fecha

    def __str__(self) -> str:
        return f"{self.fecha} | {self.usuario_id} | {self.producto_codigo}"
