import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "No puedes agregar una tarea vacía.")

def mark_completed():
    try:
        selected_index = task_list.curselection()[0]
        task = task_list.get(selected_index)
        if not task.startswith("✔ "):
            task_list.delete(selected_index)
            task_list.insert(selected_index, "✔ " + task)
    except IndexError:
        messagebox.showwarning("Aviso", "Selecciona una tarea para marcar como completada.")

def delete_task():
    try:
        selected_index = task_list.curselection()[0]
        task_list.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Aviso", "Selecciona una tarea para eliminar.")

# Crear ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("500x400")  # Aumentar tamaño
root.eval('tk::PlaceWindow . center')  # Centrar en pantalla
root.configure(bg="#f0f0f0")  # Color de fondo

# Estilos generales
font_style = ("Arial", 12)
bg_color = "#ffffff"
button_style = {"font": ("Arial", 10, "bold"), "bg": "#007BFF", "fg": "white", "bd": 2, "relief": "raised"}

# Crear widgets
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

task_entry = tk.Entry(frame, font=font_style, width=40, bg=bg_color, relief="solid")
task_entry.grid(row=0, column=0, padx=5, pady=5)
task_entry.bind("<Return>", add_task)  # Agregar tarea con Enter

add_button = tk.Button(frame, text="Añadir Tarea", command=add_task, **button_style)
add_button.grid(row=0, column=1, padx=5, pady=5)

task_list = tk.Listbox(root, font=font_style, width=50, height=12, bg=bg_color, relief="solid")
task_list.pack(pady=10)

mark_button = tk.Button(root, text="Marcar como Completada", command=mark_completed, **button_style)
mark_button.pack(pady=5)

delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task, **button_style)
delete_button.pack(pady=5)

root.mainloop()
