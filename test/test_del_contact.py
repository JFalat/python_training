import random

from model.contact import Contact
from random import randrange

def test_delete_first_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.creation_and_submit(Contact(firstname="rwerwer"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts








