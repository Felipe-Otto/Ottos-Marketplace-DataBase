from model.Customer import Customer
from connection.sqlserver_connection import SQLServerConnection


def validate_key(cursor, CustomerKey):
    try:
        query = f'SELECT ' \
                f'    * ' \
                f'FROM' \
                f'    Customer ' \
                f'WHERE ' \
                f'    CustomerKey = {CustomerKey};'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return True
        else:
            return False
    except Exception as e:
        print(f'Error while trying to to validate customer key from \033[1;31mCustomer\033[0m:\n{e}')


def define_key(cursor):
    try:
        query = f'SELECT ' \
                f'    MAX(CustomerKey) ' \
                f'FROM ' \
                f'    Customer;'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return row[0] + 1
    except Exception as e:
        print(f'Error while trying to select the greater customer key from \033[1;31mCustomer\033[0m:\n{e}')


class CustomerDAO:
    def __init__(self):
        self.conn = SQLServerConnection()

    def select_all_customers(self):
        try:
            query = 'SELECT ' \
                    '    * ' \
                    'FROM ' \
                    '    Customer;'
            with self.conn as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                return [Customer(*row) for row in rows]
        except Exception as e:
            print(f'Error while trying to select all data from \033[1;31mCustomer\033[0m:\n{e}')

    def select_customer_by_key(self, CustomerKey):
        try:
            query = f'SELECT ' \
                    f'    * ' \
                    f'FROM ' \
                    f'    Customer ' \
                    f'WHERE ' \
                    f'    CustomerKey = {CustomerKey};'
            with self.conn as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                if row is not None:
                    return Customer(*row)
                else:
                    print(f'\033[1;31mThere is no customer with primary key {CustomerKey}.\033[0m')
        except Exception as e:
            print(f'Error while trying to select data from \033[1;31mCustomer\033[0m with specific key:\n{e}')

    def insert_customer(self, customer):
        with self.conn as cursor:
            CustomerKey = define_key(cursor)
            try:
                query = f'INSERT INTO ' \
                        f'    Customer (CustomerKey, FirstName, LastName, CustomerAddress, CustomerEmail, CustomerPhone) ' \
                        f'VALUES ' \
                        f'    ({CustomerKey}, \'{customer.get_first_name()}\', \'{customer.get_last_name()}\', \'{customer.get_customer_address()}\', \'{customer.get_customer_email()}\', \'{customer.get_customer_phone()}\');'
                cursor.execute(query)
                cursor.commit()
                print('\033[1;32mData successfully inserted in Customer.\033[0m')
            except Exception as e:
                print(f'Error while trying to insert data into \033[1;31mCustomer\033[0m:\n{e}')

    def update_customer(self, customer, CustomerKey):
        with self.conn as cursor:
            if validate_key(cursor, CustomerKey):
                try:
                    query = f'UPDATE ' \
                            f'    Customer ' \
                            f'SET ' \
                            f'    FirstName = \'{customer.get_first_name()}\', ' \
                            f'    LastName = \'{customer.get_last_name()}\', ' \
                            f'    CustomerAddress = \'{customer.get_customer_address()}\', ' \
                            f'    CustomerEmail = \'{customer.get_customer_email()}\', ' \
                            f'    CustomerPhone = \'{customer.get_customer_phone()}\' ' \
                            f'WHERE ' \
                            f'    CustomerKey = {CustomerKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData successfully updated in Customer.\033[0m')
                except Exception as e:
                    print(f'Error while trying to update data from \033[1;31mCustomer\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no customer with primary key {CustomerKey}.\033[0m')

    def delete_customer(self, CustomerKey):
        with self.conn as cursor:
            if validate_key(cursor, CustomerKey):
                try:
                    query = f'DELETE FROM ' \
                            f'    Customer ' \
                            f'WHERE ' \
                            f'    CustomerKey = {CustomerKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData deleted successfully from Customer\033[0m')
                except Exception as e:
                    print(f'Error while trying to delete data from \033[1;31mCustomer\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no customer with primary key {CustomerKey}.\033[0m')
