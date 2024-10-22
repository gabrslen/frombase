
import tkinter as tk
from tkinter import ttk
from control.controller import Control

class Terminal:
    def __init__(self):
        self.root = tk.Tk()
        self.selected_table = 'names_table'

        self.create_frames()
        self.create_widgets()
        self.create_buttons()
        self.create_treeview()

    def create_frames(self):
        self.entry_frame = ttk.Frame(self.root)
        self.entry_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.treeview_frame = ttk.Frame(self.root)
        self.treeview_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

    def create_widgets(self):
        self.label_nome = ttk.Label(self.entry_frame, text="Nome:")
        self.label_nome.grid(row=0, column=0)
        self.entry_nome = ttk.Entry(self.entry_frame)
        self.entry_nome.grid(row=0, column=1, padx=20)

    def create_buttons(self):
        self.create_button = ttk.Button(self.button_frame, text="Adicionar", command=self.add_recurso)
        self.create_button.grid(row=0, column=0)
        self.create_button = ttk.Button(self.button_frame, text="Buscar", command=None)
        self.create_button.grid(row=0, column=1)

    def create_treeview(self):
        for widget in self.treeview_frame.winfo_children():
            widget.destroy()
        self.columns = ('id', 'Nome')

        nomes_treeview = ttk.Treeview(self.treeview_frame, columns=self.columns, show="headings")
        for col in self.columns:
            nomes_treeview.heading(col, text=col)
            nomes_treeview.column(col, anchor=tk.CENTER)
            data = Control.get_full_names_table(self.selected_table)

        for row in data:
            nomes_treeview.insert("", tk.END, values=row)
        nomes_treeview.grid(row=0, column=0, padx=0, pady=0)

    def get_name_inputs(self):
            input_name = self.entry_nome.get()
            dicionario_info = {"nome": input_name}
            return self.selected_table, dicionario_info
    
    def add_recurso(self):
        table, values = self.get_name_inputs()
        Control.set_name_in_table(table, values)
        self.create_treeview()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Terminal()
    app.run()
