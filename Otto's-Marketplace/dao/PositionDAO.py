from model.Position import Position
from connection.sqlserver_connection import SQLServerConnection


def validate_key(cursor, PositionKey):
    try:
        query = f'SELECT ' \
                f'    * ' \
                f'FROM ' \
                f'    Position ' \
                f'WHERE ' \
                f'    PositionKey = {PositionKey};'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return True
        else:
            return False
    except Exception as e:
        print(f'Error while trying to validate position key from \033[1;31mPosition\033[0m:\n{e}')


def define_key(cursor):
    try:
        query = f'SELECT ' \
                f'    MAX(PositionKey) ' \
                f'FROM ' \
                f'    Position;'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return row[0] + 1
    except Exception as e:
        print(f'Error while trying to select the greater position key from \033[1;31mPosition\033[0m:\n{e}')


class PositionDAO:
    def __init__(self):
        self.conn = SQLServerConnection()

    def select_all_positions(self):
        try:
            query = 'SELECT ' \
                    '    * ' \
                    'FROM ' \
                    '    Position;'
            with self.conn as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                return [Position(*row) for row in rows]
        except Exception as e:
            print(f'Error while trying to select all data from \033[1;31mPosition\033[0m:\n{e}')

    def select_position_by_key(self, PositionKey):
        try:
            query = f'SELECT ' \
                    f'    * ' \
                    f'FROM ' \
                    f'    Position ' \
                    f'WHERE ' \
                    f'    PositionKey = {PositionKey};'
            with self.conn as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                if row is not None:
                    return Position(*row)
                else:
                    print(f'\033[1;31mThere is no position with primary key {PositionKey}.\033[0m')
        except Exception as e:
            print(f'Error while trying to select data from \033[1;31mPosition\033[0m with specific key:\n{e}')

    def insert_position(self, position):
        with self.conn as cursor:
            PositionKey = define_key(cursor)
            try:
                query = f'INSERT INTO ' \
                        f'    Position (PositionKey, PositionName) ' \
                        f'VALUES ' \
                        f'    ({PositionKey}, \'{position.get_position_name()}\');'
                cursor.execute(query)
                cursor.commit()
                print('\033[1;32mData successfully inserted in Position.\033[0m')
            except Exception as e:
                print(f'Error while trying to insert data into \033[1;31mPosition\033[0m:\n{e}')

    def update_position(self, position, PositionKey):
        with self.conn as cursor:
            if validate_key(cursor, PositionKey):
                try:
                    query = f'UPDATE ' \
                            f'    Position ' \
                            f'SET ' \
                            f'    PositionName = \'{position.get_position_name()}\' ' \
                            f'WHERE ' \
                            f'    PositionKey = {PositionKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData successfully updated in Position.\033[0m')
                except Exception as e:
                    print(f'Error while trying to update data from \033[1;31mPosition\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no position with primary key {PositionKey}.\033[0m')

    def delete_position(self, PositionKey):
        with self.conn as cursor:
            if validate_key(cursor, PositionKey):
                try:
                    query = f'DELETE FROM ' \
                            f'    Position ' \
                            f'WHERE ' \
                            f'    PositionKey = {PositionKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData deleted successfully from Position.\033[0m')
                except Exception as e:
                    print(f'Error while trying to delete data from \033[1;31mPosition\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no position with primary key {PositionKey}.\033[0m')
