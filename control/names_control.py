import database.conn as db
from model.names_class import Name

table = 'names_table'

class NamesControl:

    @staticmethod
    def set_name_in_table(data_to_insert):
        new_name = Name(name=data_to_insert.get('name'))
        valid, message = new_name.is_valid()
        if valid:
            db.perform_insert(table, data_to_insert)
        else:
            raise ValueError(message)

    @staticmethod
    def get_names_in_table(data_to_search):
        return db.perform_search(data_to_search, table, 'name')

    @staticmethod
    def get_full_names_table():
        return db.perform_full_select(table)
