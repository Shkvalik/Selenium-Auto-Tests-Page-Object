from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_goods_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BUCKET_BASKET)
        button.click()

    def should_be_correct_confirming_message(self):
        confirming_message = self.browser.find_element(*ProductPageLocators.CONFIRMING_MESSAGE).text
        goods_name = self.browser.find_element(*ProductPageLocators.CONFIRMING_MESSAGE).text
        assert goods_name == confirming_message, f"There is no goods name in confirming message\nGoods' name --->{goods_name}\nConfirming message --->{confirming_message}"

    def should_be_correct_message_about_basket_price(self):
        goods_price = self.browser.find_element(*ProductPageLocators.GOODS_PRICE).text.replace('&nbsp;£', '')
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text.replace('&nbsp;£', '')
        assert goods_price == basket_price, f"Goods' price doesn't corresponds to basket's price\nGoods' price --->{goods_price}\nbasket's price --->{basket_price}"