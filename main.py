from datetime import datetime
import time
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def printMenu():
  rows, cols = os.popen('stty size', 'r').read().split()
  print(datetime.now().strftime('%Y-%m-%d %H:%M:%S').rjust(int(cols)))
  print("TOOLS IN PYTHON")

def seleniumDefinition():
  options = Options()
  options.add_argument('--headless')
  return webdriver.Firefox(options=options)
  

def gmailSignIn(driver, email, password, numberEmail):
    
    driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent')
    driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()

    mailLogin = driver.find_element_by_xpath('//*[@id="identifierId"]')
    mailLogin.send_keys(email)

    sendMailLogin = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
    sendMailLogin.click()
    time.sleep(2)

    psw = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
    psw.send_keys(password)

    sendPsw = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
    sendPsw.click()
    time.sleep(2)

    driver.get('https://www.gmail.com/')
    for x in range(numberEmail):
      time.sleep(5)
      sendNewMail = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div')
      sendNewMail.click()
      time.sleep(5)
      mailG = driver.find_element_by_class_name("vO")
      mailG.send_keys(email)
      time.sleep(2)
      mailText = driver.find_element_by_class_name("editable")
      mailText.send_keys("bot message")
      time.sleep(1)
      btnSend = driver.find_element_by_class_name("aoO")
      btnSend.click()
      print("Email sent")
      time.sleep(5)
    driver.close()


def main():
  printMenu()
  driver = seleniumDefinition()
  gmailSignIn(driver,"yourmail@gmail.com","yourpassword",1)
      
  
  

if __name__ == "__main__":
    main()