from selenium import webdriver as wd
from time import sleep
import json
import random
import string
import json
import random
from webdriver_manager.chrome import ChromeDriverManager
driver = wd.Chrome(ChromeDriverManager().install())

#url='https://www.change.org/p/gitam-administration-being-inconsiderate-with-the-conducting-of-online-semester-examinations-at-gitam'

'''
##for hosting in heroku
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
'''

print(r"""\
   ___    _   _   _                ____        _
  /   \  | | | | | |_    ___      | __ )  ___ | |_
 |  _  | | | | | | __|  / _ \     |  _ \ / _ \| __|
 | | | | | |_| | | |   | (_) |    | |_) | (_) | |_
 |_| |_| |_____| \__|   \___/     |____/ \___/ \__|


 Author		:Srijan
 version	: 1.9.3

""")



def loop(count):
	driver.get(url)
	fname = json.loads(open('fnames.json').read())
	lname = json.loads(open('lnames.json').read())
	email_services=['@yahoo.com','@gmail.com','@hotmail.com','@icloud.com','@msn.com','@outlook.com','@laposte.net']

	randfname = random.randrange(1000)
	randlname = random.randrange(1000)

	nam=fname[randfname]
	lam=lname[randlname]
	lame=lam[0:3]
	name_extra=''.join(random.choice(string.digits))
	email=nam.lower()+lame.lower()+name_extra+random.choice(email_services)

	#driver.delete_all_cookies()

	fnamebox = driver.find_element_by_id("firstName")
	lnamebox = driver.find_element_by_id("lastName")
	emailbox = driver.find_element_by_id("email")
	publiccheck = driver.find_element_by_name("public")
	sign_btn=driver.find_element_by_xpath("""//*[@id="page"]/div[1]/div[3]/div[2]/div/div/div/div[2]/div[2]/form/button""")
	print(fname[randfname], lname[randlname], email,"num=",count)
	fnamebox.send_keys(fname[randfname])
	lnamebox.send_keys(lname[randlname])
	emailbox.send_keys(email)
	sleep(0.5)
	publiccheck.click()
	sign_btn.click()
	driver.delete_all_cookies()
	driver.get(url)

def main():
	url=input("Paste your petition URL here	:",end="\n")
	driver.get(url)
	num=0
	for _ in range(1,1000):
		try:
			loop(num)
			num += 1
		except:
			driver.delete_all_cookies()
			driver.get(url)
			print("Error filling form. Refreshing...")
		
		

main()
