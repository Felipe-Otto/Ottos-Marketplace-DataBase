from model.Product import Product
from connection.sqlserver_connection import SQLServerConnection


def validate_key(cursor, ProductKey):
    try:
        query = f'SELECT ' \
                f'    * ' \
                f'FROM ' \
                f'    Product ' \
                f'WHERE ' \
                f'    ProductKey = {ProductKey};'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return True
        else:
            return False
    except Exception as e:
        print(f'Error while trying to validate product key from \033[1;31mProduct\033[0m:\n{e}')


def define_key(cursor):
    try:
        query = f'SELECT ' \
                f'    MAX(ProductKey) ' \
                f'FROM ' \
                f'    Product;'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return row[0] + 1
    except Exception as e:
        print(f'Error while trying to select the greater product key from \033[1;31mProduct\033[0m:\n{e}')


class ProductDAO:
    def __init__(self):
        self.conn = SQLServerConnection()

    def select_all_products(self):
        try:
            query = 'SELECT ' \
                    '    * ' \
                    'FROM ' \
                    '    Product;'
            with self.conn as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                return [Product(*row) for row in rows]
        except Exception as e:
            print(f'Error while trying to select all data from \033[1;31mProduct\033[0m:\n{e}')

    def select_product_by_key(self, ProductKey):
        try:
            query = f'SELECT ' \
                    f'    * ' \
                    f'FROM ' \
                    f'    Product ' \
                    f'WHERE ' \
                    f'    ProductKey = {ProductKey};'
            with self.conn as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                if row is not None:
                    return Product(*row)
                else:
                    print(f'\033[1;31mThere is no product with primary key {ProductKey}.\033[0m')
        except Exception as e:
            print(f'Error while trying to select data from \033[1;31mProduct\033[0m with specific key:\n{e}')

    def insert_product(self, product):
        with self.conn as cursor:
            ProductKey = define_key(cursor)
            try:
                query = f'INSERT INTO ' \
                        f'    Product (ProductKey, ProductName, ProductDescription, UnitPrice, StockQuantity, ProductCategoryKey, SupplierKey) ' \
                        f'VALUES ' \
                        f'    ({ProductKey}, \'{product.get_product_name()}\', \'{product.get_product_description()}\', {product.get_unit_price()}, {product.get_stock_quantity()}, {product.get_product_category_key()}, {product.get_supplier_key()});'
                cursor.execute(query)
                cursor.commit()
                print('\033[1;32mData successfully inserted in Product.\033[0m')
            except Exception as e:
                print(f'Error while trying to insert data into \033[1;31mProduct\033[0m:\n{e}')

    def update_product(self, product, ProductKey):
        with self.conn as cursor:
            if validate_key(cursor, ProductKey):
                try:
                    query = f'UPDATE ' \
                            f'    Product ' \
                            f'SET ' \
                            f'    ProductName = \'{product.get_product_name()}\', ' \
                            f'    ProductDescription = \'{product.get_product_description()}\', ' \
                            f'    UnitPrice = {product.get_unit_price()}, ' \
                            f'    StockQuantity = {product.get_stock_quantity()}, ' \
                            f'    ProductCategoryKey = {product.get_product_category_key()}, ' \
                            f'    SupplierKey = {product.get_supplier_key()}' \
                            f'WHERE ' \
                            f'    ProductKey = {ProductKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData successfully updated in Product.\033[0m')
                except Exception as e:
                    print(f'Error while trying to update data from \033[1;31mProduct\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no product with primary key {ProductKey}.\033[0m')

    def delete_product(self, ProductKey):
        with self.conn as cursor:
            if validate_key(cursor, ProductKey):
                try:
                    query = f'DELETE FROM ' \
                            f'    Product ' \
                            f'WHERE ' \
                            f'    ProductKey = {ProductKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData deleted successfully from Product.\033[0m')
                except Exception as e:
                    print(f'Error while trying to delete data from \033[1;31mProduct\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no product with primary key {ProductKey}.\033[0m')
