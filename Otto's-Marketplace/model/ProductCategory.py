class ProductCategory:
    def __init__(self, product_category_key, product_category_name, product_category_description):
        self.product_category_key = product_category_key
        self.product_category_name = product_category_name
        self.product_category_description = product_category_description

    def __str__(self):
        return f'Product Category [Primary Key: \033[1;32m{self.product_category_key}\033[0m, ' \
               f'Name: \033[1;32m{self.product_category_name}\033[0m, ' \
               f'Description: \033[1;32m{self.product_category_description}\033[0m]'

    def get_product_category_key(self):
        return self.product_category_key

    def set_product_category_key(self, product_category_key):
        self.product_category_key = product_category_key

    def get_product_category_name(self):
        return self.product_category_name

    def set_product_category_name(self, product_category_name):
        self.product_category_name = product_category_name

    def get_product_category_description(self):
        return self.product_category_description

    def set_product_category_description(self, product_category_description):
        self.product_category_description = product_category_description
