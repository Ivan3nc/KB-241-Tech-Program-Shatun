class Student:
    def __init__(self, name, phone, group, email):
        self.name = name
        self.phone = phone
        self.group = group
        self.email = email

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.group}, {self.email}"