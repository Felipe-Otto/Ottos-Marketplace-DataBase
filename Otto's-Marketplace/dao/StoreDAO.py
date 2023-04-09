from model.Store import Store
from connection.sqlserver_connection import SQLServerConnection


def validate_key(cursor, StoreKey):
    try:
        query = f'SELECT ' \
                f'    * ' \
                f'FROM ' \
                f'    Store ' \
                f'WHERE ' \
                f'    StoreKey = {StoreKey};'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return True
        else:
            return False
    except Exception as e:
        print(f'Error while trying to validate store key from \033[1;31mStore\033[0m:\n{e}')


def define_key(cursor):
    try:
        query = f'SELECT ' \
                f'    MAX(StoreKey) ' \
                f'FROM ' \
                f'    Store;'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return row[0] + 1
    except Exception as e:
        print(f'Error while trying to select the greater store key from \033[1;31mStore\033[0m:\n{e}')


class StoreDAO:
    def __init__(self):
        self.conn = SQLServerConnection()

    def select_all_stores(self):
        try:
            query = 'SELECT ' \
                    '    * ' \
                    'FROM ' \
                    '    Store;'
            with self.conn as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                return [Store(*row) for row in rows]
        except Exception as e:
            print(f'Error while trying to select all data from \033[1;31mStore\033[0m:\n{e}')

    def select_store_by_key(self, StoreKey):
        try:
            query = f'SELECT ' \
                    f'    * ' \
                    f'FROM ' \
                    f'    Store ' \
                    f'WHERE ' \
                    f'    StoreKey = {StoreKey};'
            with self.conn as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                if row is not None:
                    return Store(*row)
                else:
                    print(f'\033[1;31mThere is no store with primary key {StoreKey}.\033[0m')
        except Exception as e:
            print(f'Error while trying to select data from \033[1;31mStore\033[0m with specific key:\n{e}')

    def insert_store(self, store):
        with self.conn as cursor:
            StoreKey = define_key(cursor)
            try:
                query = f'INSERT INTO ' \
                        f'    Store (StoreKey, StoreName, StoreAddress, StorePhone) ' \
                        f'VALUES ' \
                        f'    ({StoreKey}, \'{store.get_store_name()}\', \'{store.get_store_address()}\', \'{store.get_store_phone()}\');'
                cursor.execute(query)
                cursor.commit()
                print('\033[1;32mData successfully inserted in Store.\033[0m')
            except Exception as e:
                print(f'Error while trying to insert data into \033[1;31mStore\033[0m:\n{e}')

    def update_store(self, store, StoreKey):
        with self.conn as cursor:
            if validate_key(cursor, StoreKey):
                try:
                    query = f'UPDATE ' \
                            f'    Store ' \
                            f'SET ' \
                            f'    StoreName = \'{store.get_store_name()}\', ' \
                            f'    StoreAddress = \'{store.get_store_address()}\', ' \
                            f'    StorePhone = \'{store.get_store_phone()}\' ' \
                            f'WHERE ' \
                            f'    StoreKey = {StoreKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData successfully updated in Store.\033[0m')
                except Exception as e:
                    print(f'Error while trying to update data from \033[1;31mStore\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no store with primary key {StoreKey}.\033[0m')

    def delete_store(self, StoreKey):
        with self.conn as cursor:
            if validate_key(cursor, StoreKey):
                try:
                    query = f'DELETE FROM ' \
                            f'    Store ' \
                            f'WHERE ' \
                            f'    StoreKey = {StoreKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData deleted successfully from Store.\033[0m')
                except Exception as e:
                    print(f'Error while trying to delete data from \033[1;31mStore\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no store with primary key {StoreKey}.\033[0m')
