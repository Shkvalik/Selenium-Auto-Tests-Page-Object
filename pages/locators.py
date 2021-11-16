from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_TO_BUCKET_BASKET = (By.CSS_SELECTOR, 'button[class = "btn btn-lg btn-primary btn-add-to-basket"]')
    CONFIRMING_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner strong')
    GOODS_NAME = (By.CSS_SELECTOR, 'div[class="col-sm-6 product_main"] h1')
    GOODS_PRICE = (By.CSS_SELECTOR, 'p[class="price_color"]')
    BASKET_PRICE = (By.CSS_SELECTOR, 'div.alertinner p strong')