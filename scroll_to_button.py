from selenium import webdriver
from time import sleep
import math


def calc(el):
    return str(math.log(abs(12 * math.sin(int(el)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://SunInJuly.github.io/execute_script.html')

    x = int(browser.find_element_by_id('input_value').text)                # вычисляем формулу
    x = calc(x)
    res = browser.find_element_by_id('answer').send_keys(x)

    check = browser.find_element_by_id('robotCheckbox').click()            # нажимаем checkbox "i'm the robot"

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("arguments[0].scrollIntoView(true);", button)   # листаем страницу к перекрытым элементам

    radio = browser.find_element_by_id('robotsRule').click()               # нажимаем radiobutton "Robots rule"

    button.click()                                                         # нажимаем кнопку "Submit"

finally:
    sleep(5)
    browser.quit()
