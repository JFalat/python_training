from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_value2(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_contact_form(self, contact):
            wd = self.app.wd
            self.change_field_value("firstname", contact.firstname)
            self.change_field_value("middlename", contact.middlename)
            self.change_field_value("lastname", contact.lastname)
            self.change_field_value("nickname", contact.nickname)
            self.change_field_value("title", contact.title)
            self.change_field_value("company", contact.company)
            self.change_field_value("address", contact.address)
            self.change_field_value("mobile", contact.mobile)
            self.change_field_value("home", contact.home)
            self.change_field_value("work", contact.work)
            self.change_field_value("fax", contact.fax)
            self.change_field_value("email", contact.email)
            self.change_field_value("email2", contact.email2)
            self.change_field_value("email3", contact.email3)
            self.change_field_value("homepage", contact.homepage)
            self.change_field_value2("bday",contact.bday)
            self.change_field_value2("bmonth", contact.bday)
            self.change_field_value("byear", contact.byear)
            self.change_field_value2("aday", contact.bday)
            self.change_field_value2("amonth", contact.bday)
            self.change_field_value("ayear", contact.ayear)
            self.change_field_value("address2", contact.address2)
            self.change_field_value("phone2", contact.phone2)
            self.change_field_value("notes", contact.notes)

    def creation_and_submit(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # self.app.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value = 'Delete']").click()
        # self.return_to_home_page()
        WebDriverWait(wd, 10).until(EC.alert_is_present())
        wd.switch_to.alert.accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        # select first contact
        self.select_first_contact()
        # click edit contact
        wd.find_element_by_css_selector("img[alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # submit update
        wd.find_element_by_name("update").click()

    def go_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))
