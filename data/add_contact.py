from model.contact import Contact
import random
import string

constant = [
        Contact(firstname="firstname1", lastname="lastname1", address="address1"),
        Contact(firstname="firstname2", lastname="lastname2", address="address2"),
    ]

def random_string(prefix,maxlen):
    # symbols = string.ascii_letters + string.digits+string.punctuation + "" * 10
    symbols = string.ascii_letters + string.digits + "" * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", address=""
            # homephone= "", mobilephone="", workphone="", fax="", email="", email2="", email3="",
            # homepage="", bday="", bmonth="", byear="", aday="", amonth="", ayear="", address2="", phone2="", notes=""
                    )] + [
            Contact(firstname=random_string("firstname", 20), lastname=random_string("lastname", 20),
            address=random_string("address", 5))

    for i in range(5)
]
