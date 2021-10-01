from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time
from twilio.rest import Client

client = Client("ACe3b244dd7ea3ff1d29eb7bfa469770f3", "7a41d6e53e9f1302460a0e389a9e419a")

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

failedatts = 0
Firstname = "Muhammad"
Lastname = "Janjua"
MVID = "088158084"
DOB = "2000/08/01"
email = "mojanjua15@gmail.com"


driver.get("https://scheduler.itialb4dmv.com/SchAlberta/Applicant/Information")



booknew = driver.find_element_by_id("btnBookAppt")
actions = ActionChains(driver)

actions.double_click(booknew).perform()

buytest = driver.find_element_by_id("invalidPermit")
actions = ActionChains(driver)

actions.double_click(buytest).perform()

while True:
    t = time.localtime()
    current_hour = time.strftime("%H", t)
    if current_hour=='21':
        time.sleep(10800)

    
    driver.get("https://scheduler.itialb4dmv.com/SchAlberta/Applicant/Information")


    driver.find_element(By.ID, 'FirstName').send_keys(Firstname)
    driver.find_element(By.ID, 'LastName').send_keys(Lastname)
    driver.find_element(By.ID, 'MVID').send_keys(MVID)
    driver.find_element(By.ID, 'Birthdate').send_keys(DOB)
    driver.find_element(By.ID, 'Email').send_keys(email)

    #click custom checkbox
    element = driver.find_element_by_id('isTermsAccepted')

    driver.execute_script("arguments[0].click();", element)

    nextb = driver.find_element_by_xpath('//*[@id="formSubmit"]')
    driver.execute_script("arguments[0].click();", nextb)



    #------------------------next page
    test = driver.find_element_by_xpath('//*[@id="serviceGroupList"]')
    drp = Select(test)
    drp.select_by_value("7")#basic road test

    element = driver.find_element_by_id('isTermsAccepted')

    driver.execute_script("arguments[0].click();", element)


    accept = driver.find_element_by_xpath('//*[@id="acceptTerms"]')
    driver.execute_script("arguments[0].click();", accept)

    #search location
    city = 'Calgary'
    kms = '25'
    driver.find_element(By.ID, 'cityNameSearch').send_keys(city)

    dist = driver.find_element_by_xpath('//*[@id="citySearchRadius"]')
    drp = Select(dist)
    drp.select_by_value(kms)

    search = driver.find_element_by_xpath('//*[@id="searchSelectedLocation"]')
    driver.execute_script("arguments[0].click();", search)

    # APPOINTMENTS PAGE
    noapp = 'No available appointment slots found for the selected criteria. Please go back and change your search to try again.'
    try:
        if (driver.find_element_by_class_name('text-danger').text == noapp):
            result = 'No openings'
            print(result)
            failedatts = failedatts + 1
            client.messages.create(to="+15877000257", 
                       from_="+12513255241", 
                       body=result)

        else:
            result = 'BOOK NOW in {}!'.format(city)
            print(result)
            client.messages.create(to="+15877000257", 
                       from_="+12513255241", 
                       body=result)
            #enter notification info
            time.sleep(60)

    except:
        result = 'BOOK NOW opening in {}!'.format(city)
        print(result)
        client.messages.create(to="+15877000257", 
                       from_="+12513255241", 
                       body=result)
        time.sleep(60)