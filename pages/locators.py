from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BTN_BASKET = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')


class BasketPageLocators():
    empty_text = {
        "en-gb": "Your basket is empty",
        "en": "Your basket is empty",
        "ru": "Ваша корзина пуста",
        "es": "Tu carrito esta vacío",
        "fr": "Votre panier est vide",
        "de": "Ihr Warenkorb ist leer",
        "pl": "Twój koszyk jest pusty"
    }
    BASKET_INNER = (By.CSS_SELECTOR, "#content_inner p")
    # если в корзине есть товар то появляются:
    BASKET_TITLE = (By.CSS_SELECTOR, "#content_inner div.basket-title")
    BASKET_ROW = (By.CSS_SELECTOR, "#content_inner div.basket-title div.row")


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