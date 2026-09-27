import tkinter as tk
from pathlib import Path
from tkinter import messagebox

BG = '#eef3f8'; NAVY = '#1f2f4d'; BLUE = '#2f6fed'; RED = '#ef1748'; TEXT = '#172033'; MUTED = '#64748b'; WHITE = '#ffffff'

class LoginView(tk.Frame):
    def __init__(self, master, restaurante_servicio, on_login_success):
        super().__init__(master, bg=BG)
        self.servicio = restaurante_servicio; self.on_login_success = on_login_success
        self.assets = Path(__file__).resolve().parent.parent / 'assets'; self.logo = None
        self.columnconfigure(0, weight=1); self.rowconfigure(0, weight=1)
        card = tk.Frame(self, bg=WHITE, padx=48, pady=36); card.grid(row=0, column=0)
        try:
            self.logo = tk.PhotoImage(file=str(self.assets/'logo.png')).zoom(2,2)
            tk.Label(card, image=self.logo, bg=WHITE).pack(pady=(0,8))
        except tk.TclError: pass
        tk.Label(card, text='RESTAURANTE', font=('Segoe UI', 25, 'bold'), fg=TEXT, bg=WHITE).pack()
        tk.Label(card, text='Inicio de sesión', font=('Segoe UI', 12), fg=MUTED, bg=WHITE).pack(pady=(8,28))
        tk.Label(card, text='Usuario', font=('Segoe UI', 11, 'bold'), fg=TEXT, bg=WHITE).pack(anchor='w')
        self.usuario_entry=tk.Entry(card, font=('Segoe UI',12), relief='flat', bg='#f8fafc', highlightthickness=1, highlightbackground='#cbd5e1'); self.usuario_entry.pack(fill='x', ipady=9, pady=(5,16))
        tk.Label(card, text='Contraseña', font=('Segoe UI', 11, 'bold'), fg=TEXT, bg=WHITE).pack(anchor='w')
        self.contrasena_entry=tk.Entry(card, font=('Segoe UI',12), show='*', relief='flat', bg='#f8fafc', highlightthickness=1, highlightbackground='#cbd5e1'); self.contrasena_entry.pack(fill='x', ipady=9, pady=(5,25))
        tk.Button(card, text='Iniciar sesión', command=self.iniciar_sesion, bg=BLUE, fg=WHITE, activebackground='#245bd0', activeforeground=WHITE, relief='flat', font=('Segoe UI',12,'bold'), cursor='hand2').pack(fill='x', ipady=10)
        self.usuario_entry.focus(); self.contrasena_entry.bind('<Return>', lambda e:self.iniciar_sesion())
    def iniciar_sesion(self):
        u=self.usuario_entry.get().strip(); c=self.contrasena_entry.get().strip()
        if not u or not c: messagebox.showwarning('Campos incompletos','Debe completar usuario y contraseña.'); return
        obj=self.servicio.validar_acceso(u,c)
        if obj is None: messagebox.showerror('Acceso denegado','Usuario o contraseña incorrectos.'); return
        self.on_login_success(obj)
