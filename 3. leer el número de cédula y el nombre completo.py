import tkinter as tk
from tkinter import simpledialog

def leer_cedula_nombre():
    ventana = tk.Tk()
    ventana.withdraw()

    cedula = simpledialog.askstring("Cédula", "Introduce tu número de cédula:")
    nombre = simpledialog.askstring("Nombre Completo", "Introduce tu nombre completo:")

    if cedula and nombre:
        print(f"Cédula: {cedula}, Nombre: {nombre}")

leer_cedula_nombre()
