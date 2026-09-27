from datetime import datetime
from modelos import Producto, Usuario, Venta


class RestauranteServicio:
    def __init__(self, archivo_servicio) -> None:
        self.archivo_servicio = archivo_servicio
        self._productos = self._crear_productos(archivo_servicio.cargar_productos())
        self._usuarios = self._crear_usuarios(archivo_servicio.cargar_usuarios())
        self._ventas = self._crear_ventas(archivo_servicio.cargar_ventas())

    def _crear_productos(self, datos):
        productos = []
        for r in datos:
            try:
                productos.append(Producto(r["codigo"], r["nombre"], r["categoria"], float(r["precio"]), int(r.get("stock", 0))))
            except (KeyError, TypeError, ValueError):
                continue
        return productos

    def _crear_usuarios(self, datos):
        usuarios = []
        for r in datos:
            try:
                usuarios.append(Usuario(r["identificacion"], r["nombre"], r["correo"], r["contrasena"]))
            except (KeyError, TypeError, ValueError):
                continue
        return usuarios

    def _crear_ventas(self, datos):
        ventas = []
        for r in datos:
            try:
                ventas.append(Venta(r["usuario_id"], r["producto_codigo"], r["fecha"]))
            except (KeyError, TypeError, ValueError):
                continue
        return ventas

    def validar_acceso(self, identificacion, contrasena):
        identificacion, contrasena = identificacion.strip(), contrasena.strip()
        return next((u for u in self._usuarios if u.identificacion == identificacion and u.contrasena == contrasena), None)

    def listar_productos(self): return self._productos.copy()
    def listar_usuarios(self): return self._usuarios.copy()
    def listar_ventas(self): return self._ventas.copy()
    def cantidad_productos(self): return len(self._productos)
    def cantidad_usuarios(self): return len(self._usuarios)

    def buscar_producto(self, codigo):
        codigo = codigo.strip().upper()
        return next((p for p in self._productos if p.codigo.upper() == codigo), None)

    def buscar_usuario(self, identificacion):
        identificacion = identificacion.strip()
        return next((u for u in self._usuarios if u.identificacion == identificacion), None)

    def registrar_producto(self, codigo, nombre, categoria, precio, stock):
        codigo = codigo.strip().upper()
        if self.buscar_producto(codigo):
            raise ValueError("Ya existe un producto con ese código.")
        producto = Producto(codigo, nombre, categoria, float(precio), int(stock))
        self._productos.append(producto)
        self._guardar_productos()

    def actualizar_producto(self, codigo, nombre, categoria, precio, stock):
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError("No existe un producto con ese código.")
        nuevo = Producto(producto.codigo, nombre, categoria, float(precio), int(stock))
        self._productos[self._productos.index(producto)] = nuevo
        self._guardar_productos()

    def eliminar_producto(self, codigo):
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError("No existe un producto con ese código.")
        self._productos.remove(producto)
        self._guardar_productos()

    def registrar_venta(self, usuario_id, producto_codigo):
        usuario = self.buscar_usuario(usuario_id)
        if usuario is None:
            raise ValueError("El usuario seleccionado no existe.")
        producto = self.buscar_producto(producto_codigo)
        if producto is None:
            raise ValueError("El producto seleccionado no existe.")
        if producto.stock <= 0:
            raise ValueError("El producto seleccionado no tiene stock disponible.")

        venta = Venta(usuario.identificacion, producto.codigo, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        producto.stock -= 1
        self._ventas.append(venta)
        self._guardar_productos()
        self._guardar_ventas()
        return venta

    def _guardar_productos(self):
        datos = [{"codigo": p.codigo, "nombre": p.nombre, "categoria": p.categoria, "precio": p.precio, "stock": p.stock} for p in self._productos]
        self.archivo_servicio.guardar_productos(datos)

    def _guardar_ventas(self):
        datos = [{"usuario_id": v.usuario_id, "producto_codigo": v.producto_codigo, "fecha": v.fecha} for v in self._ventas]
        self.archivo_servicio.guardar_ventas(datos)
