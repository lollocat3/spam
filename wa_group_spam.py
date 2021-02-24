###-
###- Web whatsapp python selenium script
###-


### configurations
number_of_times = 3
### List of contact names that match the contacts in your phone

listNames = ['Vince']

### List of group names that are randomly chosen from
listGroups = ['gruppo1', 'gruppo2', 'gruppo3']


### Selenium automation
#- download http://chromedriver.storage.googleapis.com/index.html?path=2.21/
#- details https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
import random


## Selenium web drivers
driver = None

def wait(web_opening_time=3):
	time.sleep(web_opening_time)

## load web driver for selenium : chrome
def web_driver_load():
	global driver
	driver = webdriver.Chrome('/Users/lorenzo/Documents/chromedriver_87')
## quit web driver for selenium
def web_driver_quit():
	driver.quit()
	quit()

## actual login in hockey app site
def whatsapp_login():
	driver.get('https://web.whatsapp.com/');
	for i in range(0,number_of_times):
		time.sleep(1)
		try:
			createGroup()
		except NoSuchElementException:
			pass
		finally:
			print('Login Checked')

def createGroup():
	while True:
		time.sleep(2)
		print('Attempting to create group')
		chat = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]')
		chat.click()
		time.sleep(2)
		# click on create group
		#group = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[1]/span/div/span/div/div[2]/div[1]/div/div[1]/div[2]/div/div')
		#group.click()
		pyautogui.click(130, 360)
		time.sleep(2)
		# click on input
		for name in listNames: 
			pyautogui.write(name)
			time.sleep(2)
			pyautogui.press('enter')
		time.sleep(2)
		# click on arrow
		pyautogui.click(230, 820)
		time.sleep(1)
		number = random.randint(0,2)
		pyautogui.write(listGroups[number])
		time.sleep(0.5)
		pyautogui.press('enter')
		time.sleep(3)
		pyautogui.click(1185, 200)
		time.sleep(1)
		for i in range(5):
			pyautogui.press('down')
		time.sleep(0.5)
		pyautogui.press('enter')
		time.sleep(1)
		pyautogui.click(760, 555)
		time.sleep(0.5)
		pyautogui.click(1185, 200)
		time.sleep(1)
		for i in range(4):
			pyautogui.press('down')
		time.sleep(0.5)
		pyautogui.press('enter')
		time.sleep(1)
		pyautogui.click(760, 555)
		print('Group Created')

	exit(0)


### Main Method
if __name__ == "__main__":
	web_driver_load()
	whatsapp_login()
	for i in range(number_of_times):
		sendMessage(message)
		wait()
	print("Process complete successfully")
	web_driver_quit()