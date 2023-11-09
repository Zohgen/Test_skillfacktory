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



def test_auth_without_login():

    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.ID, 'username').send_keys('')
    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.ID, 'password').send_keys("passwrd")
    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest.driver.implicitly_wait(5)

    assert pytest.driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[1]/div[2]/span').text == ('Введите логин, указанный при регистрации')





@pytest.mark.parametrize('login, passwrd',[
    ("1254789632", "123"), #пароль меньше 8
    ("1254789632", "123456789012345678901"), #пароль больше 20
    ("1254789632", "達羅瓦達羅瓦達羅瓦"), #пароль на другом языке
    ("達羅瓦達羅瓦達羅瓦", "A1P,i525r2"), #логин на другом языке
    (";:?*%:?", "A1P,ipYoArr2"), #логин символы
    ("Zhorik228", "A1P,i525r2"), #логин на латинице с числами
    ("Хрумыч007", "A1P,i525r2"), #логин на кириллице с числами
])





def test_auth_by_login_fail(login,passwrd):
    #element = WebDriverWait(pytest.driver, 3).until(EC.presence_of_element_located((By.ID, "email")))
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.implicitly_wait(5)
   # pytest.driver.find_element(By.ID, 'username').send_keys('test_rostteelekom@mail.ru')
    pytest.driver.find_element(By.ID, 'username').send_keys(login)
    pytest.driver.implicitly_wait(5)
    #pytest.driver.find_element(By.ID, 'password').send_keys('A1P,ipYoArr2')
    pytest.driver.find_element(By.ID, 'password').send_keys(passwrd)
    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest.driver.implicitly_wait(5)
   # assert pytest.driver.find_element(By.TAG_NAME, 'h3').text == "Учетные данные"
    #assert pytest.driver.find_element(By.ID, 'form-error-message').text == ("Неверный логин или пароль" or "Неверно введен текст с картинки")
    assert pytest.driver.find_element(By.ID, 'form-error-message').text == ("Неверный логин или пароль") or ("Неверно введен текст с картинки")

