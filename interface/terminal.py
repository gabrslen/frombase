# terminal.py

import tkinter as tk
from interface.names_form import NamesForm
import requests

class Terminal:
    def __init__(self):
        self.root = tk.Tk()
        self.names_form = NamesForm(
            root=self.root,
            add_name_command=self.add_name,
            search_command=self.search_names
        )
        self.search_names()

    def get_name_inputs(self):
        input_name = self.names_form.entry_name.get()
        return {"name": input_name}

    def add_name(self):
        values = self.get_name_inputs()
        try:
            response = requests.post("http://localhost:5000/set_name", json=values)
            if response.status_code == 201:
                get_response = requests.get("http://localhost:5000/get_names")
                if get_response.status_code == 200:
                    data = get_response.json()
                    self.names_form.update_treeview(data)
                else:
                    print(f"Error fetching Names from list: {get_response.json().get('details', 'Unknown Error!')}")
            else:
                print(f"Error saving Name: {response.json().get('details', 'Unknown Error!')}")
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to API: {e}")


    def search_names(self):
        name_to_find = self.names_form.entry_name.get()
        params = {"name": name_to_find} if name_to_find else {}
        try:
            response = requests.get("http://localhost:5000/get_names", params=params)
            if response.status_code == 200:
                result = response.json()
                self.names_form.update_treeview(result)
            else:
                print(f"Error fetching Name: {response.json().get('details', 'Unknown Error!')}")
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to API: {e}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Terminal()
    app.run()
