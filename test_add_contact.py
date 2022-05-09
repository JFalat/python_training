# -*- coding: utf-8 -*-
from application_contact import ApplicationContact
import pytest
from contact import Contact

@pytest.fixture
def app(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
        app.login(username="admin", password="secret")
        app.contact_creation_and_submit(Contact(firstname= "Joanna", middlename="Test", lastname="LastTest", nickname="Test1", title="Test2", company="TestCompany", address="abc",
                                         mobile="123456789", home= "12345678", work="123456", fax="12345", email="a@a.com", email2="b@b.com", email3="c@c.com",
                                         homepage="aaa",
                                                bday="15",
                                                bmonth="May",
                                                byear="1970",
                                                aday="21",
                                                amonth="December",
                                                ayear="1980",
                                                address2="werewr",
                                                phone2="123456",
                                                notes="abc"))
        app.logout()


def test_add_empty_contact(app):
        app.login(username="admin", password="secret")
        app.contact_creation_and_submit(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", mobile="", home="", work="", fax="", email="", email2="", email3="",
                                         homepage="", bday="-", bmonth="-", byear="-", aday="-", amonth="-", ayear="-", address2="", phone2="", notes=""))
        app.logout()

