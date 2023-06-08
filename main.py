from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime
import sys
import time

# 设置 Chrome WebDriver 的路径
webdriver_service = Service('path/to/chromedriver')

times = "2023-06-08 20:00:00"

# 创建 Chrome WebDriver 实例
driver = webdriver.Chrome(service=webdriver_service)
# 打开网页
driver.get('https://www.taobao.com')
driver.find_element(By.CLASS_NAME, "btn-login").click()

print(f"扫码登录")
time.sleep(10)

driver.get("https://cart.taobao.com/cart.html")

while 1==1:
    if driver.find_element(By.CLASS_NAME, "J_CheckBoxShop"):
        driver.find_element(By.CLASS_NAME, "J_CheckBoxShop").click()
        break

while 1==1:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    print(now)

    if now > times:
        while 1==1:
            try:
                if driver.find_element(By.CLASS_NAME, "J_CheckBoxShop"):
                    print("here")
                    driver.find_element(By.CLASS_NAME, "J_CheckBoxShop").click()
                    print("已经抢到商品啦")
                    break
            except:
                pass
            