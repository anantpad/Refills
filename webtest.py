import os
import re
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

from enterData import submit_data

post_data = submit_data()
name = post_data[0]
gender = post_data[1]
dob = post_data[2][:10]
address = post_data[3]
city = post_data[4]
state = post_data[5]
zip = post_data[6]
phone = post_data[7]
presc = post_data[8]
medic = post_data[9]
strength = re.findall('\d+\D+.+(?=\s)', medic)
ndc = post_data[10]
qty = ''.join(c if c in map(str, range(0, 10)) else "" for c in post_data[11])
instr = post_data[12]
firstname = post_data[13]
lastname = post_data[14]

print(strength)

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
PrescriptionText.send_keys(presc)
# driver.close()

# Pharmacy Information
pharmacyDropDown = Select(driver.find_element_by_xpath("//*[@id='pharmacy']"))
pharmacyDropDown.select_by_index(2)

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
providerPhone = driver.find_element_by_xpath("//*[@id='prov_phone']").send_keys(os.getenv("PHONE"))
driver.find_element_by_xpath("//*[@id='prov_fax']").clear()
providerFax = driver.find_element_by_xpath("//*[@id='prov_fax']").send_keys(os.getenv("FAX"))

# Patient Information
first = driver.find_element_by_xpath("//*[@id='pat_fname']").send_keys(firstname)
last = driver.find_element_by_xpath("//*[@id='pat_lname']").send_keys(lastname)
sex = driver.find_element_by_xpath("//*[@id='pat_gen']").send_keys(gender)
birth = driver.find_element_by_xpath("//*[@id='pat_dob']").send_keys(dob)
address1 = driver.find_element_by_xpath("//*[@id='pat_address']").send_keys(address)
cities = driver.find_element_by_xpath("//*[@id='pat_city']").send_keys(city)
states = driver.find_element_by_xpath("//*[@id='pat_state']").send_keys(state)
zips = driver.find_element_by_xpath("//*[@id='pat_zip']").send_keys(zip)
phones = driver.find_element_by_xpath("//*[@id='pat_phone']").send_keys(phone)

# Medication Information
drugName = driver.find_element_by_xpath("//*[@id='drug_name']").send_keys(medic)
strngth = driver.find_element_by_xpath("//*[@id='drug_strength']").send_keys(strength)
ndcid = driver.find_element_by_xpath("//*[@id='NDCID']").send_keys(ndc)
quantity = driver.find_element_by_xpath("//*[@id='drug_quantity']").send_keys(qty)
refills = driver.find_element_by_xpath("//*[@id='drug_refills']").send_keys("1")
instructions = driver.find_element_by_xpath("//*[@id='drug_sig']").send_keys(instr)

submit_button = driver.find_elements_by_xpath('//*[@id="sendxml"]')[0]
submit_button.click()

# time.sleep(5)
# driver.close()
