class Usuario:
    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str,
        contrasena: str
    ) -> None:
        identificacion = identificacion.strip()
        nombre = nombre.strip()
        correo = correo.strip()
        contrasena = contrasena.strip()

        if not identificacion:
            raise ValueError("La identificación no puede estar vacía.")
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if not correo:
            raise ValueError("El correo no puede estar vacío.")
        if not contrasena:
            raise ValueError("La contraseña no puede estar vacía.")

        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena

    def __str__(self) -> str:
        return f"{self.identificacion} | {self.nombre} | {self.correo}"
