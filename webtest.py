import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv('.env')
username = os.getenv("PORTALLOGIN")
userpassword = os.getenv("PORTALPASSWORD")

# download the latest chrome driverand update the path here
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
url = "https://integration.drfirst.com/portal-integration-overview/script-2017-utility-message-tester/"
driver.get(url)
time.sleep(2)
UsernameTextBox = driver.find_element_by_xpath("//*[@id='user_login']")
UsernameTextBox.send_keys(username)

UserPassWord = driver.find_element_by_xpath("//*[@id='user_pass']")
UserPassWord.send_keys(userpassword)

LoginButton = driver.find_element_by_xpath("//*[@id='wp-submit']")
LoginButton.click()
time.sleep(3)

# Message Type
MessageTypeDropDown = Select(driver.find_element_by_xpath("//*[@id='message']"))
# MessageTypeDropDown.select_by_value("refill")
MessageTypeDropDown.select_by_index(1)

# Prescription Number
PrescriptionText = driver.find_element_by_xpath("//*[@id='serial_number']")
PrescriptionText.send_keys("1234234534678")
# driver.close()

# Pharmacy Information
pharmacyDropDown = Select(driver.find_element_by_xpath("//*[@id='pharmacy']"))
pharmacyDropDown.select_by_index(1)

# Provider Information
providerFirstName = driver.find_element_by_xpath("//*[@id='prov_fname']").send_keys(os.getenv("PROVFIRSTNAME"))
providerLastName = driver.find_element_by_xpath("//*[@id='prov_lname']").send_keys(os.getenv("PROVLASTNAME"))
providerNPI = driver.find_element_by_xpath("//*[@id='prov_npi']").send_keys(os.getenv("NPI"))
providerSPI = driver.find_element_by_xpath("//*[@id='SPI']").send_keys(os.getenv("SPI"))
driver.find_element_by_xpath("//*[@id='prov_address']").clear()
providerAddress = driver.find_element_by_xpath("//*[@id='prov_address']").send_keys(os.getenv("ADDRESS"))
driver.find_element_by_xpath("//*[@id='prov_city']").clear()
providerCity = driver.find_element_by_xpath("//*[@id='prov_city']").send_keys(os.getenv("CITY"))
driver.find_element_by_xpath("//*[@id='prov_state']").clear()
providerStateCode = driver.find_element_by_xpath("//*[@id='prov_state']").send_keys(os.getenv("STATECODE"))
driver.find_element_by_xpath("//*[@id='prov_zip']").clear()
providerZip = driver.find_element_by_xpath("//*[@id='prov_zip']").send_keys(os.getenv("ZIP"))
driver.find_element_by_xpath("//*[@id='prov_phone']").clear()
driver.find_element_by_xpath("//*[@id='prov_fax']").clear()
