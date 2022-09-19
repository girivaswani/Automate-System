from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import datetime
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()
# browser.get('https://store.mi.com/in/item/3210700007')
browser.get('https://store.mi.com/in/item/3194500001')
time.sleep(1)

signin=browser.find_elements(By.CLASS_NAME,'entry')
for ele in signin:
    if ele.text=="SIGN IN":
        ele.click()
        time.sleep(2)
        inputlist=browser.find_elements(By.CLASS_NAME,"mi-input__input")
        for index in range(len(inputlist)):
            if index==0:
                inputlist[index].send_keys("Your username")
            else:
                inputlist[index].send_keys("Your Password")
        time.sleep(1)
        button=browser.find_element(By.CLASS_NAME,'mi-button--fullwidth')
        button.click()

        time.sleep(1)
        break
current=datetime.datetime.now().strftime("%I:%M%p")
req="04:00PM"
i=1
while current<req:
    current = datetime.datetime.now().strftime("%I:%M%p")
    print(i)
    i+=1
    time.sleep(0.5)
    # pass
else:
    link=browser.find_element(By.CLASS_NAME,'J_addCart')
    link.click()
    time.sleep(1)
    link1=browser.find_element(By.ID,'J_miniCartIcon')
    link1.click()
    time.sleep(1)
    checkout=browser.find_element(By.CLASS_NAME,'cart__footer-checkout')
    checkout.click()
    time.sleep(1)
    placeOrder=browser.find_element(By.CLASS_NAME,'J_checkoutOrder')
    placeOrder.click()
    time.sleep(100)
    browser.close()