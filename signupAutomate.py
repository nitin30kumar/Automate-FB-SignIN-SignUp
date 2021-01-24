from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

#Steps for facebook signup -
#for signup we need:
#firstname lastname
#working email address
#global recognised password
#date of birth with 3 dropdown
#gender with 3 radiobutton
#signup button

#email confirmation button

driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")

#signup process begins here !!!

#user input for the information
firstname=input("Enter your firstname:")
lastname=input("Enter your lastname:")
email_id=input("Enter your email:")
password=input("Enter your strong password:")
date_ob=int(input("Enter only DATE of birth"))
month_ob=int(input("Enter only MONTH of birth:(month number)"))
year_ob=int(input("Enter only YEAR of birth"))
gender=input("Enter your gender: (Female, Male)")

#taking some time to fill details
print("\n\nPlease wait while we fill your data into the website ...\n\n")


#link for Facebook Sign up
driver.get("https://www.facebook.com/r.php")

#open gmailnator for gmail id
driver.execute_script('''window.open("https://gmailnator.com","_blank");''')

#clicks on "Click here for custom email" button
driver.find_element_by_xpath("/html/body/section/div[1]/div/div/div[2]/div/div[4]/a[2]").click()

#taking input for pre-email text
driver.find_element_by_xpath("/html/body/section/div[1]/div/div/div[2]/div/div[5]/div[1]/input").send_keys(firstname,date_ob,month_ob,year_ob)

#click on Go
driver.find_element_by_xpath("/html/body/section/div[1]/div/div/div[2]/div/div[5]/div[1]/div[2]/button").click()

#------------------------------------------------------

#Switch to signup facebook tab
driver.switch_to.window(driver.window_handles[0])


#input for firstname
driver.find_element_by_name("firstname").send_keys(str(firstname))

#input for lasttname
driver.find_element_by_name("lastname").send_keys(str(lastname))

#input for email
driver.find_element_by_name("reg_email__").send_keys(str(email_id))

#input for reemail
driver.find_element_by_name("reg_email_confirmation__").send_keys(str(email_id))

#input for password
driver.find_element_by_name("reg_passwd__").send_keys(str(password))

#input for only date of birth
date_birth=driver.find_element_by_id("day")
element=Select(date_birth)
element.select_by_value(str(date_ob))

#input for only month of birth
month_birth=driver.find_element_by_id("month")
element=Select(month_birth)
element.select_by_value(str(month_ob))

#input for only year of birth
year_birth=driver.find_element_by_id("year")
element=Select(year_birth)
element.select_by_value(str(year_ob))

#input for gender
if gender=="Female":
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[1]/input").click()
elif gender=="Male":
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/input").click()
else:
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[3]/input").click()


#Signup button click
driver.find_element_by_name("websubmit").click()

#switch to gmailnator tab
driver.switch_to.window(driver.window_handles[1])


#search for the 6 digit code
cnfrm_code =

#switch to facebook signup page
driver.switch_to.window(driver.window_handles[0])

#paste the code in below input element



#print("Account created successfully")


