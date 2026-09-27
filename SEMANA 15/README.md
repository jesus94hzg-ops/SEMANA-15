# restaurante_app — Semana 15

**Estudiante:** Jesús Horacio Zambrano García  
**Asignatura:** Programación Orientada a Objetos

## Propósito
La Semana 15 continúa la evolución de `restaurante_app` para evidenciar los conceptos fundamentales del manejo de eventos. Se conserva el inicio de sesión, la consulta de usuarios y la gestión de productos, y se incorpora el registro de ventas mediante `command=` y un callback.

## Estructura
- `datos/`: `productos.json`, `usuarios.json` y `ventas.json`.
- `modelos/`: clases `Producto`, `Usuario` y `Venta`.
- `servicios/`: lectura/escritura JSON y reglas del restaurante.
- `ui/`: `LoginView` y `MainView`.
- `assets/`: logo y recursos visuales de la aplicación.
- `main.py`: punto de entrada.

## Evolución realizada
- Se conserva la funcionalidad desarrollada en la Semana 14.
- Se agregó el modelo `Venta`, que relaciona usuario, producto y fecha.
- Se agregó `datos/ventas.json` para persistencia.
- Se incorporó una sección **Ventas** en la navegación.
- Usuario y producto se seleccionan con `ttk.Combobox`.
- El botón **Registrar venta** usa `command=self.registrar_venta_callback`.
- El callback obtiene las selecciones y delega la operación a `RestauranteServicio`.
- `RestauranteServicio` valida usuario, producto y stock; registra la venta y actualiza los archivos JSON.
- Las ventas se muestran en un `Treeview` y se actualizan inmediatamente.
- Se incorporó la carpeta obligatoria `assets/` con logo e íconos/recursos visuales.

## Flujo de manejo de eventos
`Usuario → botón Registrar venta → command= → callback → RestauranteServicio → persistencia JSON → actualización de la interfaz`.

La interfaz no lee ni escribe directamente los archivos JSON; esta responsabilidad permanece en la capa de servicios.

## Credencial de prueba
- Identificación: `1301854078`
- Contraseña: `1234`

## Ejecución
Desde la carpeta `restaurante_app`:

```bash
python main.py
```

En Windows también puede usarse:

```bash
py main.py
```

## Comprobación funcional
1. Iniciar sesión.
2. Verificar Productos y Usuarios.
3. Abrir Ventas.
4. Seleccionar un usuario y un producto.
5. Pulsar **Registrar venta**.
6. Confirmar que aparece en la tabla y en `datos/ventas.json`.
7. Cerrar y volver a ejecutar para comprobar la persistencia.
