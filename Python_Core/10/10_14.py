class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts
        

    def add_contacts(self, name, phone, email, favorite):
        self.contact = {}
        self.contact["id"] = self.current_id
        self.contact["name"] = name
        self.contact["phone"] = phone
        self.contact["email"] = email
        self.contact["favorite"] = favorite
        self.contacts.append(self.contact)
        Contacts.current_id += 1
        print(self.contacts)
        return self.contacts