import tkinter as tk
from tkinter import ttk

def agregar_elemento():
    """Agrega el texto ingresado en el campo a la tabla."""
    texto = entrada_texto.get()
    if texto:
        tabla.insert("", "end", values=(texto,))
        entrada_texto.delete(0, tk.END)

def limpiar_lista():
    """Elimina todos los elementos de la tabla."""
    for item in tabla.get_children():
        tabla.delete(item)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")
ventana.geometry("400x400")
ventana.configure(bg="#f0f0f0")  # Color de fondo

# Etiqueta y campo de entrada
etiqueta = tk.Label(ventana, text="Ingrese un elemento:", font=("Arial", 12, "bold"), bg="#f0f0f0")
etiqueta.pack(pady=5)

entrada_texto = tk.Entry(ventana, font=("Arial", 12))
entrada_texto.pack(pady=5)

# Botón para agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento, font=("Arial", 12, "bold"), bg="#4caf50", fg="white", padx=10, pady=5)
boton_agregar.pack(pady=5)

# Tabla para mostrar datos
tabla = ttk.Treeview(ventana, columns=("Elemento",), show="headings")
tabla.heading("Elemento", text="Elemento")
tabla.pack(pady=5)

# Botón para limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista, font=("Arial", 12, "bold"), bg="#f44336", fg="white", padx=10, pady=5)
boton_limpiar.pack(pady=5)

# Ejecutar aplicación
ventana.mainloop()

