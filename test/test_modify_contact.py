from model.contact import Contact


def test_modify_first_name(app):
    app.contact.modify_first_contact(Contact(name="New contact"))

def test_modify_middlename(app):
    app.contact.modify_first_contact(Contact(middlename="Middle contact"))


def test_modify_titlw(app):
    app.contact.modify_first_contact(Contact(title="title"))


