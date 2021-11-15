from selenium.webdriver.common.by import By
from time import sleep


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    sleep(30)
    button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")

    assert button != [], 'Элемент не найден'
