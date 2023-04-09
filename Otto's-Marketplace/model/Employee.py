class Employee:
    def __init__(self, employee_key, first_name, last_name, employee_address, employee_email, employee_phone, position_key):
        self.employee_key = employee_key
        self.first_name = first_name
        self.last_name = last_name
        self.employee_address = employee_address
        self.employee_email = employee_email
        self.employee_phone = employee_phone
        self.position_key = position_key

    def __str__(self):
        return f'Employee [Primary Key: {self.employee_key}\033[0m, ' \
               f'First Name: \033[1;32m{self.first_name}\033[0m, ' \
               f'Last Name: \033[1;32m{self.last_name}\033[0m, ' \
               f'Address: \033[1;32m{self.employee_address}\033[0m, ' \
               f'Email: \033[1;32m{self.employee_email}\033[0m, ' \
               f'Phone: \033[1;32m{self.employee_phone}\033[0m, ' \
               f'Position: \033[1;32m{self.position_key}\033[0m]'

    def get_employee_key(self):
        return self.employee_key

    def set_employee_key(self, employee_key):
        self.employee_key = employee_key

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_employee_address(self):
        return self.employee_address

    def set_employee_address(self, employee_address):
        self.employee_address = employee_address

    def get_employee_email(self):
        return self.employee_email

    def set_employee_email(self, employee_email):
        self.employee_email = employee_email

    def get_employee_phone(self):
        return self.employee_phone

    def set_employee_phone(self, employee_phone):
        self.employee_phone = employee_phone

    def get_position_key(self):
        return self.position_key

    def set_position_key(self, position_key):
        self.position_key = position_key
