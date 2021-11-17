import time
import pytest
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.add_product
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        password = 'Akmnfoiemp'
        email = 'Shkvalik' + str(time.time()) + "@fakemail.org"
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.confirming_message_should_not_be()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_goods_to_basket()
        page.should_be_correct_confirming_message()
        page.should_be_correct_message_about_basket_price()


def test_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_goods_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_confirming_message()
    page.should_be_correct_message_about_basket_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_goods_to_basket()
    page.solve_quiz_and_get_code()
    page.confirming_message_should_not_be()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_goods_to_basket()
    page.solve_quiz_and_get_code()
    page.confirming_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_btn_basket()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()


@pytest.mark.need_review
@pytest.mark.parametrize('suffix', (no if no != 7 else pytest.param(no, marks=pytest.mark.xfail) for no in range(10)))
def test_guest_can_add_product_to_basket(browser, suffix):
    url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{suffix}"
    page = ProductPage(browser, url)
    page.open()
    page.add_goods_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_confirming_message()
    page.should_be_correct_message_about_basket_price()
