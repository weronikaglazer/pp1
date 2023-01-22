import contact
import contact_list


contact1 = contact.Contact("John Brown","brown@onet.pl","555234000")
contact2 = contact.Contact("Anna May", "am@o2.pl", "232000199")
contact3 = contact.Contact("George Small", "smallg@google.pl", "222999100")
contact4 = contact.Contact("Paola Big", "bigpaola@poczta.pl", "100200300")


my_contacts = contact_list.ContactList()
my_contacts.add_contact(contact1)
my_contacts.add_contact(contact2)
my_contacts.add_contact(contact3)
my_contacts.add_contact(contact4)
my_contacts.display_contacts()

