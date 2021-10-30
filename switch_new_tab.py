from selenium import webdriver
from time import sleep
from math import log, sin


def calc(el):
    return str(log(abs(12 * sin(int(el)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    browser.find_element_by_css_selector('button.trollface').click()        # нажимаем на плавающую кнопку

    new_window = browser.window_handles[1]                                  # узнаем имя новой вкладки в браузере
    browser.switch_to.window(new_window)                                    # переходим на новую вкладку в браузере

    x = int(browser.find_element_by_id('input_value').text)                 # получаем число X
    x = calc(x)                                                             # вычисляем по формуле

    input_res = browser.find_element_by_css_selector('input#answer')        # получаем поля для ввода
    input_res.send_keys(x)                                                  # вводим результат в поле для ввода

    button = browser.find_element_by_css_selector('button.btn').click()     # подтверждаем и отправляем овтет

finally:
    sleep(5)
    browser.quit()
