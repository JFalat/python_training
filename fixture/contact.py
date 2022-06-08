import re

from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.wd = None
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
            # wd.find_element_by_name(field_name).clear()
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
            self.change_field_value("mobile", contact.mobilephone)
            self.change_field_value("home", contact.homephone)
            self.change_field_value("work", contact.workphone)
            self.change_field_value("fax", contact.fax)
            self.change_field_value("email", contact.email)
            self.change_field_value("email2", contact.email2)
            self.change_field_value("email3", contact.email3)
            self.change_field_value("homepage", contact.homepage)
            self.change_field_value2("bday",contact.bday)
            self.change_field_value2("bmonth", contact.bmonth)
            self.change_field_value("byear", contact.byear)
            self.change_field_value2("aday", contact.aday)
            self.change_field_value2("amonth", contact.amonth)
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
        wd.find_element_by_name("submit").click()
        # self.go_to_home_page()
        self.contact_cache = None

    def delete_first_group(self):
        self.delete_contact_by_index(0)

    def modify_first_group(self):
        self.modify_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value = 'Delete']").click()
        # self.return_to_home_page()
        WebDriverWait(wd, 10).until(EC.alert_is_present())
        wd.switch_to.alert.accept()
        # self.return_to_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        # select first contact
        self.select_contact_by_index()
        # click edit contact
        wd.find_element_by_css_selector("img[alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # submit update
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def go_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook.php") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                address= cells[3].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_email = cells[4].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                                                  all_phones_from_home_page = all_phones, all_email_from_home_page = all_email))
        return list(self.contact_cache)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, homephone=homephone, workphone=workphone, mobilephone=mobilephone,
                    phone2=phone2, email=email, email2=email2, email3=email3)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, phone2=phone2)




