from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def printMenu():
  print("TOOLS IN PYTHON")
  rows, cols = os.popen('stty size', 'r').read().split()
  print(datetime.now().strftime('%Y-%m-%d %H:%M:%S').rjust(int(cols)))

def seleniumDefinition():
  options = Options()
  options.add_argument('--headless')
  options.add_argument('--no-sandbox')
  return webdriver.Chrome('/usr/local/bin/chromedriver', options=options) 


def main():
  printMenu()
  driver = seleniumDefinition()
  driver.get("https://www.google.com/")
  #driver.get_screenshot_as_file("capture.png")
  print ("Chrome Initialized")
  driver.quit()

if __name__ == "__main__":
    main()