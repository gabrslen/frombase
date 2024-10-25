
import tkinter as tk
from tkinter import messagebox
import database.conn as db
from model.names_class import Name

table = 'names_table'

class NamesControl:

    def set_name_in_table(data_to_insert):
        new_name = Name(name=data_to_insert.get('nome'))
        if new_name.is_valid():
            db.perform_insert(table, data_to_insert)
        else:
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Erro de Validação", "Dados inválidos: Verifique o nome.")
            root.destroy()

    def get_names_in_table(data_to_search):
        names = db.perform_search(data_to_search, table, 'name')
        return names
    
    def get_full_names_table():
        names = db.perform_full_select(table)
        return names
