list_contacts = [
{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
},
{
    "name": "Allen Raymond",
    "email": "nulla1.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
]

def get_emails(list_contacts):
    
    obj = map(get_email, list_contacts)
    result = list(obj)
    print(result)
    return result

        
    

def get_email(dic):
    
    email = dic["email"]
    return email


get_emails(list_contacts)