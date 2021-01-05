from datetime import datetime
import time
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import progressbar


def printMenu():
  rows, cols = os.popen('stty size', 'r').read().split()
  print(datetime.now().strftime('%Y-%m-%d %H:%M:%S').rjust(int(cols)))
  print("TOOLS IN PYTHON")
  senter = input("Enter senter mail: ") 
  password = input("Enter senter password: ") 
  recipient = input("Enter recipient mail: ") 
  message = input("Enter the text to sent: ")
  numberEmail = input("Enter the number email to sent: ")
  return senter,recipient,password,message,numberEmail
  
def seleniumDefinition():
  options = Options()
  options.add_argument('--headless')
  return webdriver.Firefox(options=options)
  
def gmailSignIn(driver, email, password, recipient, message, numberEmail):
  with progressbar.ProgressBar(max_value=100) as bar:
    for i in range(1):
      
      driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent')
      driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()

      bar.update(14)

      mailLogin = driver.find_element_by_xpath('//*[@id="identifierId"]')
      mailLogin.send_keys(email)

      bar.update(21)

      sendMailLogin = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
      sendMailLogin.click()
      time.sleep(3)

      bar.update(37)

      psw = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
      psw.send_keys(password)

      bar.update(45)

      sendPsw = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
      sendPsw.click()

      bar.update(53)
      time.sleep(3)

      driver.get('https://www.gmail.com/')
      for x in range(int(numberEmail)):
        time.sleep(5)
        bar.update(65)
        sendNewMail = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div')
        sendNewMail.click()
        time.sleep(7)
        bar.update(73)
        mailG = driver.find_element_by_class_name("vO")
        mailG.send_keys(recipient)
        bar.update(89)
        time.sleep(5)
        mailText = driver.find_element_by_class_name("editable")
        mailText.send_keys(message)
        time.sleep(2)
        bar.update(95)
        btnSend = driver.find_element_by_class_name("aoO")
        btnSend.click()
        bar.update(100)
        print("email {} sent".format(x+1))
  driver.close()

def main():
  senter, recipient, password, message, numberEmail = printMenu()
  os.system("clear")
  print(' senter: {}\n recipient: {}\n message: {}\n number Email {}\n\n'.format(senter,recipient,message,numberEmail))
  driver = seleniumDefinition()
  print('Running...')
  gmailSignIn(driver, senter, password, recipient,message, numberEmail)
      

if __name__ == "__main__":
    main()