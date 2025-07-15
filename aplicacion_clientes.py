import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import clientes

class aplicacion_clientes:
    def __init__(self):
        self.cliente1 = clientes.Clientes()
        self.cliente1.crear_tabla()  
        self.ventana1 = tk.Tk()
        self.ventana1.title("Pedidos de Artículos de los Clientes - NicBread")
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.cargar_clientes()
        self.consultar_por_codigo()
        self.listado_completo()
        self.borrado()
        self.modificar()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def cargar_clientes(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de Clientes")
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Cliente")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1 = ttk.Label(self.labelframe1, text="Código (debe comenzar con 100):")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigocarga = tk.StringVar()
        self.entrycodigo = ttk.Entry(self.labelframe1, textvariable=self.codigocarga)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2 = ttk.Label(self.labelframe1, text="Nombre:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombrecarga = tk.StringVar()
        self.entrynombre = ttk.Entry(self.labelframe1, textvariable=self.nombrecarga)
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)
        self.label3 = ttk.Label(self.labelframe1, text="Contacto:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.contactocarga = tk.StringVar()
        self.entrycontacto = ttk.Entry(self.labelframe1, textvariable=self.contactocarga)
        self.entrycontacto.grid(column=1, row=2, padx=4, pady=4)
        self.boton1 = ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def agregar(self):
        codigo = self.codigocarga.get()
        nombre = self.nombrecarga.get().strip()
        contacto = self.contactocarga.get().strip()
        if not codigo.startswith("100"):
            mb.showerror("Error", "El código debe comenzar con 100")
            return
        if not nombre or not contacto:
            mb.showerror("Error", "Nombre y contacto no pueden estar vacíos")
            return
        datos = (codigo, nombre, contacto)
        self.cliente1.alta(datos)
        mb.showinfo("Información", "Los datos fueron correctamente cargados")
        self.codigocarga.set("")
        self.nombrecarga.set("")
        self.contactocarga.set()

    def consultar_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por Código")
        self.labelframe2 = ttk.LabelFrame(self.pagina2, text="Cliente")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        self.label1 = ttk.Label(self.labelframe2, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo = tk.StringVar()
        self.entrycodigo = ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2 = ttk.Label(self.labelframe2, text="Nombre:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombre = tk.StringVar()
        self.entrynombre = ttk.Entry(self.labelframe2, textvariable=self.nombre, state="readonly")
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)
        self.label3 = ttk.Label(self.labelframe2, text="Contacto:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.contacto = tk.StringVar()
        self.entrycontacto = ttk.Entry(self.labelframe2, textvariable=self.contacto, state="readonly")
        self.entrycontacto.grid(column=1, row=2, padx=4, pady=4)
        self.boton1 = ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos = (self.codigo.get(),)
        respuesta = self.cliente1.consulta(datos)
        if len(respuesta) > 0:
            self.nombre.set(respuesta[0][0])
            self.contacto.set(respuesta[0][1])
        else:
            self.nombre.set('')
            self.contacto.set('')
            mb.showinfo("Información", "No existe un cliente con el código pedido")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado Completo")
        self.labelframe3 = ttk.LabelFrame(self.pagina3, text="Cliente")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1 = ttk.Button(self.labelframe3, text="Listado Completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1 = st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0, row=1, padx=10, pady=10)

    def listar(self):
        respuesta = self.cliente1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, f"código: {fila[0]}\n"
                                             f"nombre: {fila[1]}\n"
                                             f"contacto: {fila[2]}\n\n")

    def borrado(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de Clientes")
        self.labelframe4 = ttk.LabelFrame(self.pagina4, text="Cliente")
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)
        self.label1 = ttk.Label(self.labelframe4, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigoborra = tk.StringVar()
        self.entryborra = ttk.Entry(self.labelframe4, textvariable=self.codigoborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        self.boton1 = ttk.Button(self.labelframe4, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos = (self.codigoborra.get(),)
        cantidad = self.cliente1.baja(datos)
        if cantidad == 1:
            mb.showinfo("Información", "Se borró el cliente con el código ingresado")
        else:
            mb.showinfo("Información", "No existe un cliente con el código escrito")

    def modificar(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar Cliente")
        self.labelframe5 = ttk.LabelFrame(self.pagina5, text="Cliente")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)
        self.label1 = ttk.Label(self.labelframe5, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigomod = tk.StringVar()
        self.entrycodigo = ttk.Entry(self.labelframe5, textvariable=self.codigomod)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2 = ttk.Label(self.labelframe5, text="Nombre:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombremod = tk.StringVar()
        self.entrynombre = ttk.Entry(self.labelframe5, textvariable=self.nombremod)
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)
        self.label3 = ttk.Label(self.labelframe5, text="Contacto:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.contactomod = tk.StringVar()
        self.entrycontacto = ttk.Entry(self.labelframe5, textvariable=self.contactomod)
        self.entrycontacto.grid(column=1, row=2, padx=4, pady=4)
        self.boton1 = ttk.Button(self.labelframe5, text="Consultar", command=self.consultar_mod)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)
        self.boton2 = ttk.Button(self.labelframe5, text="Modificar", command=self.modifica)
        self.boton2.grid(column=1, row=4, padx=4, pady=4)

    def modifica(self):
        datos = (self.nombremod.get(), self.contactomod.get(), self.codigomod.get())
        cantidad = self.cliente1.modificar(datos)
        if cantidad == 1:
            mb.showinfo("Información", "Se modificó el cliente")
        else:
            mb.showinfo("Información", "No existe un cliente con código mencionado")

    def consultar_mod(self):
        datos = (self.codigomod.get(),)
        respuesta = self.cliente1.consulta(datos)
        if len(respuesta) > 0:
            self.nombremod.set(respuesta[0][0])
            self.contactomod.set(respuesta[0][1])
        else:
            self.nombremod.set('')
            self.contactomod.set('')
            mb.showinfo("Información", "No existe un cliente con código mencionado")

if __name__ == "__main__":
    aplicacion1 = aplicacion_clientes()