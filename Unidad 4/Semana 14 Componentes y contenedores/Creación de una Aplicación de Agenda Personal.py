import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("700x450")

        # Frame para la entrada de datos
        frame_input = tk.Frame(root)
        frame_input.pack(pady=10)

        tk.Label(frame_input, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(frame_input, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(frame_input, width=15)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(frame_input, width=30)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botones
        frame_buttons = tk.Frame(root)
        frame_buttons.pack(pady=10)

        tk.Button(frame_buttons, text="Agregar Evento", command=self.add_event).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame_buttons, text="Eliminar Evento", command=self.delete_event).grid(row=0, column=1, padx=5,
                                                                                         pady=5)
        tk.Button(frame_buttons, text="Salir", command=root.quit).grid(row=0, column=2, padx=5, pady=5)

        # Lista de eventos
        self.tree = ttk.Treeview(root, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

    def add_event(self):
        fecha = self.date_entry.get()
        hora = self.time_entry.get()
        descripcion = self.desc_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", tk.END, values=(fecha, hora, descripcion))
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")

    def delete_event(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Error", "Seleccione un evento para eliminar")
            return

        confirm = messagebox.askyesno("Confirmación", "¿Seguro que desea eliminar el evento seleccionado?")
        if confirm:
            self.tree.delete(selected_item[0])


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
