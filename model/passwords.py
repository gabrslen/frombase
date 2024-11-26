class Password:
    def __init__(self, password, id_names, data_criacao, inativo):
        self.password = password
        self.id_names = id_names
        self.data_criacao = data_criacao
        self.inativo = inativo

    def is_valid(self):
        valid, message = self.validate_password()
        if not valid:
            print(f"Validation Error: {message}")
        return valid, message

    def validate_password(self):
        if not isinstance(self.password, str):
            return False, "Password must be a string."
        if len(self.password.strip()) <= 8:
            return False, "Password must be longer than 8 characters."
        return True, "Valid password."
