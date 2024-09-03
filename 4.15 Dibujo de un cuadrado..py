import tkinter as tk
from tkinter import ttk


def dibujar_cuadrado_bordes(tamano):
    if tamano < 2:
        return "*"

    cuadrado = []
    for i in range(tamano):
        if i == 0 or i == tamano - 1:
            cuadrado.append('*' * tamano)
        else:
            cuadrado.append('*' + ' ' * (tamano - 2) + '*')

    return '\n'.join(cuadrado)


def mostrar_cuadrado():
    try:
        tamano = int(entrada_tamano.get())
        if tamano <= 0:
            raise ValueError("El tamaño debe ser un número positivo.")

        cuadrado = dibujar_cuadrado_bordes(tamano)
        etiqueta_resultado.config(text=cuadrado)

    except ValueError as e:
        etiqueta_resultado.config(text=f"Error: {e}")


# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Dibujador de Cuadrado con Bordes")
ventana.geometry("400x400")

# Widgets
frame = ttk.Frame(ventana, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Tamaño del cuadrado:").grid(column=0, row=0, sticky=tk.W, pady=5)
entrada_tamano = ttk.Entry(frame, width=10)
entrada_tamano.grid(column=1, row=0, sticky=tk.W, pady=5)

ttk.Button(frame, text="Dibujar", command=mostrar_cuadrado).grid(column=0, row=1, columnspan=2, pady=10)

etiqueta_resultado = tk.Label(frame, text="", font=("Courier", 12), justify=tk.LEFT, anchor="w")
etiqueta_resultado.grid(column=0, row=2, columnspan=2, pady=5)

ventana.mainloop()

