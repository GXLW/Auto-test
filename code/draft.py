import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time, sleep
from math import log


@pytest.fixture(scope='function')
def browser():
    print('\nstart browser')
    browser = webdriver.Chrome()

    yield browser

    print('\nquit browser')
    sleep(5)
    browser.quit()


class TestDetectedAliens:

    @pytest.mark.xfail
    @pytest.mark.parametrize('number',
                             ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905',]
                             )
    def test_login_link(self, browser, number):
        answer = str(log(int(time())))

        link = f'https://stepik.org/lesson/{number}/step/1'
        browser.get(link)
        browser.implicitly_wait(50)

        browser.find_element(By.CSS_SELECTOR, 'textarea').send_keys(answer)        # вводим результат
        browser.find_element(By.CSS_SELECTOR, 'button.submit-submission').click()   # нажимаем кнопку отпраки
