class Name:
    def __init__(self, name):
        self.name = name

    def is_valid(self):
        valid, message = self.validate_name()
        if not valid:
            print(f"Validation Error: {message}")
        return valid, message

    def validate_name(self):
        if not isinstance(self.name, str):
            return False, "Nome deve ser uma string."
        if len(self.name.strip()) <= 2:
            return False, "Nome deve ter mais de 2 caracteres."
        if not self.name.isalpha():
            return False, "Nome deve conter apenas letras."
        return True, "Nome válido."
