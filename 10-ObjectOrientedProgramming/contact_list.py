import contact

class ContactList:
    def __init__(self):
        self.contact_list = []

    def add_contact(self,contact):
        self.contact_list.append(contact)

    def display_contacts(self):
        
        for contact in self.contact_list:
            contact_obj = contact.__dict__

            print(contact_obj['name'] + "   " + contact_obj['email'] + "   " + contact_obj['telephone'])






