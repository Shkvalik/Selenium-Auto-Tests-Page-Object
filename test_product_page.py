from pages.product_page import ProductPage


def test_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_goods_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_confirming_message()
    page.should_be_correct_message_about_basket_price()