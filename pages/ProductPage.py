class ProductPage:
    def __init__(self, page):
        self.page = page

    def sort_products_by(self, criteria):
        self.page.select_option(".product_sort_container", criteria)

    def get_product_prices(self):
        return [float(price.inner_text()[1:]) for price in self.page.locator(".inventory_item_price").all()]

    def add_item_to_cart(self, item_index):
        self.page.locator(".btn_inventory").nth(item_index).click()

    def add_multiple_items_to_cart(self, items):
        for item in items:
            self.add_item_to_cart(item)