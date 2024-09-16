import tkinter as tk
from tkinter import simpledialog

def leer_clave():
    ventana = tk.Tk()
    ventana.withdraw()  # Ocultar la ventana principal

    clave = simpledialog.askstring("Clave Secreta", "Introduce tu clave:", show='*')

    if clave:
        print("Clave guardada correctamente")

leer_clave()
