from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep


def calc(el1, el2):
    return str(el1 + el2)


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')

    x = browser.find_element_by_id('num1').text
    y = browser.find_element_by_id('num2').text
    res = calc(int(x), int(y))

    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(res)

    button = browser.find_element_by_css_selector('button.btn-default').click()

finally:
    sleep(5)
    browser.quit()
