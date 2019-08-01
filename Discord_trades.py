# - details https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

button = ''
popup = ''
file = ''
send_text = ''

# Defines the delay between two trade posting(in minutes)
trades_delay = 20

# Put in your email and password here
email = ''
password = ''

# Channels
bm = '#rl_bm_decals'
bodies = '#rl_bodies'
boosts = '#rl_boosts'
crates = '#rl_crates'
decals = '#rl_decals'
ge = '#rl_goal_explosions'
wheels = '#rl_wheels'
other = '#rl_other_items'
cross = '#rl_cross_game_trading'
cash = '#rl_cash_trades'
ltb = '#rl_looking_to_buy'

driver = webdriver.Chrome('E:\chromedriver_win32\chromedriver.exe')
actions = ActionChains(driver)


def wait(web_opening_time=3):
    time.sleep(web_opening_time)


# quit web driver for selenium
def web_driver_quit():
    driver.quit()


# actual login in Discord site
def discord_login():
    driver.get("https://discordapp.com/login")
    driver.maximize_window()
    email_field = driver.find_element_by_xpath("//input[@type='email']")
    email_field.send_keys(email)
    password_field = driver.find_element_by_xpath("//input[@type='password']")
    password_field.send_keys(password)
    submit_button = driver.find_element_by_xpath("//button[@type='submit']")
    submit_button.send_keys(Keys.RETURN)


# You may need to modify the folder name or path here
def open_file(f_name):
    global file
    file = open("discord_trades\\" + f_name)
    text = file.read()
    return text


def find_tc():
    print("\nHit 1 when page is ready")
    a = input()
    if a:
        driver.find_element_by_xpath('//a[@href="/channels/223259649967652887/381675339702599690"]').click()


def get_search_bar():
    global button
    global popup
    button = driver.find_element_by_class_name("btn-11C5_u").click()
    popup = driver.find_element_by_class_name("input-2VB9rf")


def post_ltb():
    if os.stat("discord_trades\\ltb.txt").st_size != 0:
        global ltb
        global send_text
        send_text = ''
        get_search_bar()
        popup.send_keys(ltb)
        popup.send_keys(Keys.RETURN)
        text = open_file("ltb.txt")
        text_bar = driver.find_element_by_xpath('//textarea[@placeholder="Message #rl_looking_to_buy"]')
        for ch in range(0, len(text)):
            if text[ch] == '\n':
                text_bar.send_keys(send_text)
                send_text = ''
                text_bar.send_keys(Keys.SHIFT, Keys.RETURN)
            else:
                send_text += text[ch]
        text_bar.send_keys(send_text)
        text_bar.send_keys(Keys.RETURN)
        print("Trades posted for rl_looking_to_buy.")

    else:
        print("No trades in rl_looking_to_buy.")


def post_bm():
    if os.stat("discord_trades\\bm.txt").st_size != 0:
        global bm
        global send_text
        send_text = ''
        get_search_bar()
        popup.send_keys(bm)
        popup.send_keys(Keys.RETURN)
        text = open_file("bm.txt")
        text_bar = driver.find_element_by_xpath('//textarea[@placeholder="Message #rl_bm_decals"]')
        for ch in range(0, len(text)):
            if text[ch] == '\n':
                text_bar.send_keys(send_text)
                send_text = ''
                text_bar.send_keys(Keys.SHIFT, Keys.RETURN)
            else:
                send_text += text[ch]
        text_bar.send_keys(send_text)
        text_bar.send_keys(Keys.RETURN)
        print("Trades posted for rl_bm_decals.")

    else:
        print("No trades in rl_bm_decals.")


def post_bodies():
    if os.stat("discord_trades\\bodies.txt").st_size != 0:
        global bodies
        global send_text
        send_text = ''
        get_search_bar()
        popup.send_keys(bodies)
        popup.send_keys(Keys.RETURN)
        text = open_file("bodies.txt")
        text_bar = driver.find_element_by_xpath('//textarea[@placeholder="Message #rl_bodies"]')
        for ch in range(0, len(text)):
            if text[ch] == '\n':
                text_bar.send_keys(send_text)
                text_bar.send_keys(Keys.SHIFT, Keys.RETURN)
                send_text = ''
            else:
                send_text += text[ch]
        text_bar.send_keys(send_text)
        text_bar.send_keys(Keys.RETURN)
        print("Trades posted for rl_bodies.")

    else:
        print("No trades in rl_bodies.")


def post_boosts():
    if os.stat("discord_trades\\boosts.txt").st_size != 0:
        global boosts
        global send_text
        send_text = ''
        get_search_bar()
        popup.send_keys(boosts)
        popup.send_keys(Keys.RETURN)
        text = open_file("boosts.txt")
        text_bar = driver.find_element_by_xpath('//textarea[@placeholder="Message #rl_boosts"]')
        for ch in range(0, len(text)):
            if text[ch] == '\n':
                text_bar.send_keys(send_text)
                send_text = ''
                text_bar.send_keys(Keys.SHIFT, Keys.RETURN)
            else:
                send_text += text[ch]
        text_bar.send_keys(send_text)
        text_bar.send_keys(Keys.RETURN)
        print("Trades posted for rl_boosts.")

    else:
        print("No trades in rl_boosts.")


def post_crates():
    if os.stat("discord_trades\\crates.txt").st_size != 0:
        global crates
        global send_text
        send_text = ''
        get_search_bar()
        popup.send_keys(crates)
        popup.send_keys(Keys.RETURN)
        text = open_file("crates.txt")
        text_bar = driver.find_element_by_xpath('//textarea[@placeholder="Message #rl_crates"]')
        for ch in range(0, len(text)):
            if text[ch] == '\n':
                text_bar.send_keys(send_text)
                send_text = ''
                text_bar.send_keys(Keys.SHIFT, Keys.RETURN)
            else:
                send_text += text[ch]
        text_bar.send_keys(send_text)
        text_bar.send_keys(Keys.RETURN)
        print("Trades posted for rl_crates.")

    else:
        print("No trades in rl_crates.")


def post_decals():
    if os.stat("discord_trades\\decals.txt").st_size != 0:
        global ltb
        global send_text
        send_text = ''
        get_search_bar()
        popup.send_keys(decals)
        popup.send_keys(Keys.RETURN)
        text = open_file("decals.txt")
        text_bar = driver.find_element_by_xpath('//textarea[@placeholder="Message #rl_decals"]')
        for ch in range(0, len(text)):
            if text[ch] == '\n':
                text_bar.send_keys(send_text)
                send_text = ''
                text_bar.send_keys(Keys.SHIFT, Keys.RETURN)
            else:
                send_text += text[ch]
        text_bar.send_keys(send_text)
        text_bar.send_keys(Keys.RETURN)
        print("Trades posted for rl_decals.")

    else:
        print("No trades in rl_decals.")


def post_ge():
    if os.stat("discord_trades\\ge.txt").st_size != 0:
        global ge
        global send_text
        send_text = ''
        get_search_bar()
        popup.send_keys(ge)
        popup.send_keys(Keys.RETURN)
        text = open_file("ge.txt")
        text_bar = driver.find_element_by_xpath('//textarea[@placeholder="Message #rl_goal_explosions"]')
        for ch in range(0, len(text)):
            if text[ch] == '\n':
                text_bar.send_keys(send_text)
                send_text = ''
                text_bar.send_keys(Keys.SHIFT, Keys.RETURN)
            else:
                send_text += text[ch]
        text_bar.send_keys(send_text)
        text_bar.send_keys(Keys.RETURN)
        print("Trades posted for rl_goal_explosions.")

    else:
        print("No trades in rl_goal_explosions.")


def post_wheels():
    if os.stat("discord_trades\\wheels.txt").st_size != 0:
        global wheels
        global send_text
        send_text = ''
        get_search_bar()
        popup.send_keys(wheels)
        popup.send_keys(Keys.RETURN)
        text = open_file("wheels.txt")
        text_bar = driver.find_element_by_xpath('//textarea[@placeholder="Message #rl_wheels"]')
        for ch in range(0, len(text)):
            if text[ch] == '\n':
                text_bar.send_keys(send_text)
                send_text = ''
                text_bar.send_keys(Keys.SHIFT, Keys.RETURN)
            else:
                send_text += text[ch]
        text_bar.send_keys(send_text)
        text_bar.send_keys(Keys.RETURN)
        print("Trades posted for rl_wheels.")

    else:
        print("No trades in rl_wheels.")


def post_other():
    if os.stat("discord_trades\\other.txt").st_size != 0:
        global other
        global send_text
        send_text = ''
        get_search_bar()
        popup.send_keys(other)
        popup.send_keys(Keys.RETURN)
        text = open_file("other.txt")
        text_bar = driver.find_element_by_xpath('//textarea[@placeholder="Message #rl_other_items"]')
        for ch in range(0, len(text)):
            if text[ch] == '\n':
                text_bar.send_keys(send_text)
                send_text = ''
                text_bar.send_keys(Keys.SHIFT, Keys.RETURN)
            else:
                send_text += text[ch]
        text_bar.send_keys(send_text)
        text_bar.send_keys(Keys.RETURN)
        print("Trades posted for rl_other_items.")

    else:
        print("No trades in rl_other_items.")


def post_cross():
    if os.stat("discord_trades\\cross.txt").st_size != 0:
        global cross
        global send_text
        send_text = ''
        get_search_bar()
        popup.send_keys(cross)
        popup.send_keys(Keys.RETURN)
        text = open_file("cross.txt")
        text_bar = driver.find_element_by_xpath('//textarea[@placeholder="Message #rl_cross_game_trading"]')
        for ch in range(0, len(text)):
            if text[ch] == '\n':
                text_bar.send_keys(send_text)
                send_text = ''
                text_bar.send_keys(Keys.SHIFT, Keys.RETURN)
            else:
                send_text += text[ch]
        text_bar.send_keys(send_text)
        text_bar.send_keys(Keys.RETURN)
        print("Trades posted for rl_cross_game_trading.")

    else:
        print("No trades in rl_cross_game_trading.")


def post_cash():
    if os.stat("discord_trades\\cash.txt").st_size != 0:
        global cross
        global send_text
        send_text = ''
        get_search_bar()
        popup.send_keys(cash)
        popup.send_keys(Keys.RETURN)
        text = open_file("cash.txt")
        text_bar = driver.find_element_by_xpath('//textarea[@placeholder="Message #rl_cash_trades"]')
        for ch in range(0, len(text)):
            if text[ch] == '\n':
                text_bar.send_keys(send_text)
                send_text = ''
                text_bar.send_keys(Keys.SHIFT, Keys.RETURN)
            else:
                send_text += text[ch]
        text_bar.send_keys(send_text)
        text_bar.send_keys(Keys.RETURN)
        print("Trades posted for rl_cash_trades.")

    else:
        print("No trades in rl_cash_trades.")


# Main Method
if __name__ == "__main__":
    running = True
    discord_login()
    find_tc()
    while running:
        post_bm()
        post_bodies()
        post_boosts()
        post_crates()
        post_decals()
        post_ge()
        post_wheels()
        post_other()
        post_ltb()
        post_cross()
        post_cash()

        print("Process completed successfully")

        print("\nRe-post trades? (0/1):")
        a = input()
        if not a:
            running = False
            print("\nTerminating the process...")
        #print("\n" + str(trades_delay) + " Minutes timer initiated!\n")
        #
        #i = trades_delay
        #while i != 0:
        #    print(str(i) + " Minutes left...")
        #    wait(60)
        #    i -= 1
        else:
            print("\n\nRe-posting trades...")

        wait()

    web_driver_quit()
