class Customer:
    def __init__(self, customer_key, first_name, last_name, customer_address, customer_email, customer_phone):
        self.customer_key = customer_key
        self.first_name = first_name
        self.last_name = last_name
        self.customer_address = customer_address
        self.customer_email = customer_email
        self.customer_phone = customer_phone

    def __str__(self):
        return f'Customer [Primary Key: \033[1;32m{self.customer_key}\033[0m, ' \
               f'First Name: \033[1;32m{self.first_name}\033[0m, ' \
               f'Last Name: \033[1;32m{self.last_name}\033[0m, ' \
               f'Address: \033[1;32m{self.customer_address}\033[0m, ' \
               f'E-mail: \033[1;32m{self.customer_email}\033[0m, ' \
               f'Phone: \033[1;32m{self.customer_phone}\033[0m]'

    def get_customer_key(self):
        return self.customer_key

    def set_customer_key(self, customer_key):
        self.customer_key = customer_key

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_customer_address(self):
        return self.customer_address

    def set_customer_address(self, customer_address):
        self.customer_address = customer_address

    def get_customer_email(self):
        return self.customer_email

    def set_customer_email(self, customer_email):
        self.customer_email = customer_email

    def get_customer_phone(self):
        return self.customer_phone

    def set_customer_phone(self, customer_phone):
        self.customer_phone = customer_phone
