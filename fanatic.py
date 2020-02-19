from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os, time
import datetime
import schedule

print('stack_overflow_attendance docker status up: ', datetime.datetime.now())

xpath = {
    'login_button': '/html/body/header/div/ol[2]/li[2]/a[1]',
    'username': '/html/body/div[4]/div[2]/div/div[3]/form/div[1]/div/input',
    'password': '/html/body/div[4]/div[2]/div/div[3]/form/div[2]/div[1]/input',
    'inner_login_button': '/html/body/div[4]/div[2]/div/div[3]/form/div[3]/button',
    'profile_page': '/html/body/header/div/ol[2]/li[2]/a/div[1]/img',
    'fanatic_points': '//*[@id="top-cards"]/aside[2]/div/div/div[2]/div[2]/div/div[1]/span'
}


stackoverflow_username = os.environ['STACKOVERFLOW_EMAIL']
stackoverflow_password = os.environ['STACKOVERFLOW_PASSWORD']
browser = ""


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')


def waitForElement(browser, path):
    try:
        WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.XPATH, path)))
    except TimeoutException:
        print('stack_overflow_attendance timeout_exception: ', browser.current_url)
    except NoSuchElementException:
        print('stack_overflow_attendance failed_to_find_element: ', path)


def stack_overflow_attendance():

    print('stack_overflow_attendance script start:', datetime.datetime.now())

    try:

        browser = webdriver.Chrome(chrome_options=chrome_options)

        browser.get('https://stackoverflow.com/')

        time.sleep(5)

        waitForElement(browser, xpath['login_button'])

        home_page_login = browser.find_element_by_xpath(xpath['login_button'])
        home_page_login.click()

        time.sleep(4)
        waitForElement(browser, xpath['username'])
        username = browser.find_element_by_xpath(xpath['username'])
        username.clear()
        username.send_keys(stackoverflow_username)

        time.sleep(2)

        password = browser.find_element_by_xpath(xpath['password'])
        password.clear()
        password.send_keys(stackoverflow_password)

        time.sleep(3)
        login = browser.find_element_by_xpath(xpath['inner_login_button'])
        login.click()

        time.sleep(3)
        waitForElement(browser, xpath['profile_page'])
        profile_page = browser.find_element_by_xpath(xpath['profile_page'])
        profile_page.click()

        get_fanatic = browser.find_element_by_xpath(xpath['fanatic_points'])
        fanatic = get_fanatic.text
        print('stack_overflow_attendance script count:', fanatic)
        print('stack_overflow_attendance script end  :', datetime.datetime.now())

        browser.close()

    except Exception as error:
        print("stack_overflow_attendance exception:", error)


schedule.every().day.at("12:00").do(stack_overflow_attendance)


while 1:
    schedule.run_pending()
    time.sleep(1)
