from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PlayerFormTest(LiveServerTestCase):

  def testform(self):
    selenium = webdriver.Chrome()
    selenium.get('http://127.0.0.1:8000/signin')

    username = selenium.find_element("id", "username") 
    password = selenium.find_element("id", "password")
    selenium.find_element('id','signin').click()

    assert 'Sign' in selenium.page_source