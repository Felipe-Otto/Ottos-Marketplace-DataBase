from model.ShoppingCart import ShoppingCart
from connection.sqlserver_connection import SQLServerConnection


def validate_key(cursor, ShoppingCartKey):
    try:
        query = f'SELECT ' \
                f'    * ' \
                f'FROM ' \
                f'    ShoppingCart ' \
                f'WHERE ' \
                f'    ShoppingCartKey = {ShoppingCartKey};'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return True
        else:
            return False
    except Exception as e:
        print(f'Error while trying to validate shopping cart key from \033[1;31mShopping Cart\033[0m:\n{e}')


def define_key(cursor):
    try:
        query = f'SELECT ' \
                f'    MAX(ShoppingCartKey) ' \
                f'FROM ' \
                f'    ShoppingCart;'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return row[0] + 1
    except Exception as e:
        print(f'Error while trying to select the greater shopping cart key from \033[1;31mShopping Cart\033[0m:\n{e}')


class ShoppingCartDAO:
    def __init__(self):
        self.conn = SQLServerConnection()

    def select_all_shopping_carts(self):
        try:
            query = 'SELECT ' \
                    '    * ' \
                    'FROM ' \
                    '    ShoppingCart;'
            with self.conn as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                return [ShoppingCart(*row) for row in rows]
        except Exception as e:
            print(f'Error while trying to select all data from \033[1;31mShopping Cart\033[0m:\n{e}')

    def select_shopping_cart_by_key(self, ShoppingCartKey):
        try:
            query = f'SELECT ' \
                    f'    * ' \
                    f'FROM ' \
                    f'    ShoppingCart ' \
                    f'WHERE ' \
                    f'    ShoppingCartKey = {ShoppingCartKey};'
            with self.conn as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                if row is not None:
                    return ShoppingCart(*row)
                else:
                    print(f'\033[1;31mThere is no shopping cart with primary key {ShoppingCartKey}.\033[0m')
        except Exception as e:
            print(f'Error while trying to select data from \033[1;31mShopping Cart\033[0m with specific key:\n{e}')

    def insert_shopping_cart(self, shopping_cart):
        with self.conn as cursor:
            ShoppingCartKey = define_key(cursor)
            try:
                query = f'INSERT INTO ' \
                        f'    ShoppingCart (ShoppingCartKey, CustomerKey, ProductKey, Quantity) ' \
                        f'VALUES ' \
                        f'    ({ShoppingCartKey}, {shopping_cart.get_customer_key()}, {shopping_cart.get_product_key()}, {shopping_cart.get_quantity()});'
                cursor.execute(query)
                cursor.commit()
                print('\033[1;32mData successfully inserted in Shopping Cart.\033[0m')
            except Exception as e:
                print(f'Error while trying to insert data into \033[1;31mShopping Cart\033[0m:\n{e}')

    def update_shopping_cart(self, shopping_cart, ShoppingCartKey):
        with self.conn as cursor:
            if validate_key(cursor, ShoppingCartKey):
                try:
                    query = f'UPDATE ' \
                            f'    ShoppingCart ' \
                            f'SET ' \
                            f'    CustomerKey = {shopping_cart.get_customer_key()}, ' \
                            f'    ProductKey = {shopping_cart.get_product_key()}, ' \
                            f'    Quantity = {shopping_cart.get_quantity()} ' \
                            f'WHERE ' \
                            f'    ShoppingCartKey = {ShoppingCartKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData successfully updated in Shopping Cart.\033[0m')
                except Exception as e:
                    print(f'Error while trying to update data from \033[1;31mShopping Cart\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no shopping cart with primary key {ShoppingCartKey}.\033[0m')

    def delete_shopping_cart(self, ShoppingCartKey):
        with self.conn as cursor:
            if validate_key(cursor, ShoppingCartKey):
                try:
                    query = f'DELETE FROM ' \
                            f'    ShoppingCart ' \
                            f'WHERE ' \
                            f'    ShoppingCartKey = {ShoppingCartKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData deleted successfully from Shopping Cart.\033[0m')
                except Exception as e:
                    print(f'Error while trying to delete data from \033[1;31mShopping Cart\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no shopping cart with primary key {ShoppingCartKey}.\033[0m')
