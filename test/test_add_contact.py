# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits+string.punctuation + "" * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company=""
            # homephone= "", mobilephone="", workphone="", fax="", email="", email2="", email3="",
            # homepage="", bday="", bmonth="", byear="", aday="", amonth="", ayear="", address2="", phone2="", notes=""
                    )] + [
            Contact(firstname=random_string("firstname", 20), middlename=random_string("middlename", 20), lastname=random_string("lastname", 20),
            nickname=random_string("nickname", 10), title=random_string("title", 5), company=random_string("company", 7))
            #         ,
            # homephone= random_string("homephone",10), mobilephone=random_string("mobilephone",10), workphone=random_string("workphone",10),
            # fax=random_string("fax",10), email=random_string("email",10), email2=random_string("email2",10), email3=random_string("email3",10),
            # homepage=random_string("homepage",10), bday=random_string("bday",10), bmonth=random_string("bmonth",10),
            # byear=random_string("byear",10), aday=random_string("aday",10), amonth=random_string("amonth",10),
            # ayear=random_string("ayear",10), address2=random_string("address2",10), phone2=random_string("phone2",10), notes=random_string("notes",10))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
        old_contacts = app.contact.get_contact_list()
        # contact = Contact(firstname="Joanna", middlename="Test", lastname="LastTest", nickname="Test1", title="Test2", company="TestCompany", address="abc",
        #                                         homephone= "12345678", mobilephone="123456789", workphone="123456", fax="12345", email="a@a.com", email2="b@b.com", email3="c@c.com",
        #                                         homepage="aaa", bday="15", bmonth="May", byear="1970", aday="21", amonth="December", ayear="1980", address2="werewr", phone2="123456", notes="abc")
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
