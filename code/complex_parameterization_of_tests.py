import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import time
from math import log


@pytest.fixture(scope='function')
def browser():
    print('\nstart')
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)

    yield browser

    print('\nquit')
    browser.quit()
    print(result)


result = ''                                                                        # переменная для сбора ответа


class TestDetectedAliens:

    @pytest.mark.parametrize('number', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
    def test_login_link(self, browser, number):
        global result
        answer = str(log(int(time())))

        link = f'https://stepik.org/lesson/{number}/step/1'
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, 'textarea').send_keys(answer)        # вводим результат
        browser.find_element(By.CSS_SELECTOR, 'button.submit-submission').click()  # нажимаем кнопку отпраки
        feedback = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text   # получаем фидбек

        try:
            assert 'Correct!' == feedback                                          # проверяем фидбек на корректность

        except AssertionError:
            result += feedback                                                     # сборка ответа
