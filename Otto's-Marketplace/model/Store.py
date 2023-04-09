class Store:
    def __init__(self, store_key, store_name, store_address, store_phone):
        self.store_key = store_key
        self.store_name = store_name
        self.store_address = store_address
        self.store_phone = store_phone

    def __str__(self):
        return f'Store [Primary Key: \033[1;32m{self.store_key}\033[0m, ' \
               f'Name: \033[1;32m{self.store_name}\033[0m, ' \
               f'Address: \033[1;32m{self.store_address}\033[0m, ' \
               f'Phone: \033[1;32m{self.store_phone}\033[0m]'

    def get_store_key(self):
        return self.store_key

    def set_store_key(self, store_key):
        self.store_key = store_key

    def get_store_name(self):
        return self.store_name

    def set_store_name(self, store_name):
        self.store_name = store_name

    def get_store_address(self):
        return self.store_address

    def set_store_address(self, store_address):
        self.store_address = store_address

    def get_store_phone(self):
        return self.store_phone

    def set_store_phone(self, store_phone):
        self.store_phone = store_phone
