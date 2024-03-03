from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def validate_phone(self, value):
        return value.isdigit() & len(value) == 10


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone : Phone):
        self.phones.append(phone)

    def remove_phone(self, phone : Phone):    
        self.phones.remove(phone)
        
    def edit_phone(self, phone : Phone, new_phone : Phone):    
        self.remove_phone(phone=phone)
        self.add_phone(phone=new_phone)

    def find_phone(self, phone : Phone):
        if phone in self.phones:
            return phone
        else:
            return f"{phone} not found"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record : Record):
        self.data.append(record)
    
    def find(self, name):
        if name in list(self.data.keys()):
            return self.data[name]

    def delete(self, name):
        self.data.pop(name)        
        
