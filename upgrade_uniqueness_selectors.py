from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import unittest


def test_link(link):
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(1)

    # Заполнение обязательных полей и нажатие кнопки для отправления
    browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys("Иван")
    browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys("Иванов")
    browser.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys("ivan@yandex.ru")

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    # Возвращает сообщение об успешной регистрации, если она произошла
    return browser.find_element(By.TAG_NAME, 'h1').text


class TestReg(unittest.TestCase):

    def test_reg1(self):
        self.assertEqual(test_link('http://suninjuly.github.io/registration1.html'),
                         "Congratulations! You have successfully registered!", "registration is failed")

    def test_reg2(self):
        self.assertEqual(test_link('http://suninjuly.github.io/registration2.html'),
                         "Congratulations! You have successfully registered!", "registration is failed")


if __name__ == '__main__':
    unittest.main()
