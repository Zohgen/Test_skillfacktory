from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
import time,os
from selenium import webdriver

@pytest.fixture(autouse=True)
def testing():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--incognito")
    pytest.driver= webdriver.Chrome(options=chrome_options)
    pytest.driver.get('https://b2c.passport.rt.ru')

    yield

    pytest.driver.quit()

#передаем пустое значение в поле лицевого счета

def test_auth_without_ls():

    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()


    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 'username').send_keys('')



    pytest.driver.implicitly_wait(3)
    pytest.driver.find_element(By.ID, 'password').send_keys('passwrd')


    pytest.driver.implicitly_wait(3)
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest.driver.implicitly_wait(3)


    assert pytest.driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[1]/div[2]/span').text == ('Введите номер вашего лицевого счета')


#передаем в логин ровно 12 чисел

def test_auth_ls_rovno():

    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 'username').send_keys("123456789012")

    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.ID, 'password').send_keys("passwrd")
    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest.driver.implicitly_wait(5)

    assert pytest.driver.find_element(By.ID, 'form-error-message').text == ("Неверный логин или пароль") or ("Неверно введен текст с картинки")

#так как в поле лицевого счета нельзя вписать ничего кроме чисел то проверки будут на кол-во введенных чисел

@pytest.mark.parametrize('ls, passwrd',[
    ("1252", "達羅瓦達羅瓦達羅瓦"),  # логин меньше 12 символов
    ("123456789", "達羅瓦達羅瓦達羅瓦"),  # логин меньше 12 символов
    ("6669111", "達羅瓦達羅瓦達羅瓦"),  # логин меньше 12 символов
])
def test_auth_by_login_fail(ls,passwrd):

    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.ID, 'username').send_keys(ls)

    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.ID, 'password').send_keys(passwrd)
    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest.driver.implicitly_wait(5)

    assert pytest.driver.find_element(By.XPATH,'/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[1]/div[2]/span').text==('Проверьте, пожалуйста, номер лицевого счета')

