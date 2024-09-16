import tkinter as tk
from tkinter import simpledialog

def leer_mascotas():
    ventana = tk.Tk()
    ventana.withdraw()

    mascotas = []
    for i in range(3):
        nombre = simpledialog.askstring(f"Mascota {i+1}", "Introduce el nombre de la mascota:")
        edad = simpledialog.askinteger(f"Mascota {i+1}", "Introduce la edad de la mascota:")
        especie = simpledialog.askstring(f"Mascota {i+1}", "Introduce la especie de la mascota:")
        mascotas.append((nombre, edad, especie))

    for i, mascota in enumerate(mascotas, start=1):
        print(f"Mascota {i}: Nombre: {mascota[0]}, Edad: {mascota[1]}, Especie: {mascota[2]}")

leer_mascotas()
