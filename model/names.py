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
            return False, "Name must be a string."
        if len(self.name.strip()) <= 2:
            return False, "Name must be longer than 2 characters."
        if not self.name.isalpha():
            return False, "Name must contain only letters."
        return True, "Valid name."
