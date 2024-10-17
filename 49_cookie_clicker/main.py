from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

URL = "https://orteil.dashnet.org/experiments/cookie/"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(URL)

cookie = driver.find_element(By.ID, "cookie")

timeout = 60*5   # [seconds]

timeout_start = time.time()
t_current = time.time()

while time.time() < timeout_start + timeout:
    #time.sleep(0.001)
    cookie.click()
    if time.time() >= t_current + 1:
        t_current = time.time()
        if int(t_current % 5) == 0:
            money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
            price_cursor = int(driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').text.split(" - ")[1].replace(",", ""))
            price_grandma = int(driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b').text.split(" - ")[1].replace(",", ""))
            price_factory = int(driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b').text.split(" - ")[1].replace(",", ""))
            price_mine = int(driver.find_element(By.XPATH, '//*[@id="buyMine"]/b').text.split(" - ")[1].replace(",", ""))
            price_shipment = int(driver.find_element(By.XPATH, '//*[@id="buyShipment"]/b').text.split(" - ")[1].replace(",", ""))
            price_alchemy = int(driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b').text.split(" - ")[1].replace(",", ""))
            price_portal = int(driver.find_element(By.XPATH, '//*[@id="buyPortal"]/b').text.split(" - ")[1].replace(",", ""))
            price_timemachine = int(driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b').text.split(" - ")[1].replace(",", ""))
            if money >= price_timemachine:
                driver.find_element(By.ID, "buyTime machine").click()
            elif money >= price_portal:
                driver.find_element(By.ID, "buyPortal").click()
            elif money >= price_alchemy:
                driver.find_element(By.ID, "buyAlchemy lab").click()
            elif money >= price_shipment:
                driver.find_element(By.ID, "buyShipment").click()
            elif money >= price_mine:
                driver.find_element(By.ID, "buyMine").click()
            elif money >= price_factory:
                driver.find_element(By.ID, "buyFactory").click()
            elif money >= price_grandma:
                driver.find_element(By.ID, "buyGrandma").click()
            elif money >= price_cursor:
                driver.find_element(By.ID, "buyCursor").click()
                
cps = driver.find_element(By.ID, "cps")
print(cps.text)
driver.quit()