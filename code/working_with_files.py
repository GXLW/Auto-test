from selenium import webdriver
from time import sleep
import os


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    # код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector('[placeholder="Enter first name"]').send_keys('Ivan')
    last_name = browser.find_element_by_css_selector('[placeholder="Enter last name"]').send_keys('Petrov')
    mail = browser.find_element_by_css_selector('[placeholder="Enter email"]').send_keys('ivan.petrov@ynadex.ru')
    file = browser.find_element_by_id('file')

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname('file.txt'))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file.txt')
    # отправляем файл
    file.send_keys(file_path)

    # отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    sleep(5)
    browser.quit()
