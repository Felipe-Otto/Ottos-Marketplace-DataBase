class Order:
    def __init__(self, order_key, order_date, order_status, total_price, customer_key, store_key):
        self.order_key = order_key
        self.order_date = order_date
        self.order_status = order_status
        self.total_price = total_price
        self.customer_key = customer_key
        self.store_key = store_key

    def __str__(self):
        return f'Order [Primary Key: \033[1;32m{self.order_key}\033[0m, ' \
               f'Date: \033[1;32m{self.order_date}\033[0m, ' \
               f'Status: \033[1;32m{self.order_status}\033[0m, ' \
               f'Total Price: \033[1;32m{self.total_price}\033[0m, ' \
               f'Customer Key: \033[1;32m{self.customer_key}\033[0m, ' \
               f'Store Key: \033[1;32m{self.store_key}\033[0m]'

    def get_order_key(self):
        return self.order_key

    def set_order_key(self, order_key):
        self.order_key = order_key

    def get_order_date(self):
        return self.order_date

    def set_order_date(self, order_date):
        self.order_date = order_date

    def get_order_status(self):
        return self.order_status

    def set_order_status(self, order_status):
        self.order_status = order_status

    def get_total_price(self):
        return self.total_price

    def set_total_price(self, total_price):
        self.total_price = total_price

    def get_customer_key(self):
        return self.customer_key

    def set_customer_key(self, customer_key):
        self.customer_key = customer_key

    def get_store_key(self):
        return self.store_key

    def set_store_key(self, store_key):
        self.store_key = store_key
