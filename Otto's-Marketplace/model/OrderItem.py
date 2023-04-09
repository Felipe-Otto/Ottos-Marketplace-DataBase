class OrderItem:
    def __init__(self, order_item_key, quantity, unit_price, product_key, order_key):
        self.order_item_key = order_item_key
        self.quantity = quantity
        self.unit_price = unit_price
        self.product_key = product_key
        self.order_key = order_key

    def __str__(self):
        return f'OrderItem [Primary Key: \033[1;32m{self.order_item_key}\033[0m, ' \
               f'Quantity: \033[1;32m{self.quantity}\033[0m, ' \
               f'Unit Price: \033[1;32m{self.unit_price}\033[0m, ' \
               f'Product Key: \033[1;32m{self.product_key}\033[0m, ' \
               f'Order Key: \033[1;32m{self.order_key}\033[0m]'

    def get_order_item_key(self):
        return self.order_item_key

    def set_order_item_key(self, order_item_key):
        self.order_item_key = order_item_key

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_unit_price(self):
        return self.unit_price

    def set_unit_price(self, unit_price):
        self.unit_price = unit_price

    def get_product_key(self):
        return self.product_key

    def set_product_key(self, product_key):
        self.product_key = product_key

    def get_order_key(self):
        return self.order_key

    def set_order_key(self, order_key):
        self.order_key = order_key
