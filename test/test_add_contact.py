# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
        contacts = json_contacts
        old_contacts = db.get_contact_list()
        app.contact.creation_and_submit(contacts)
        # assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = db.get_contact_list()
        old_contacts.append(contacts)
        if check_ui:
                assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
