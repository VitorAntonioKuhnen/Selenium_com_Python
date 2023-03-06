
from selenium import webdriver

import webbrowser

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pickle

url = 'https://web.whatsapp.com/'

# driver = webdriver.Firefox(executable_path='C:\\Users\\Vítor\\Documents\\Selenium\\Driver\\geckodriver.exe')

# driver = webdriver.Chrome(executable_path='C:\\ChromeDriver\\chromedriver.exe') 

# driver.get("https://web.whatsapp.com/")



'''
Processo para salvar conexão com o WhatsApp, após efetuar a conexão poderá ignora-lo
'''
firefox = webbrowser.Mozilla(r"C:\\Program Files\\Mozilla Firefox\\firefox.exe")

firefox.open(url)

# input("Se já escaneou Enter")

time.sleep(1)

myprofile = webdriver.FirefoxProfile(r'C:\\Users\\Vítor\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\gaexxmc1.default-release')
driver = webdriver.Firefox(firefox_profile=myprofile)
driver.get(url)
driver.refresh

elemente = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div/div[6]/div/div/div/div[2]/div[2]/div[2]')
print(elemente.send_keys(Keys.RETURN))


# elemente = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
# elemente.send_keys('Vitor')
# elemente.send_keys(Keys.ENTER)

# with open("cookies.pkl", "wb") as file:
#     pickle.dump(driver.get_cookies(), file)


# with open("cookies.pkl", "rb") as file:
#     cookies = pickle.load(file)

# # Adcicione os ookies ao WebDriver
# for cookie in cookies:
#     driver.add_cookie(cookie)

# # Atualize a página para carregar os cookies
# driver.refresh()



# driver.get("https://www.google.com.br/")
# time.sleep(30)
# driver.quit
# elemente = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
# elemente.send_keys('Vitor')
# elemente.send_keys(Keys.ENTER)

