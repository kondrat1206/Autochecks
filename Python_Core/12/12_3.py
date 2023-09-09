import csv


contacts = [{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False}, {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}]


def write_contacts_to_file(filename, contacts):

    with open(filename, 'w', newline='') as file:
        if len(contacts) > 0:
            fieldnames = contacts[0].keys()
        else:
            fieldnames = []
        writer = csv.DictWriter(file, fieldnames, delimiter=',')
        writer.writeheader()
        for contact in contacts:
            writer.writerow(rowdict=contact)
        
        
def read_contacts_from_file(filename):

    unserialized = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            if row["favorite"] == "True":
                row["favorite"] = True
            else:
                row["favorite"] = False
            unserialized.append(row)
    
    return unserialized

write_contacts_to_file("test.csv", contacts)
read_contacts_from_file("test.csv")