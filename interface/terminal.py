
import tkinter as tk
from tkinter import ttk
from control.names_control import NamesControl

class Terminal:
    def __init__(self):
        self.root = tk.Tk()

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
        self.label_name = ttk.Label(self.entry_frame, text="Name:")
        self.label_name.grid(row=0, column=0)
        self.entry_name = ttk.Entry(self.entry_frame)
        self.entry_name.grid(row=0, column=1, padx=20)

    def create_buttons(self):
        self.create_button = ttk.Button(self.button_frame, text="Add Name", command=self.add_name)
        self.create_button.grid(row=0, column=0)
        self.create_button = ttk.Button(self.button_frame, text="Search", command=self.search_names)
        self.create_button.grid(row=0, column=1)

    def create_treeview(self):
        for widget in self.treeview_frame.winfo_children():
            widget.destroy()
        self.columns = ('id', 'Name')

        nomes_treeview = ttk.Treeview(self.treeview_frame, columns=self.columns, show="headings")
        for col in self.columns:
            nomes_treeview.heading(col, text=col)
            nomes_treeview.column(col, anchor=tk.CENTER)
            data = NamesControl.get_full_names_table()

        for row in data:
            nomes_treeview.insert("", tk.END, values=row)
        nomes_treeview.grid(row=0, column=0, padx=0, pady=0)

    def get_name_inputs(self):
            input_name = self.entry_name.get()
            dicionario_info = {"name": input_name}
            return dicionario_info

    def add_name(self):
        values = self.get_name_inputs()
        NamesControl.set_name_in_table(values)
        self.create_treeview()

    def search_names(self):
        name_to_find = self.entry_name.get()
        result = NamesControl.get_names_in_table(name_to_find)
        print(result)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Terminal()
    app.run()
