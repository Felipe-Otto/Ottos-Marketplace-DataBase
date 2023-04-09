from model.ProductCategory import ProductCategory
from connection.sqlserver_connection import SQLServerConnection


def validate_key(cursor, ProductCategoryKey):
    try:
        query = f'SELECT ' \
                f'    * ' \
                f'FROM ' \
                f'    ProductCategory ' \
                f'WHERE ' \
                f'    ProductCategoryKey = {ProductCategoryKey};'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return True
        else:
            return False
    except Exception as e:
        print(f'Error while trying to validate product category key from \033[1;31mProduct Category\033[0m:\n{e}')


def define_key(cursor):
    try:
        query = f'SELECT ' \
                f'    MAX(ProductCategoryKey) ' \
                f'FROM ' \
                f'    ProductCategory;'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return row[0] + 1
    except Exception as e:
        print(f'Error while trying to select the greater product category key from \033[1;31mProduct Category\033[0m:\n{e}')


class ProductCategoryDAO:
    def __init__(self):
        self.conn = SQLServerConnection()

    def select_all_product_categories(self):
        try:
            query = 'SELECT ' \
                    '    * ' \
                    'FROM ' \
                    '    ProductCategory;'
            with self.conn as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                return [ProductCategory(*row) for row in rows]
        except Exception as e:
            print(f'Error while trying to select all data from \033[1;31mProduct Category\033[0m:\n{e}')

    def select_product_category_by_key(self, ProductCategoryKey):
        try:
            query = f'SELECT ' \
                    f'    * ' \
                    f'FROM ' \
                    f'    ProductCategory ' \
                    f'WHERE ' \
                    f'    ProductCategoryKey = {ProductCategoryKey};'
            with self.conn as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                if row is not None:
                    return ProductCategory(*row)
                else:
                    print(f'\033[1;31mThere is no product category with primary key {ProductCategoryKey}.\033[0m')
        except Exception as e:
            print(f'Error while trying to select data from \033[1;31mProduct Category\033[0m with specific key:\n{e}')

    def insert_product_category(self, product_category):
        with self.conn as cursor:
            ProductCategoryKey = define_key(cursor)
            try:
                query = f'INSERT INTO ' \
                        f'    ProductCategory (ProductCategoryKey, ProductCategoryName, ProductCategoryDescription) ' \
                        f'VALUES ' \
                        f'    ({ProductCategoryKey}, \'{product_category.get_product_category_name()}\', \'{product_category.get_product_category_description()}\');'
                cursor.execute(query)
                cursor.commit()
                print('\033[1;32mData successfully inserted in ProductCategory.\033[0m')
            except Exception as e:
                print(f'Error while trying to insert data into \033[1;31mProduct Category\033[0m:\n{e}')

    def update_product_category(self, product_category, ProductCategoryKey):
        with self.conn as cursor:
            if validate_key(cursor, ProductCategoryKey):
                try:
                    query = f'UPDATE ' \
                            f'    ProductCategory ' \
                            f'SET ' \
                            f'    ProductCategoryName = \'{product_category.get_product_category_name()}\', ' \
                            f'    ProductCategoryDescription = \'{product_category.get_product_category_description()}\' ' \
                            f'WHERE ' \
                            f'    ProductCategoryKey = {ProductCategoryKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData successfully updated in Product Category.\033[0m')
                except Exception as e:
                    print(f'Error while trying to update data from \033[1;31mProduct Category\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no product category with primary key {ProductCategoryKey}.\033[0m')

    def delete_product_category(self, ProductCategoryKey):
        with self.conn as cursor:
            if validate_key(cursor, ProductCategoryKey):
                try:
                    query = f'DELETE FROM ' \
                            f'    ProductCategory ' \
                            f'WHERE ' \
                            f'    ProductCategoryKey = {ProductCategoryKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData deleted successfully from Product Category.\033[0m')
                except Exception as e:
                    print(f'Error while trying to delete data from \033[1;31mProduct Category\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no product category with primary key {ProductCategoryKey}.\033[0m')
