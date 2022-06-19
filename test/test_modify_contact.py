from model import contact
from model.contact import Contact
import random

def test_modify_first_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.creation_and_submit(Contact(firstname="rwerwer"))
    old_contacts = db.get_contact_list()
    contacts = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contacts.id, contacts)
    new_contact = db.get_contact_list()
    assert len(old_contacts) == len(new_contact)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
