class Supplier:
    def __init__(self, supplier_key, supplier_name, supplier_address, supplier_email, supplier_phone):
        self.supplier_key = supplier_key
        self.supplier_name = supplier_name
        self.supplier_address = supplier_address
        self.supplier_email = supplier_email
        self.supplier_phone = supplier_phone

    def __str__(self):
        return f'Supplier [Primary Key: \033[1;32m{self.supplier_key}\033[0m, ' \
               f'Name: \033[1;32m{self.supplier_name}\033[0m, ' \
               f'Address: \033[1;32m{self.supplier_address}\033[0m, ' \
               f'Email: \033[1;32m{self.supplier_email}\033[0m, ' \
               f'Phone: \033[1;32m{self.supplier_phone}\033[0m]'

    def get_supplier_key(self):
        return self.supplier_key

    def set_supplier_key(self, supplier_key):
        self.supplier_key = supplier_key

    def get_supplier_name(self):
        return self.supplier_name

    def set_supplier_name(self, supplier_name):
        self.supplier_name = supplier_name

    def get_supplier_address(self):
        return self.supplier_address

    def set_supplier_address(self, supplier_address):
        self.supplier_address = supplier_address

    def get_supplier_email(self):
        return self.supplier_email

    def set_supplier_email(self, supplier_email):
        self.supplier_email = supplier_email

    def get_supplier_phone(self):
        return self.supplier_phone

    def set_supplier_phone(self, supplier_phone):
        self.supplier_phone = supplier_phone
