# -*- coding: utf-8 -*-
from model import contact
from model.contact import Contact

def test_add_contact(app):
        old_contacts = app.contact.get_contact_list()
        contact = Contact(firstname="Joanna", middlename="Test", lastname="LastTest", nickname="Test1", title="Test2", company="TestCompany", address="abc",
                                                homephone= "12345678", mobilephone="123456789", workphone="123456", fax="12345", email="a@a.com", email2="b@b.com", email3="c@c.com",
                                                homepage="aaa", bday="15", bmonth="May", byear="1970", aday="21", amonth="December", ayear="1980", address2="werewr", phone2="123456", notes="abc")
        app.contact.creation_and_submit(contact)
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#
# def test_add_empty_contact(app):
#         old_contacts = app.contact.get_contact_list()
#         app.contact.creation_and_submit(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="", mobile="", work="", fax="", email="", email2="", email3="",
#                                                 homepage="", bday="-", bmonth="-", byear="-", aday="-", amonth="-", ayear="-", address2="", phone2="", notes=""))
#         app.contact.creation_and_submit(contact)
#         new_contacts = app.contact.get_contact_list()
#         assert len(old_contacts) + 1 == len(new_contacts)
#         old_contacts.append(contact)
#         assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
