import tkinter as tk
from tkinter import messagebox

ventana = None
entrada_nombre = None
entrada_numero = None
etiqueta_estado = None

def agreagar_persona():
    print("Agregar persona")
    
def limpiar_campos():
    print("Limpiar campos")

def construir_interfaz():
    global ventana, entrada_nombre, entrada_numero, etiqueta_estado
    ventana = tk.Tk()
    
    etiqueta_nombre = tk.Label(ventana, text="Nombre:")
    etiqueta_nombre.pack()
    entrada_nombre = tk.Entry(ventana)
    entrada_nombre.pack()
    
    etiqueta_numero = tk.Label(ventana, text="Numero:")
    etiqueta_numero.pack()
    entrada_numero= tk.Entry(ventana)
    entrada_numero.pack()
    
    boton_agregar = tk.Button(ventana, text="Agregar", command=agreagar_persona)
    boton_agregar.pack()
    boton_agregar = tk.Button(ventana, text="Limpiar", command=limpiar_campos)
    boton_agregar.pack()



def main():
    global ventana
    construir_interfaz()
    ventana.mainloop()

if __name__ == "__main__":
    main()