import tkinter as tk
from interface.names_form import NamesForm
from control.names_control import NamesControl

class Terminal:
    def __init__(self):
        self.root = tk.Tk()
        self.names_form = NamesForm(
            root=self.root,
            add_name_command=self.add_name,
            search_command=self.search_names
        )

    def get_name_inputs(self):
        input_name = self.names_form.entry_name.get()
        return {"name": input_name}

    def add_name(self):
        values = self.get_name_inputs()
        NamesControl.set_name_in_table(values)
        self.names_form.create_treeview()

    def search_names(self):
        name_to_find = self.names_form.entry_name.get()
        result = NamesControl.get_names_in_table(name_to_find)
        print(result)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Terminal()
    app.run()
