from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BTN_BASKET = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


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
    PART_URL = "login"

    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, 'input[name="login-username"]')
    LOGIN_PASS = (By.CSS_SELECTOR, 'input[name="login-password"]')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[name="login_submit"]')

    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, 'input[name="registration-email"]')
    REGISTER_PASS1 = (By.CSS_SELECTOR, 'input[name="registration-password1"]')
    REGISTER_PASS2 = (By.CSS_SELECTOR, 'input[name="registration-password2"]')
    REGISTER_BTN = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators():
    ADD_TO_BUCKET_BASKET = (By.CSS_SELECTOR, 'button[class = "btn btn-lg btn-primary btn-add-to-basket"]')
    CONFIRMING_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner strong')
    GOODS_NAME = (By.CSS_SELECTOR, 'div[class="col-sm-6 product_main"] h1')
    GOODS_PRICE = (By.CSS_SELECTOR, 'p[class="price_color"]')
    BASKET_PRICE = (By.CSS_SELECTOR, 'div.alertinner p strong')