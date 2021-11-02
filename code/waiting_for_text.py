from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from math import log, sin


def calc(el):
    return str(log(abs(12 * sin(int(el)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    book = browser.find_element_by_id('book').click()

    x = int(browser.find_element_by_id('input_value').text)
    x = calc(x)

    button = browser.find_element_by_id('solve')
    browser.execute_script("arguments[0].scrollIntoView(true);", button)   # скроллим страницу

    input_res = browser.find_element_by_css_selector('input#answer').send_keys(x)
    button.click()

finally:
    sleep(5)
    browser.quit()
