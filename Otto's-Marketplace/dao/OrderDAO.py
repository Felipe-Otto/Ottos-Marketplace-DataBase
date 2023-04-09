from model.Order import Order
from connection.sqlserver_connection import SQLServerConnection


def validate_key(cursor, OrderKey):
    try:
        query = f'SELECT ' \
                f'    * ' \
                f'FROM ' \
                f'    [Order] ' \
                f'WHERE ' \
                f'    OrderKey = {OrderKey};'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return True
        else:
            return False
    except Exception as e:
        print(f'Error while trying to validate order key from \033[1;31mOrder\033[0m:\n{e}')


def define_key(cursor):
    try:
        query = f'SELECT ' \
                f'    MAX(OrderKey) ' \
                f'FROM ' \
                f'    [Order];'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return row[0] + 1
    except Exception as e:
        print(f'Error while trying to select the greater order key from \033[1;31mOrder\033[0m:\n{e}')


class OrderDAO:
    def __init__(self):
        self.conn = SQLServerConnection()

    def select_all_orders(self):
        try:
            query = 'SELECT ' \
                    '    * ' \
                    'FROM ' \
                    '    [Order];'
            with self.conn as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                return [Order(*row) for row in rows]
        except Exception as e:
            print(f'Error while trying to select all data from \033[1;31mOrder\033[0m:\n{e}')

    def select_order_by_key(self, OrderKey):
        try:
            query = f'SELECT ' \
                    f'    * ' \
                    f'FROM ' \
                    f'    [Order] ' \
                    f'WHERE ' \
                    f'    OrderKey = {OrderKey};'
            with self.conn as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                if row is not None:
                    return Order(*row)
                else:
                    print(f'\033[1;31mThere is no order with primary key {OrderKey}.\033[0m')
        except Exception as e:
            print(f'Error while trying to select data from \033[1;31mOrder\033[0m with specific key:\n{e}')

    def insert_order(self, order):
        with self.conn as cursor:
            OrderKey = define_key(cursor)
            try:
                query = f'INSERT INTO ' \
                        f'    [Order] (OrderKey, OrderDate, OrderStatus, TotalPrice, CustomerKey, StoreKey) ' \
                        f'VALUES ' \
                        f'    ({OrderKey}, \'{order.get_order_date()}\', \'{order.get_order_status()}\', {order.get_total_price()}, {order.get_customer_key()}, {order.get_store_key()});'
                cursor.execute(query)
                cursor.commit()
                print('\033[1;32mData successfully inserted in Order.\033[0m')
            except Exception as e:
                print(f'Error while trying to insert data into \033[1;31mOrder\033[0m:\n{e}')

    def update_order(self, order, OrderKey):
        with self.conn as cursor:
            if validate_key(cursor, OrderKey):
                try:
                    query = f'UPDATE ' \
                            f'    [Order] ' \
                            f'SET ' \
                            f'    OrderDate = \'{order.get_order_date()}\', ' \
                            f'    OrderStatus = \'{order.get_order_status()}\', ' \
                            f'    TotalPrice = {order.get_total_price()}, ' \
                            f'    CustomerKey = {order.get_customer_key()}, ' \
                            f'    StoreKey = {order.get_store_key()} ' \
                            f'WHERE ' \
                            f'    OrderKey = {OrderKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData successfully updated in Order.\033[0m')
                except Exception as e:
                    print(f'Error while trying to update data from \033[1;31mOrder\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no order with primary key {OrderKey}.\033[0m')

    def delete_order(self, OrderKey):
        with self.conn as cursor:
            if validate_key(cursor, OrderKey):
                try:
                    query = f'DELETE FROM ' \
                            f'    [Order] ' \
                            f'WHERE ' \
                            f'    OrderKey = {OrderKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData deleted successfully from Order.\033[0m')
                except Exception as e:
                    print(f'Error while trying to delete data from \033[1;31mOrder\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no order with primary key {OrderKey}.\033[0m')
