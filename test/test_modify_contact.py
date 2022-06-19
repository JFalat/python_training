from model.contact import Contact
from random import randrange

def test_modify_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="rwerwer"))
        old_contacts = app.contact.get_contact_list()
        index = randrange(len(old_contacts))
        contacts = Contact(firstname="rwerwer")
        contacts.id = old_contacts[index].id
        app.group.modify_contact_by_index(index, contacts)
        new_contact = app.contact.get_contact_list()
        assert len(old_contacts) == len(new_contact)
        old_contacts[index] = contacts
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
