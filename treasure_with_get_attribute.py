from selenium import webdriver
from time import sleep
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'

browser = webdriver.Chrome()
browser.get(link)


try:
    check = browser.find_element_by_id('robotCheckbox').click()
    radio = browser.find_element_by_id('robotsRule').click()

    x_element = browser.find_element_by_css_selector('#treasure')
    value = x_element.get_attribute('valuex')

    x = value
    y = calc(x)

    res = browser.find_element_by_id('answer')
    res.send_keys(y)

    button = browser.find_element_by_class_name('btn-default')
    button.click()

finally:
    sleep(10)
    browser.quit()
