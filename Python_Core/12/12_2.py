import json

contacts = [{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
},
{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}]


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w') as file:
        data = {"contacts" : contacts}
        json.dump(data, file)
        


def read_contacts_from_file(filename):
    with open(filename, 'r') as file:
        contacts = json.load(file)["contacts"]

    return contacts

write_contacts_to_file("test.json", contacts)