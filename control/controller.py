
import database.conn as db

class Control:

    def set_name_in_table(selected_table, data_to_insert):
        db.perform_insert(selected_table, data_to_insert)

    def select_names_in_table(selected_table, selected_column):
        names  = db.perform_select(selected_table, selected_column)
        return names
    
    def get_full_names_table(selected_table):
            names = db.perform_full_select(selected_table)
            return names
