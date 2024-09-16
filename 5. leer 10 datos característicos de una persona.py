import tkinter as tk
from tkinter import simpledialog

def leer_datos_persona():
    ventana = tk.Tk()
    ventana.withdraw()

    datos = {}
    campos = ["Nombre", "Edad", "Género", "Altura", "Peso", "Nacionalidad", "Profesión", "Estado Civil", "Dirección", "Teléfono"]

    for campo in campos:
        valor = simpledialog.askstring("Datos de la Persona", f"Introduce tu {campo}:")
        datos[campo] = valor

    for campo, valor in datos.items():
        print(f"{campo}: {valor}")

leer_datos_persona()
