import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.set_window_size(1024, 768)

from getpass import getpass

# driver.get(url)
# driver.find_element_by_xpath(xpath)

url = "https://order.papajohns.com/mobile/index.wap?site=WAP&utm_source=TABLET&utm_medium=orderpages&utm_campaign=experiencechange"
driver.get(url)

sign_in_xpath = '//*[@id="content"]/ol/li[4]/a'
sign_in = driver.find_element_by_xpath(sign_in_xpath)
sign_in.click()

email_xpath = '//*[@id="ip-username"]'
el = driver.find_element_by_xpath(email_xpath)
el.click()
el.send_keys("dbieber@princeton.edu")

password = getpass()

pass_xpath = '//*[@id="ip-password"]'
el2 = driver.find_element_by_xpath(pass_xpath)
el2.click()
el2.send_keys(password)

sign_xpath = '//*[@id="signInForm"]/div/button'
sign_in = driver.find_element_by_xpath(sign_xpath)
sign_in.click()

offer_xpath = '//*[@id="foot"]/ul/li[2]/a'
offer_btn = driver.find_element_by_xpath(offer_xpath)
offer_btn.click()

def click_xpath(xpath):
    btn = driver.find_element_by_xpath(xpath)
    btn.click()

click_xpath('//*[@id="content"]/ol/li[1]/a')  # click any large pizza

pizzas = driver.find_elements_by_xpath('//*[@id="orderBuilder"]/fieldset/label')

pizza_ids = {}
for pizza in pizzas:
    pizza_name = pizza.text
    pizza_id = pizza.get_attribute('for')

    pizza_ids[pizza_name] = pizza_id

# We now have all the pizza ids...

def order_pizza(name):
    driver.get('http://order.papajohns.com/mobile/build/deal/6803.wap')
    pizza_id = pizza_ids[name]
    click_xpath('//*[@id="%s"]' % pizza_id)
    click_xpath('//*[@id="orderBuilder"]/div/button')
    click_xpath('//*[@id="orderBuilder"]/div/button')

order_pizza('Lg Orig Spicy Italian')

raw_input()


print el

raw_input()

driver.close()
