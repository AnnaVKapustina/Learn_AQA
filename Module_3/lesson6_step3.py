import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(20) #Ждем прогрузки
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', ['https://stepik.org/lesson/236895/step/1',
                                 'https://stepik.org/lesson/236896/step/1',
                                 'https://stepik.org/lesson/236897/step/1',
                                 'https://stepik.org/lesson/236898/step/1',
                                 'https://stepik.org/lesson/236899/step/1',
                                 'https://stepik.org/lesson/236903/step/1',
                                 'https://stepik.org/lesson/236904/step/1',
                                 'https://stepik.org/lesson/236905/step/1'])
def test_correct_feedback(browser, url):
    link = f"{url}"
    browser.get(link)
    input1 = browser.find_element(By.CLASS_NAME, 'textarea')
    input1.send_keys(str(math.log(int(time.time()))))
    button = browser.find_element(By.CLASS_NAME, 'submit-submission')
    button.click()
    feedback = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    text = feedback.text
    assert 'Correct!' == text, f'Text is not "Correct!", Text is "{text}"'

