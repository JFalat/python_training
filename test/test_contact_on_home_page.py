from pony.orm import Database

from model.contact import Contact
from fixture.orm import ORMFixture

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
db = Database()

def test_add_contact(app, db, orm, check_ui):
        # contacts = json_contacts
        old_contacts = db.get_contact_list()
        # assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = orm.get_contact_list()
        # old_contacts.append(contacts)
        if check_ui:
                assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
