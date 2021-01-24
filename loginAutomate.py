from selenium import webdriver
from getpass import getpass

username = "Blackeagleindian123@gmailnator.com"
password = "b1@ckEag1E"

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.facebook.com/")

username_textbox = driver.find_element_by_id("email")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("pass")
password_textbox.send_keys(password)

login_button = driver.find_element_by_id("u_0_b")
login_button.submit()



