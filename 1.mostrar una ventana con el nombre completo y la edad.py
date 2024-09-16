import tkinter as tk

def mostrar_nombre_edad():
    ventana = tk.Tk()
    ventana.title("Nombre y Edad")

    nombre = "Juan Pérez"
    edad = 25

    etiqueta = tk.Label(ventana, text=f"Nombre: {nombre}\nEdad: {edad} años", font=("Arial", 16))
    etiqueta.pack(expand=True)

    ventana.mainloop()

mostrar_nombre_edad()
