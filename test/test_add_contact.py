# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix,maxlen):
    # symbols = string.ascii_letters + string.digits+string.punctuation + "" * 10
    symbols = string.digits + "" * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", address=""
            # homephone= "", mobilephone="", workphone="", fax="", email="", email2="", email3="",
            # homepage="", bday="", bmonth="", byear="", aday="", amonth="", ayear="", address2="", phone2="", notes=""
                    )] + [
            Contact(firstname=random_string("firstname", 20), lastname=random_string("lastname", 20),
            address=random_string("address", 5))

    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
        old_contacts = app.contact.get_contact_list()
        app.contact.creation_and_submit(contact)
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
# def test_add_group(app, group):
#     old_groups = app.group.get_group_list()
#     app.group.create(group)
#     assert len(old_groups) + 1 == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


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
