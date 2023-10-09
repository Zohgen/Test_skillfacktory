from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest

from selenium import webdriver


@pytest.fixture(autouse=True)
def testing():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    pytest.driver= webdriver.Chrome(options=chrome_options)
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()

def test_show_my_pets():

    element = WebDriverWait(pytest.driver, 3).until(EC.presence_of_element_located((By.ID, "email")))

    #вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys('sobachki@yandex.ru')

    element = WebDriverWait(pytest.driver, 3).until(EC.presence_of_element_located((By.ID, "pass")))
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys('lovesobachek')

    element = WebDriverWait(pytest.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    #переход на страницу Мои питомцы
    element = WebDriverWait(pytest.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/my_pets']")))
    pytest.driver.find_element(By.XPATH, "//a[@href='/my_pets']").click()
    # Проверяем, что мы оказались на странице Мои питомцы
    assert pytest.driver.find_element(By.CSS_SELECTOR, 'html>body>div>div>div>h2').text == "ololoev"

    #Добавили неявное ожидание
    pytest.driver.implicitly_wait(3)
    Element_images = pytest.driver.find_elements(By.CSS_SELECTOR,'.card-deck .card-img-top')
    Element_names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    Element_descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')


    for i in range(len(Element_names)):
        assert Element_images[i].get_attribute('src') != ''
        assert Element_names[i].text != ''
        assert Element_descriptions[i].text != ''
        assert ', ' in Element_descriptions[i]
        parts = Element_descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0









