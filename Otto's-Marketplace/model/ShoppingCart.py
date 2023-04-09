class ShoppingCart:
    def __init__(self, shopping_cart_key, customer_key, product_key, quantity):
        self.shopping_cart_key = shopping_cart_key
        self.customer_key = customer_key
        self.product_key = product_key
        self.quantity = quantity

    def __str__(self):
        return f'ShoppingCart [Primary Key: \033[1;32m{self.shopping_cart_key}, ' \
               f'Customer Key: \033[1;32m{self.customer_key}\033[0m, ' \
               f'Product Key: \033[1;32m{self.product_key}\033[0m, ' \
               f'Quantity: \033[1;32m{self.quantity}\033[0m]'

    def get_shopping_cart_key(self):
        return self.shopping_cart_key

    def set_shopping_cart_key(self, shopping_cart_key):
        self.shopping_cart_key = shopping_cart_key

    def get_customer_key(self):
        return self.customer_key

    def set_customer_key(self, customer_key):
        self.customer_key = customer_key

    def get_product_key(self):
        return self.product_key

    def set_product_key(self, product_key):
        self.product_key = product_key

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
