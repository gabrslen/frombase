class Name:
    def __init__(self, name):
        self.name = name

    def is_valid(self):
        return self.validate_name()

    def validate_name(self):
        return isinstance(self.name, str) and 2 <= len(self.name)
