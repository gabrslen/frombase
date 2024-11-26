import database.conn as db
from model.passwords import Password

table = 'passwords'

class PasswordsControl:

    @staticmethod
    def set_password_in_table(password, id_names, data_criacao, inativo):
        new_password = Password(password, id_names, data_criacao, inativo)
        print(new_password)
        # Criar o mecanismo para inserir o dado na table

    @staticmethod
    def get_password_in_table(data_to_search):
        return db.perform_search(data_to_search, table, 'password')

    @staticmethod
    def get_full_passwords_table():
        return db.perform_full_select(table)
