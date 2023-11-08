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


#отправляем пустой номер

def test_auth_by_phone_wihtout_number():

    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.ID, 'username').send_keys('')
    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.ID, 'password').send_keys('passwrd')
    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest.driver.implicitly_wait(5)

    assert pytest.driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[1]/div[2]/span').text == ('Введите номер телефона')




@pytest.mark.parametrize('phone, passwrd',[
    ("1254789632", "A1P,i"),#пароль меньше 8 символов
    ("1234567890", "A1P,i525r2A1P,i525r2A1P,i525r2"),#пароль больше 20 символов
    ("$^(&U$^", "A1P,ipYoArr2"),  #символы вместо телефона - переадресация на логин

])


def test_auth_by_phone_fail(phone,passwrd):

    pytest.driver.implicitly_wait(5)
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.ID, 'username').send_keys(phone)
    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.ID, 'password').send_keys(passwrd)
    pytest.driver.implicitly_wait(5)

    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest.driver.implicitly_wait(5)
    
    assert pytest.driver.find_element(By.ID, 'form-error-message').text == ("Неверный логин или пароль") or ("Неверно введен текст с картинки")




# def test_auth_by_phone_without_password():
#
#     #ничего не происходит если не вводить пароль
#
#
#     #element = WebDriverWait(pytest.driver, 3).until(EC.presence_of_element_located((By.ID, "email")))
#     time.sleep(5)
#     pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
#     time.sleep(5)
#    # pytest.driver.find_element(By.ID, 'username').send_keys('test_rostteelekom@mail.ru')
#     pytest.driver.find_element(By.ID, 'username').send_keys('1234567890')
#     time.sleep(3)
#     #pytest.driver.find_element(By.ID, 'password').send_keys('A1P,ipYoArr2')
#     pytest.driver.find_element(By.ID, 'password').send_keys('')
#     time.sleep(3)
#
#     pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#     time.sleep(3)
#    # assert pytest.driver.find_element(By.TAG_NAME, 'h3').text == "Учетные данные"
#     #assert pytest.driver.find_element(By.ID, 'form-error-message').text == ("Неверный логин или пароль" or "Неверно введен текст с картинки")
#     #assert pytest.driver.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/div/form/div[1]/div[2]/span').text == ('Введите номер телефона')