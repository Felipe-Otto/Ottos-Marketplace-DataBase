from model.OrderItem import OrderItem
from connection.sqlserver_connection import SQLServerConnection


def validate_key(cursor, OrderItemKey):
    try:
        query = f'SELECT ' \
                f'    * ' \
                f'FROM ' \
                f'    OrderItem ' \
                f'WHERE ' \
                f'    OrderItemKey = {OrderItemKey};'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return True
        else:
            return False
    except Exception as e:
        print(f'Error while trying to validate order item key from \033[1;31mOrder Item\033[0m:\n{e}')


def define_key(cursor):
    try:
        query = f'SELECT ' \
                f'    MAX(OrderItemKey) ' \
                f'FROM ' \
                f'    [OrderItem];'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return row[0] + 1
    except Exception as e:
        print(f'Error while trying to select the greater order item key from \033[1;31mOrder Item\033[0m:\n{e}')


class OrderItemDAO:
    def __init__(self):
        self.conn = SQLServerConnection()

    def select_all_order_items(self):
        try:
            query = 'SELECT ' \
                    '    * ' \
                    'FROM ' \
                    '    OrderItem;'
            with self.conn as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                return [OrderItem(*row) for row in rows]
        except Exception as e:
            print(f'Error while trying to select all data from \033[1;31mOrder Item\033[0m:\n{e}')

    def select_order_item_by_key(self, OrderItemKey):
        try:
            query = f'SELECT ' \
                    f'    * ' \
                    f'FROM ' \
                    f'    OrderItem ' \
                    f'WHERE ' \
                    f'    OrderItemKey = {OrderItemKey};'
            with self.conn as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                if row is not None:
                    return OrderItem(*row)
                else:
                    print(f'\033[1;31mThere is no order item with primary key {OrderItemKey}.\033[0m')
        except Exception as e:
            print(f'Error while trying to select data from \033[1;31mOrder Item\033[0m with specific key:\n{e}')

    def insert_order_item(self, order_item):
        with self.conn as cursor:
            OrderItemKey = define_key(cursor)
            try:
                query = f'INSERT INTO ' \
                        f'    OrderItem (OrderItemKey, Quantity, UnitPrice, ProductKey, OrderKey) ' \
                        f'VALUES ' \
                        f'    ({OrderItemKey}, {order_item.get_quantity()}, {order_item.get_unit_price()}, {order_item.get_product_key()}, {order_item.get_order_key()});'
                cursor.execute(query)
                cursor.commit()
                print('\033[1;32mData successfully inserted in Order Item.\033[0m')
            except Exception as e:
                print(f'Error while trying to insert data into \033[1;31mOrder Item\033[0m:\n{e}')

    def update_order_item(self, orderItem, OrderItemKey):
        with self.conn as cursor:
            if validate_key(cursor, OrderItemKey):
                try:
                    query = f'UPDATE ' \
                            f'    OrderItem ' \
                            f'SET ' \
                            f'    Quantity = {orderItem.get_quantity()}, ' \
                            f'    UnitPrice = {orderItem.get_unit_price()}, ' \
                            f'    ProductKey = {orderItem.get_product_key()}, ' \
                            f'    OrderKey = {orderItem.get_order_key()} ' \
                            f'WHERE ' \
                            f'    OrderItemKey = {OrderItemKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData successfully updated in Order Item.\033[0m')
                except Exception as e:
                    print(f'Error while trying to update data from \033[1;31mOrder Item\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no order item with primary key {OrderItemKey}.\033[0m')

    def delete_order_item(self, OrderItemKey):
        with self.conn as cursor:
            if validate_key(cursor, OrderItemKey):
                try:
                    query = f'DELETE FROM ' \
                            f'    OrderItem ' \
                            f'WHERE ' \
                            f'    OrderItemKey = {OrderItemKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData deleted successfully from Order Item.\033[0m')
                except Exception as e:
                    print(f'Error while trying to delete data from \033[1;31mOrder Item\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no order item with primary key {OrderItemKey}.\033[0m')
