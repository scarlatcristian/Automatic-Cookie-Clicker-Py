from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

option = Options()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=option)

driver.get("https://orteil.dashnet.org/cookieclicker/")

consent_btn = driver.find_element(
    "xpath", "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p")
consent_btn.click()

pick_language = driver.find_element("id", "langSelect-EN")
pick_language.click()

cookie = driver.find_element("id", "bigCookie")

while True:
    cookie.click()
