class Product:
    def __init__(self, product_key, product_name, product_description, unit_price, stock_quantity, product_category_key,
                 supplier_key):
        self.product_key = product_key
        self.product_name = product_name
        self.product_description = product_description
        self.unit_price = unit_price
        self.stock_quantity = stock_quantity
        self.product_category_key = product_category_key
        self.supplier_key = supplier_key

    def __str__(self):
        return f'Product [Primary Key: \033[1;32m{self.product_key}\033[0m, ' \
               f'Name: \033[1;32m{self.product_name}\033[0m, ' \
               f'Description: \033[1;32m{self.product_description}\033[0m, ' \
               f'Unit Price: \033[1;32m{self.unit_price}\033[0m, ' \
               f'Stock Quantity: \033[1;32m{self.stock_quantity}\033[0m, ' \
               f'Category: \033[1;32m{self.product_category_key}\033[0m, ' \
               f'Supplier Key: \033[1;32m{self.supplier_key}\033[0m]'

    def get_product_key(self):
        return self.product_key

    def set_product_key(self, product_key):
        self.product_key = product_key

    def get_product_name(self):
        return self.product_name

    def set_product_name(self, product_name):
        self.product_name = product_name

    def get_product_description(self):
        return self.product_description

    def set_product_description(self, product_description):
        self.product_description = product_description

    def get_unit_price(self):
        return self.unit_price

    def set_unit_price(self, unit_price):
        self.unit_price = unit_price

    def get_stock_quantity(self):
        return self.stock_quantity

    def set_stock_quantity(self, stock_quantity):
        self.stock_quantity = stock_quantity

    def get_product_category_key(self):
        return self.product_category_key

    def set_product_category_key(self, product_category_key):
        self.product_category_key = product_category_key

    def get_supplier_key(self):
        return self.supplier_key

    def set_supplier_key(self, supplier_key):
        self.supplier_key = supplier_key
