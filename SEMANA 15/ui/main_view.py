import tkinter as tk
from tkinter import ttk, messagebox

NAVY='#1f2f4d'; NAVY2='#34445d'; BLUE='#2f6fed'; RED='#ef1748'; BG='#f4f7fb'; WHITE='#ffffff'; TEXT='#172033'; MUTED='#64748b'; LINE='#dbe3ee'

class MainView(tk.Frame):
    def __init__(self, master, restaurante_servicio, usuario, on_logout):
        super().__init__(master,bg=BG); self.servicio=restaurante_servicio; self.usuario=usuario; self.on_logout=on_logout; self.entries={}; self.nav={}
        self.columnconfigure(1,weight=1); self.rowconfigure(0,weight=1)
        self.sidebar=tk.Frame(self,bg=NAVY,width=245); self.sidebar.grid(row=0,column=0,sticky='ns'); self.sidebar.grid_propagate(False)
        tk.Label(self.sidebar,text='RESTAURANTE',font=('Segoe UI',22,'bold'),fg=WHITE,bg=NAVY).pack(anchor='w',padx=26,pady=(30,2))
        tk.Label(self.sidebar,text=self.usuario.nombre,font=('Segoe UI',11),fg='#d8e2f0',bg=NAVY).pack(anchor='w',padx=26,pady=(0,30))
        for key,icon,text,cmd in [('inicio','⌂','Inicio',self.mostrar_inicio),('usuarios','♙','Usuarios',self.mostrar_usuarios),('productos','▣','Productos',self.mostrar_productos),('ventas','▤','Ventas',self.mostrar_ventas)]:
            b=tk.Button(self.sidebar,text=f'  {icon}  {text}',anchor='w',font=('Segoe UI',12,'bold'),fg=WHITE,bg=NAVY2,activebackground=BLUE,activeforeground=WHITE,relief='flat',bd=0,cursor='hand2',command=cmd); b.pack(fill='x',padx=22,pady=4,ipady=14); self.nav[key]=b
        tk.Frame(self.sidebar,bg=NAVY).pack(expand=True)
        tk.Button(self.sidebar,text='↪  Cerrar sesión',font=('Segoe UI',12,'bold'),fg=WHITE,bg=RED,activebackground='#cf123d',activeforeground=WHITE,relief='flat',bd=0,cursor='hand2',command=on_logout).pack(fill='x',padx=22,pady=22,ipady=13)
        right=tk.Frame(self,bg=BG); right.grid(row=0,column=1,sticky='nsew'); right.rowconfigure(0,weight=1); right.columnconfigure(0,weight=1)
        self.contenido=tk.Frame(right,bg=BG); self.contenido.grid(row=0,column=0,sticky='nsew',padx=38,pady=(28,12)); self.contenido.rowconfigure(1,weight=1); self.contenido.columnconfigure(0,weight=1)
        self.status=tk.Label(right,text='',anchor='w',font=('Segoe UI',10),fg='#475569',bg='#dbeafe',padx=24,pady=10); self.status.grid(row=1,column=0,sticky='ew')
        self.mostrar_inicio()
    def _clear(self,key):
        for w in self.contenido.winfo_children(): w.destroy()
        for k,b in self.nav.items(): b.configure(bg=BLUE if k==key else NAVY2)
        self._status()
    def _status(self): self.status.config(text=f'Productos: {len(self.servicio.listar_productos())} | Usuarios: {len(self.servicio.listar_usuarios())} | Ventas: {len(self.servicio.listar_ventas())} | Datos JSON locales')
    def _title(self,text,sub=''):
        tk.Label(self.contenido,text=text,font=('Segoe UI',25,'bold'),fg=TEXT,bg=BG).grid(row=0,column=0,sticky='nw')
        if sub: tk.Label(self.contenido,text=sub,font=('Segoe UI',12),fg='#475569',bg=BG).grid(row=0,column=0,sticky='nw',pady=(48,0))
    def mostrar_inicio(self):
        self._clear('inicio'); self._title('Panel principal','Consulte usuarios, gestione productos y registre ventas desde el menú lateral.')
        cards=tk.Frame(self.contenido,bg=BG); cards.grid(row=1,column=0,sticky='new',pady=(30,0))
        for i,(t,n) in enumerate([('Usuarios registrados',len(self.servicio.listar_usuarios())),('Productos registrados',len(self.servicio.listar_productos())),('Ventas registradas',len(self.servicio.listar_ventas()))]):
            c=tk.Frame(cards,bg=WHITE,padx=28,pady=25,width=240,height=145); c.grid(row=0,column=i,padx=(0,22),sticky='nsew'); c.grid_propagate(False); tk.Label(c,text=t,font=('Segoe UI',11,'bold'),fg='#334155',bg=WHITE).pack(anchor='w'); tk.Label(c,text=str(n),font=('Segoe UI',28,'bold'),fg=BLUE,bg=WHITE).pack(anchor='w',pady=(12,0))
    def _tree_style(self):
        s=ttk.Style(); s.configure('App.Treeview',font=('Segoe UI',10),rowheight=30,background=WHITE,fieldbackground=WHITE); s.configure('App.Treeview.Heading',font=('Segoe UI',10,'bold'),background='#dbeafe',foreground=TEXT); s.map('App.Treeview',background=[('selected',BLUE)])
    def mostrar_usuarios(self):
        self._clear('usuarios'); self._title('Usuarios registrados'); box=tk.LabelFrame(self.contenido,text=' Consulta de usuarios ',font=('Segoe UI',11,'bold'),bg=BG,fg=TEXT,padx=12,pady=12); box.grid(row=1,column=0,sticky='nsew',pady=(28,0)); box.rowconfigure(0,weight=1); box.columnconfigure(0,weight=1); self._tree_style()
        t=ttk.Treeview(box,columns=('id','nombre','correo'),show='headings',style='App.Treeview');
        for c,h,w in [('id','Identificación',170),('nombre','Nombre',260),('correo','Correo',320)]: t.heading(c,text=h); t.column(c,width=w)
        for u in self.servicio.listar_usuarios(): t.insert('',tk.END,values=(u.identificacion,u.nombre,u.correo))
        t.grid(row=0,column=0,sticky='nsew'); sc=ttk.Scrollbar(box,command=t.yview); sc.grid(row=0,column=1,sticky='ns'); t.configure(yscrollcommand=sc.set)
    def mostrar_productos(self):
        self._clear('productos'); self._title('Gestión de productos'); body=tk.Frame(self.contenido,bg=BG); body.grid(row=1,column=0,sticky='nsew',pady=(28,0)); body.columnconfigure(1,weight=1); body.rowconfigure(0,weight=1)
        form=tk.LabelFrame(body,text=' Datos del producto ',font=('Segoe UI',11,'bold'),bg=BG,fg=TEXT,padx=18,pady=14); form.grid(row=0,column=0,sticky='ns',padx=(0,24)); self.entries={}
        for i,(lab,key) in enumerate([('Código','codigo'),('Nombre','nombre'),('Categoría','categoria'),('Precio','precio'),('Stock','stock')]):
            tk.Label(form,text=lab,font=('Segoe UI',10,'bold'),bg=BG,fg='#334155').grid(row=i,column=0,sticky='w',pady=7,padx=(0,10)); e=tk.Entry(form,width=28,font=('Segoe UI',10),relief='solid',bd=1); e.grid(row=i,column=1,ipady=6,pady=7); self.entries[key]=e
        for r,(txt,cmd,color) in enumerate([('＋  Registrar',self.registrar,BLUE),('⌕  Cargar por código',self.cargar,NAVY),('✎  Actualizar',self.actualizar,BLUE),('▢  Eliminar',self.eliminar,RED),('⌫  Limpiar',self.limpiar_campos,NAVY)],start=5): tk.Button(form,text=txt,command=cmd,bg=color,fg=WHITE,font=('Segoe UI',11,'bold'),relief='flat',cursor='hand2').grid(row=r,column=0,columnspan=2,sticky='ew',pady=5,ipady=9)
        box=tk.LabelFrame(body,text=' Productos registrados ',font=('Segoe UI',11,'bold'),bg=BG,fg=TEXT,padx=10,pady=10); box.grid(row=0,column=1,sticky='nsew'); box.rowconfigure(0,weight=1); box.columnconfigure(0,weight=1); self._tree_style(); cols=('codigo','nombre','categoria','precio','stock'); self.tabla=ttk.Treeview(box,columns=cols,show='headings',style='App.Treeview')
        for c,h,w in [('codigo','Código',80),('nombre','Nombre',170),('categoria','Categoría',120),('precio','Precio',80),('stock','Stock',65)]: self.tabla.heading(c,text=h); self.tabla.column(c,width=w)
        self.tabla.grid(row=0,column=0,sticky='nsew'); sc=ttk.Scrollbar(box,command=self.tabla.yview); sc.grid(row=0,column=1,sticky='ns'); self.tabla.configure(yscrollcommand=sc.set); self.refrescar()
    def valores(self): return tuple(self.entries[k].get().strip() for k in ('codigo','nombre','categoria','precio','stock'))
    def limpiar_campos(self):
        for e in self.entries.values(): e.delete(0,tk.END)
    def refrescar(self):
        for x in self.tabla.get_children(): self.tabla.delete(x)
        for p in self.servicio.listar_productos(): self.tabla.insert('',tk.END,values=(p.codigo,p.nombre,p.categoria,f'${p.precio:.2f}',p.stock))
        self._status()
    def registrar(self):
        try: self.servicio.registrar_producto(*self.valores()); self.refrescar(); self.limpiar_campos(); messagebox.showinfo('Productos','Producto registrado correctamente.')
        except (ValueError,TypeError) as e: messagebox.showerror('Datos inválidos',str(e))
    def cargar(self):
        p=self.servicio.buscar_producto(self.entries['codigo'].get())
        if not p: messagebox.showwarning('Productos','No se encontró el producto.'); return
        for k,v in zip(('codigo','nombre','categoria','precio','stock'),(p.codigo,p.nombre,p.categoria,p.precio,p.stock)): self.entries[k].delete(0,tk.END); self.entries[k].insert(0,str(v))
    def actualizar(self):
        try: self.servicio.actualizar_producto(*self.valores()); self.refrescar(); messagebox.showinfo('Productos','Producto actualizado correctamente.')
        except (ValueError,TypeError) as e: messagebox.showerror('Datos inválidos',str(e))
    def eliminar(self):
        codigo=self.entries['codigo'].get().strip()
        if not codigo: messagebox.showwarning('Productos','Ingrese el código del producto.'); return
        if messagebox.askyesno('Confirmar','¿Desea eliminar este producto?'):
            try: self.servicio.eliminar_producto(codigo); self.refrescar(); self.limpiar_campos(); messagebox.showinfo('Productos','Producto eliminado correctamente.')
            except ValueError as e: messagebox.showerror('Productos',str(e))
    def mostrar_ventas(self):
        self._clear('ventas'); self._title('Ventas'); body=tk.Frame(self.contenido,bg=BG); body.grid(row=1,column=0,sticky='nsew',pady=(28,0)); body.columnconfigure(1,weight=1); body.rowconfigure(0,weight=1)
        form=tk.LabelFrame(body,text=' Registrar venta ',font=('Segoe UI',11,'bold'),bg=BG,fg=TEXT,padx=18,pady=18); form.grid(row=0,column=0,sticky='new',padx=(0,24));
        usuarios=self.servicio.listar_usuarios(); self._map_usuarios={f'{u.identificacion} - {u.nombre}':u.identificacion for u in usuarios}; productos=self.servicio.listar_productos(); self._map_productos={f'{p.codigo} - {p.nombre}':p.codigo for p in productos}
        tk.Label(form,text='Usuario',font=('Segoe UI',10,'bold'),bg=BG,fg='#334155').grid(row=0,column=0,sticky='w',pady=8); self.venta_usuario=ttk.Combobox(form,state='readonly',width=32,values=list(self._map_usuarios)); self.venta_usuario.grid(row=0,column=1,pady=8,ipady=5)
        tk.Label(form,text='Producto',font=('Segoe UI',10,'bold'),bg=BG,fg='#334155').grid(row=1,column=0,sticky='w',pady=8); self.venta_producto=ttk.Combobox(form,state='readonly',width=32,values=list(self._map_productos)); self.venta_producto.grid(row=1,column=1,pady=8,ipady=5)
        tk.Button(form,text='＋  Registrar venta',command=self.registrar_venta_callback,bg=BLUE,fg=WHITE,font=('Segoe UI',11,'bold'),relief='flat',cursor='hand2').grid(row=2,column=0,columnspan=2,sticky='ew',pady=(18,0),ipady=11)
        box=tk.LabelFrame(body,text=' Ventas registradas ',font=('Segoe UI',11,'bold'),bg=BG,fg=TEXT,padx=10,pady=10); box.grid(row=0,column=1,sticky='nsew'); box.rowconfigure(0,weight=1); box.columnconfigure(0,weight=1); self._tree_style(); self.tabla_ventas=ttk.Treeview(box,columns=('fecha','usuario','producto'),show='headings',style='App.Treeview')
        for c,h,w in [('fecha','Fecha',155),('usuario','Usuario',220),('producto','Producto',220)]: self.tabla_ventas.heading(c,text=h); self.tabla_ventas.column(c,width=w)
        self.tabla_ventas.grid(row=0,column=0,sticky='nsew'); sc=ttk.Scrollbar(box,command=self.tabla_ventas.yview); sc.grid(row=0,column=1,sticky='ns'); self.tabla_ventas.configure(yscrollcommand=sc.set); self.refrescar_ventas()
    def registrar_venta_callback(self):
        ut=self.venta_usuario.get(); pt=self.venta_producto.get()
        if not ut or not pt: messagebox.showwarning('Venta','Seleccione un usuario y un producto.'); return
        try: v=self.servicio.registrar_venta(self._map_usuarios[ut],self._map_productos[pt]); self.mostrar_ventas(); messagebox.showinfo('Venta',f'Venta registrada correctamente.\nFecha: {v.fecha}')
        except ValueError as e: messagebox.showerror('Venta',str(e))
    def refrescar_ventas(self):
        for x in self.tabla_ventas.get_children(): self.tabla_ventas.delete(x)
        for v in self.servicio.listar_ventas():
            u=self.servicio.buscar_usuario(v.usuario_id); p=self.servicio.buscar_producto(v.producto_codigo); self.tabla_ventas.insert('',tk.END,values=(v.fecha,f'{v.usuario_id} - {u.nombre}' if u else v.usuario_id,f'{v.producto_codigo} - {p.nombre}' if p else v.producto_codigo))
        self._status()
