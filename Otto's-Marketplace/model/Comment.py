class Comment:
    def __init__(self, comment_key, text, customer_key, product_key):
        self.comment_key = comment_key
        self.comment_text = text
        self.customer_key = customer_key
        self.product_key = product_key

    def __str__(self):
        return f'Comment [Primary Key: \033[1;32m{self.comment_key}\033[0m, ' \
               f'Comment Text: \033[1;32m{self.comment_text}\033[0m, ' \
               f'Customer Key: \033[1;32m{self.customer_key}\033[0m, ' \
               f'Product Key: \033[1;32m{self.product_key}\033[0m]'

    def get_comment_key(self):
        return self.comment_key

    def set_comment_key(self, comment_key):
        self.comment_key = comment_key

    def get_comment_text(self):
        return self.comment_text

    def set_comment_text(self, comment_text):
        self.comment_text = comment_text

    def get_customer_key(self):
        return self.customer_key

    def set_customer_key(self, customer_key):
        self.customer_key = customer_key

    def get_product_key(self):
        return self.product_key

    def set_product_key(self, product_key):
        self.product_key = product_key
