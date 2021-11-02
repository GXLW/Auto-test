from selenium import webdriver
from time import sleep
from math import log, sin


def calc(el):
    return str(log(abs(12 * sin(int(el)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    submit = browser.find_element_by_css_selector('button.btn').click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = int(browser.find_element_by_id('input_value').text)
    x = calc(x)

    input_res = browser.find_element_by_css_selector('input#answer')
    input_res.send_keys(x)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    sleep(5)
    browser.quit()
