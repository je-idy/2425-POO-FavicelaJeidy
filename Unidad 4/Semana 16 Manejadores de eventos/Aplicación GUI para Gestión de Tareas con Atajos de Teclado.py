import tkinter as tk
from tkinter import messagebox

# Clase principal de la aplicación
class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")  # Título de la ventana
        self.root.geometry("400x400")         # Tamaño de la ventana

        # ---------- Campo de entrada para nuevas tareas ----------
        self.entry = tk.Entry(root, font=('Arial', 14))  # Entrada de texto
        self.entry.pack(pady=10, fill=tk.X, padx=10)     # Empaquetado con espacio
        self.entry.bind("<Return>", self.add_task)       # Atajo: Enter para añadir tarea

        # ---------- Lista donde se muestran las tareas ----------
        self.tasks_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=('Arial', 14))
        self.tasks_listbox.pack(pady=10, fill=tk.BOTH, expand=True, padx=10)

        # ---------- Frame para los botones ----------
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        # Botón para añadir tarea
        self.add_button = tk.Button(self.button_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        # Botón para marcar como completada
        self.complete_button = tk.Button(self.button_frame, text="Marcar Completada", command=self.complete_task)
        self.complete_button.grid(row=0, column=1, padx=5)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(self.button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        # ---------- Atajos de teclado ----------
        self.root.bind("<c>", lambda event: self.complete_task())      # 'c' para completar
        self.root.bind("<C>", lambda event: self.complete_task())      # 'C' para completar
        self.root.bind("<d>", lambda event: self.delete_task())        # 'd' para eliminar
        self.root.bind("<D>", lambda event: self.delete_task())        # 'D' para eliminar
        self.root.bind("<Delete>", lambda event: self.delete_task())   # Suprimir para eliminar
        self.root.bind("<Escape>", lambda event: root.quit())          # Escape para salir

        # ---------- Lista interna para guardar tareas ----------
        # Cada tarea es una tupla: (texto, estado de completado)
        self.tasks = []

    # ---------- Función para añadir una nueva tarea ----------
    def add_task(self, event=None):
        task_text = self.entry.get().strip()  # Obtiene y limpia el texto
        if task_text:
            self.tasks.append((task_text, False))  # Agrega tarea no completada
            self.entry.delete(0, tk.END)           # Limpia el campo de entrada
            self.refresh_tasks()                   # Actualiza la lista en pantalla
        else:
            # Alerta si el campo está vacío
            messagebox.showwarning("Campo vacío", "Escribe una tarea antes de añadirla.")

    # ---------- Función para marcar tarea como completada ----------
    def complete_task(self):
        selection = self.tasks_listbox.curselection()  # Obtiene tarea seleccionada
        if selection:
            index = selection[0]
            task_text, _ = self.tasks[index]           # Obtiene el texto original
            self.tasks[index] = (task_text, True)      # Marca como completada
            self.refresh_tasks()                       # Actualiza la lista

    # ---------- Función para eliminar una tarea ----------
    def delete_task(self):
        selection = self.tasks_listbox.curselection()  # Tarea seleccionada
        if selection:
            index = selection[0]
            del self.tasks[index]                      # Elimina de la lista
            self.refresh_tasks()                       # Actualiza la lista

    # ---------- Función para actualizar visualmente la lista ----------
    def refresh_tasks(self):
        self.tasks_listbox.delete(0, tk.END)  # Limpia la lista actual
        for task, completed in self.tasks:
            display_text = task + (" ✔️" if completed else "")  # Añade icono si está completada
            self.tasks_listbox.insert(tk.END, display_text)     # Muestra en pantalla

            # Cambia el estilo visual si está completada
            if completed:
                self.tasks_listbox.itemconfig(tk.END, fg="gray", font=('Arial', 14, 'overstrike'))
            else:
                self.tasks_listbox.itemconfig(tk.END, fg="black", font=('Arial', 14))

# ---------- Ejecutar la aplicación ----------
if __name__ == "__main__":
    root = tk.Tk()            # Crea la ventana principal
    app = TaskManager(root)   # Crea la instancia de la app
    root.mainloop()           # Ejecuta el bucle principal de Tkinter
