import tkinter as tk
from tkinter import ttk
from control.names_control import NamesControl

class NamesForm:
    def __init__(self, root, add_name_command, search_command):
        self.root = root
        self.add_name_command = add_name_command
        self.search_command = search_command
        self.entry_frame, self.button_frame, self.treeview_frame = self.create_frames()
        self.entry_name = self.create_widgets()
        self.create_buttons()
        self.create_treeview()

    def create_frames(self):
        entry_frame = ttk.Frame(self.root)
        entry_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        button_frame = ttk.Frame(self.root)
        button_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        treeview_frame = ttk.Frame(self.root)
        treeview_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=20)
        return entry_frame, button_frame, treeview_frame

    def create_widgets(self):
        label_name = ttk.Label(self.entry_frame, text="Name:")
        label_name.grid(row=0, column=0)
        entry_name = ttk.Entry(self.entry_frame)
        entry_name.grid(row=0, column=1, padx=20)
        return entry_name

    def create_buttons(self):
        create_button = ttk.Button(self.button_frame, text="Add Name", command=self.add_name_command)
        create_button.grid(row=0, column=0)
        search_button = ttk.Button(self.button_frame, text="Search", command=self.search_command)
        search_button.grid(row=0, column=1)

    def create_treeview(self):
        for widget in self.treeview_frame.winfo_children():
            widget.destroy()
        columns = ('id', 'Name')

        self.nomes_treeview = ttk.Treeview(self.treeview_frame, columns=columns, show="headings")
        for col in columns:
            self.nomes_treeview.heading(col, text=col)
            self.nomes_treeview.column(col, anchor=tk.CENTER)

        data = NamesControl.get_full_names_table()
        for row in data:
            self.nomes_treeview.insert("", tk.END, values=row)

        self.nomes_treeview.grid(row=0, column=0, padx=0, pady=0)
