from model.Supplier import Supplier
from connection.sqlserver_connection import SQLServerConnection


def validate_key(cursor, SupplierKey):
    try:
        query = f'SELECT ' \
                f'    * ' \
                f'FROM ' \
                f'    Supplier ' \
                f'WHERE ' \
                f'    SupplierKey = {SupplierKey};'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return True
        else:
            return False
    except Exception as e:
        print(f'Error while trying to validate supplier key from \033[1;31mSupplier\033[0m:\n{e}')


def define_key(cursor):
    try:
        query = f'SELECT ' \
                f'    MAX(SupplierKey) ' \
                f'FROM ' \
                f'    Supplier;'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return row[0] + 1
    except Exception as e:
        print(f'Error while trying to select the greater supplier key from \033[1;31mSupplier\033[0m:\n{e}')


class SupplierDAO:
    def __init__(self):
        self.conn = SQLServerConnection()

    def select_all_suppliers(self):
        try:
            query = 'SELECT ' \
                    '    * ' \
                    'FROM ' \
                    '    Supplier;'
            with self.conn as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                return [Supplier(*row) for row in rows]
        except Exception as e:
            print(f'Error while trying to select all data from \033[1;31mSupplier\033[0m:\n{e}')

    def select_supplier_by_key(self, SupplierKey):
        try:
            query = f'SELECT ' \
                    f'    * ' \
                    f'FROM ' \
                    f'    Supplier ' \
                    f'WHERE ' \
                    f'    SupplierKey = {SupplierKey};'
            with self.conn as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                if row is not None:
                    return Supplier(*row)
                else:
                    print(f'\033[1;31mThere is no supplier with primary key {SupplierKey}.\033[0m')
        except Exception as e:
            print(f'Error while trying to select data from \033[1;31mSupplier\033[0m with specific key:\n{e}')

    def insert_supplier(self, supplier):
        with self.conn as cursor:
            SupplierKey = define_key(cursor)
            try:
                query = f'INSERT INTO ' \
                        f'    Supplier (SupplierKey, SupplierName, SupplierAddress, SupplierEmail, SupplierPhone) ' \
                        f'VALUES ' \
                        f'    ({SupplierKey}, \'{supplier.get_supplier_name()}\', \'{supplier.get_supplier_address()}\', \'{supplier.get_supplier_email()}\', \'{supplier.get_supplier_phone()}\');'
                cursor.execute(query)
                cursor.commit()
                print('\033[1;32mData successfully inserted in Supplier.\033[0m')
            except Exception as e:
                print(f'Error while trying to insert data into \033[1;31mSupplier\033[0m:\n{e}')

    def update_supplier(self, supplier, SupplierKey):
        with self.conn as cursor:
            if validate_key(cursor, SupplierKey):
                try:
                    query = f'UPDATE ' \
                            f'    Supplier ' \
                            f'SET ' \
                            f'    SupplierName = \'{supplier.get_supplier_name()}\', ' \
                            f'    SupplierAddress = \'{supplier.get_supplier_address()}\', ' \
                            f'    SupplierEmail = \'{supplier.get_supplier_email()}\', ' \
                            f'    SupplierPhone = \'{supplier.get_supplier_phone()}\' ' \
                            f'WHERE ' \
                            f'    SupplierKey = {SupplierKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData successfully updated in Supplier.\033[0m')
                except Exception as e:
                    print(f'Error while trying to update data from \033[1;31mSupplier\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no supplier with primary key {SupplierKey}.\033[0m')

    def delete_supplier(self, SupplierKey):
        with self.conn as cursor:
            if validate_key(cursor, SupplierKey):
                try:
                    query = f'DELETE FROM ' \
                            f'    Supplier ' \
                            f'WHERE ' \
                            f'    SupplierKey = {SupplierKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData deleted successfully from Supplier.\033[0m')
                except Exception as e:
                    print(f'Error while trying to delete data from \033[1;31mSupplier\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no supplier with primary key {SupplierKey}.\033[0m')
