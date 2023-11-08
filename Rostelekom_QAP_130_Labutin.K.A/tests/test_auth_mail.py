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



#авторизация по зарегистрированной почте и паролю


def test_auth_by_mail():

    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 'username').send_keys('test_rostelekom@mail.ru')
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 'password').send_keys('A1P,ipYoArr2')
    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest.driver.implicitly_wait(5)
    assert pytest.driver.find_element(By.TAG_NAME, 'h3').text == "Учетные данные"

#передаем в почту пустое поле

def test_auth_without_mail():

    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 'username').send_keys('')
    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 'password').send_keys('A1P,ipYoArr2')
    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest.driver.implicitly_wait(5)

    assert pytest.driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[1]/div[2]/span').text == ('Введите адрес, указанный при регистрации')



@pytest.mark.parametrize('mail, passwrd',[
    ("test_rostelekom@mail.ru", "A1P,i"), #пароль меньше 8 символов
    ("test_rostelekom@mail.ru", "A1P,i525r2A1P,i525r2A1P,i525r2"), #пароль больше 20 символов
    ("-test_ros;:%;?telekom@mail.ru", "A1P,ipYoArr2"), #символы в почте
    ("123434", "A1P,ipYoArr2"), #числа в почте - будет переадресация на логин


])


def test_auth_by_fail_mail(mail,passwrd):

    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.ID, 'username').send_keys(mail)
    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.ID, 'password').send_keys(passwrd)
    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest.driver.implicitly_wait(5)

    assert pytest.driver.find_element(By.ID, 'form-error-message').text == ("Неверный логин или пароль") or ("Неверно введен текст с картинки")


