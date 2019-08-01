from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("E:\chromedriver_win32\chromedriver.exe")
actions = ActionChains(driver)
wait = WebDriverWait(driver, 10)

price = 2
crate_amount = 5
First_time = True

# Put in your user name and password below
user_name = ''
password = ''
delay = 10
days_for_delivery = 1 # Within how many days do you gaurantee to deliver the item

# Below goes the description about your store
description = "# Welcome to Fuffy's RL Shop\n# Fast delivery\n# Leave your steam profile link after placing your order for faster delivery!\n# Message me on steam if you want modification in the quantity of an item!\n# Steam: "


def sleep(i):
    print("sleep time: " + str(i) + " second(s)..")
    for i in range(1, i):
        print(str(i))
        time.sleep(1)
        i += 1

def load_gameflip():
    try:
        driver.get('https://gameflip.com')
        print("Gameflip page loaded")
        sleep(10)

    except:
        print("Can't load gameflip.com, please check your internet connection.")
        print("Terminating process")
        exit(1)


def login():
    driver.maximize_window()
    #try:
    driver.find_element_by_xpath('//*[contains(text(), "Sign In")]').click()

    user_name_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="username"]')))
    actions.move_to_element(user_name_field).click().perform()
    user_name_field.send_keys(user_name)
    print("username entered..")

    password_field = driver.find_element_by_xpath('//input[@name="password"]')
    password_field.click()
    password_field.send_keys(password)
    print("password entered..")

    driver.find_element_by_css_selector(".btn.btn-primary.signin-button").click()# sign-in button

    try:
        s_code_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="challenge_code"]')))
        s_code_field.click()

    except StaleElementReferenceException as e:
        raise e

    print("Please enter your security code:")

    s_code = input()
    s_code_field.send_keys(s_code)
    print("security code entered..")

    driver.find_element_by_xpath('//*[contains(text(), "Continue Signing In")]').click()#submit button
    print("Submitting the login information..")
    print("Login successful..")


def post_listing():
    global days_for_delivery
    global crate_amount
    global price

    if First_time:
        print("What is the initial amount of crates?:")
        crate_amount = int(input())
        price = (int(crate_amount/2))*100
        sleep(5)

    driver.find_element_by_class_name("pointer").click() #sell button
    print("Posting the listings..")
    driver.find_element_by_xpath('//img[@src="https://gameflip.com/img/app/icon_category_orange_skins.png"]').click() #ingame_item
    driver.find_element_by_xpath('//img[@src="https://gameflip.com/img/app/digital_platform_steam_rocketleague.png"]').click() #rl_steam

    if First_time:
        sleep(15)

    else:
        sleep(3)

    driver.find_element_by_xpath('//img[@src="/img/items/rocket-league/player_choice_crate.png"]').click() #pcc_crate

    amount_button = driver.find_element_by_css_selector(".form-control.text-right")
    amount_button.click()
    amount_button.send_keys(Keys.DELETE)
    amount_button.send_keys(crate_amount)

    driver.find_element_by_css_selector(".col-xs-5.btn.btn-primary").click()
    description_field = driver.find_element_by_xpath('//textarea[@class="form-control"]')
    description_field.click()

    sleep(15)
    description_field.send_keys(Keys.RETURN)
    description_field.send_keys(description)
    print("Description posted")

    sleep(2)

    delivery_days = driver.find_elements_by_xpath('//input[@name="delivery-transfer"]')
    delivery_days[days_for_delivery-1].click()

    price_field = driver.find_element_by_xpath('//input[@placeholder="Your Price"]')
    price_field.click()
    price_field.send_keys(str(price))

    sleep(10)
    submit = driver.find_element_by_xpath('//button[@type="submit"]') #submit listing
    submit.click()
    #driver.find_element_by_xpath('//*[contains(text(), "List Item")]').click()

    #try:
    #    accept = WebDriverWait(driver, 10).until(
    #        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "List Item")]')))
    #    actions.send_keys(Keys.TAB)
    #    accept.click()

    #except StaleElementReferenceException as e:
    #    raise e

    #accept = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "List Item")]')))
    #actions.move_to_element(accept).click().perform()

    actions.send_keys(Keys.TAB)
    accept = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "List Item")]')))
    accept.click()
    print("Listing posted successfully... (crates- " + str(crate_amount) + ", price= " + str(int(price/100)) + "$)\n")


if __name__ == '__main__':
    Running = True
    #try:
    load_gameflip()
    login()

    while crate_amount <= 120:
        post_listing()
        sleep(10)
        crate_amount = int(crate_amount) + 5
        price = (int(crate_amount / 2)) * 100
        First_time = False



