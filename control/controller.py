import database.conn as db
from model.names_class import Name
import tkinter as tk
from tkinter import messagebox

class Control:

    def set_name_in_table(selected_table, data_to_insert):

        new_name = Name(name=data_to_insert.get('nome'))

        if new_name.is_valid():
            db.perform_insert(selected_table, data_to_insert)
        else:
            root = tk.Tk()
            root.withdraw()  # Esconde a janela principal do Tkinter
            messagebox.showerror("Erro de Validação", "Dados inválidos: Verifique o nome.")
            root.destroy()  # Fecha a janela oculta após a exibição do erro

    def select_names_in_table(selected_table, selected_column):
        names = db.perform_select(selected_table, selected_column)
        return names
    
    def get_full_names_table(selected_table):
        names = db.perform_full_select(selected_table)
        return names
