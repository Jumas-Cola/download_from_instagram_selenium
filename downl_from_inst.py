
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urllib.request import urlretrieve
from selenium import webdriver
import instagram
import time
import sys
import os



def init_driver(path = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'):
	gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
	#...path to firefox.exe
	binary = FirefoxBinary(path)
	driver = webdriver.Firefox(firefox_binary=binary, executable_path=gecko+'.exe')
	driver.wait = WebDriverWait(driver, 5)
	return driver

def inst_authorization(login, password, driver):
	driver.get('https://www.instagram.com/accounts/login/')
	time.sleep(5)
	try:
		log = driver.wait.until(EC.presence_of_element_located((By.NAME, "username")))
		log.send_keys(login)
		time.sleep(1)
		pas = driver.wait.until(EC.element_to_be_clickable((By.NAME, "password")))
		pas.send_keys(password)
		time.sleep(1)
		button = driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button._5f5mN.jIbKX.KUBKM")))
		time.sleep(3)
		button.click()
		time.sleep(5)
	except TimeoutException:
		print("Box or Button not found in instagram.com")



if len(sys.argv) < 2:
	print("\n--------------------------------------------------")
	print("\nUsage: py_inst_img.py <user> <count_imgs[>12]> <login> <password>")
	sys.exit(1)

try:
	user = sys.argv[1]
except:
	print("\n--------------------------------------------------")
	print("\nError: cant find user")
	sys.exit(1)

try:
	count_imgs = int(sys.argv[2])
except:
	print("\n--------------------------------------------------")
	print("\nCant find count. Default count_imgs: 9999")
	count_imgs = 9999

try:
	login = sys.argv[3]
	password = sys.argv[4]
except:
	print("\n--------------------------------------------------")
	print("\nCant find login or pass. Try without authorization.")

try:
	agent=instagram.AgentAccount(login, password)
except:
	agent=instagram.Agent()
agent.update()
account=instagram.Account(user)
agent.update(account)
media=agent.getMedia(account, count=count_imgs)

browser = init_driver()

try:
	inst_authorization(login, password, browser)
except:
	print("\n--------------------------------------------------")
	print('\nCant authorize.')

try:
	os.makedirs('photos_inst')
except:
	print("\n--------------------------------------------------")
	print('\nDir /photos_inst already exist')

for item in media[0]:
	item = str(item)
	try:
		browser.get('https://www.instagram.com/p/'+item+'/?taken-by='+user) # Загружаем страницу
		time.sleep(5)
		place_block = browser.find_element_by_class_name("FFVAD")
		place_img = place_block.get_attribute('src')
		urlretrieve(place_img, 'photos_inst/'+item+'.png')
	except:
		try:
			browser.get('https://www.instagram.com/p/'+item+'/?taken-by='+user) # Загружаем страницу
			time.sleep(5)
			place_block = browser.find_element_by_class_name("tWeCl")
			place_video = place_block.get_attribute('src')
			urlretrieve(place_video, 'photos_inst/'+item+'.mp4')
		except:
			print('\nCant download this file: '+item)
browser.quit()
time.sleep(5)
print("\n--------------------------------------------------")
print("\nFinished!")