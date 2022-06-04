import re

# def test_phones_on_home_page(app):
#     contact_from_home_page = app.contact.get_contact_list()[0]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_home_page.all_phone_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#
# def test_email_on_home_page(app):
#     contact_from_home_page = app.contact.get_contact_list()[0]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)

def test_contact_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert merge_contact_data2(contact_from_home_page) == merge_contact_data(contact_from_edit_page)


def clear(s):
    return re.sub("[()-]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       (contact.homephone, contact.mobilephone, contact.workphone,  contact.phone2)))))


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       (contact.email, contact.email2, contact.email3)))))

def merge_contact_data(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       (contact.lastname, contact.firstname, contact.address, contact.email, contact.email2, contact.email3,
                                        contact.homephone, contact.mobilephone, contact.workphone, contact.phone2)))))

def merge_contact_data2(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       (contact.lastname, contact.firstname, contact.address, contact.all_email_from_home_page,
                                        contact.all_phone_from_home_page)))))