from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"

def test_basket(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".basket-mini")


