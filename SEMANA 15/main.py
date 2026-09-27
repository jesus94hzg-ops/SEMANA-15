import tkinter as tk
from servicios import ArchivoServicio, RestauranteServicio
from ui import LoginView, MainView


class RestauranteApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Restaurante App - Semana 15")
        self.root.geometry("1100x680")
        self.root.minsize(950, 600)
        self.restaurante_servicio = RestauranteServicio(ArchivoServicio())
        self.vista_actual = None
        self.mostrar_login()

    def cambiar_vista(self, nueva_vista) -> None:
        if self.vista_actual is not None:
            self.vista_actual.destroy()
        self.vista_actual = nueva_vista
        self.vista_actual.pack(fill="both", expand=True)

    def mostrar_login(self) -> None:
        self.cambiar_vista(LoginView(self.root, self.restaurante_servicio, self.mostrar_principal))

    def mostrar_principal(self, usuario) -> None:
        self.cambiar_vista(MainView(self.root, self.restaurante_servicio, usuario, self.mostrar_login))

    def ejecutar(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    RestauranteApp().ejecutar()
