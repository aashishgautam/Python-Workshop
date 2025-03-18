"""
This is a contact manager program that allows users to add and read contact from a file
"""

""""
create a contact manager lass
contacts list ma add contact with name phone
implement 3 methods
add contact
save contact
read contact
"""

class ContactManager:
    def __init__(self, filename="contact.txt"):
        self.contacts = []
        self.filename = filename
    
    def add_contact(self, name, phone):
        """ Adds passed contact to contact list """
        self.contacts.append ({"name": name, "phone": phone})

    def save_contact(self):
        """ Saves contact to the file """
        with open (self.filename, "w") as file:
            file.write(str(self.contacts))

    def load_contact(self):
        """ Loads contact from a file """
        with open (self.filename, "r") as file:
            print (file.read())


contact_manager = ContactManager()
contact_manager.add_contact ("Prajwol", "9812312322")
print(contact_manager.contacts)
contact_manager.add_contact("John Doe", "9812312322")
print(contact_manager.contacts)
contact_manager.save_contact()
contact_manager.load_contact()