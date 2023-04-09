from model.Comment import Comment
from connection.sqlserver_connection import SQLServerConnection


def validate_key(cursor, CommentKey):
    try:
        query = f'SELECT ' \
                f'    * ' \
                f'FROM ' \
                f'    Comment ' \
                f'WHERE ' \
                f'    CommentKey = {CommentKey};'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return True
        else:
            return False
    except Exception as e:
        print(f'Error while trying to validate comment key from \033[1;31mComment\033[0m:\n{e}')


def define_key(cursor):
    try:
        query = f'SELECT ' \
                f'    MAX(CommentKey) ' \
                f'FROM ' \
                f'    Comment;'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return row[0] + 1
    except Exception as e:
        print(f'Error while trying to select the greater comment key from \033[1;31mComment\033[0m:\n{e}')


class CommentDAO:
    def __init__(self):
        self.conn = SQLServerConnection()

    def select_all_comments(self):
        try:
            query = 'SELECT ' \
                    '    * ' \
                    'FROM ' \
                    '    Comment;'
            with self.conn as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                return [Comment(*row) for row in rows]
        except Exception as e:
            print(f'Error while trying to select all data from \033[1;31mComment\033[0m:\n{e}')

    def select_comment_by_key(self, CommentKey):
        try:
            query = f'SELECT ' \
                    f'    * ' \
                    f'FROM ' \
                    f'    Comment ' \
                    f'WHERE ' \
                    f'    CommentKey = {CommentKey};'
            with self.conn as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                if row is not None:
                    return Comment(*row)
                else:
                    print(f'\033[1;31mThere is no comment with primary key {CommentKey}.\033[0m')
        except Exception as e:
            print(f'Error while trying to select data from \033[1;31mComment\033[0m with specific key:\n{e}')

    def insert_comment(self, comment):
        with self.conn as cursor:
            CommentKey = define_key(cursor)
            try:
                query = f'INSERT INTO ' \
                        f'    Comment (CommentKey, CommentText, CustomerKey, ProductKey) ' \
                        f'VALUES ' \
                        f'    ({CommentKey}, \'{comment.get_comment_text()}\', {comment.get_customer_key()}, {comment.get_product_key()});'
                cursor.execute(query)
                cursor.commit()
                print('\033[1;32mData successfully inserted in Comment.\033[0m')
            except Exception as e:
                print(f'Error while trying to insert data into \033[1;31mComment\033[0m:\n{e}')

    def update_comment(self, comment, CommentKey):
        with self.conn as cursor:
            if validate_key(cursor, CommentKey):
                try:
                    query = f'UPDATE ' \
                            f'    Comment ' \
                            f'SET ' \
                            f'    CommentText = \'{comment.get_comment_text()}\', ' \
                            f'    CustomerKey = {comment.get_customer_key()}, ' \
                            f'    ProductKey = {comment.get_product_key()} ' \
                            f'WHERE ' \
                            f'    CommentKey = {CommentKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData successfully updated in Comment.\033[0m')
                except Exception as e:
                    print(f'Error while trying to update data from \033[1;31mComment\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no comment with primary key {CommentKey}.\033[0m')

    def delete_comment(self, CommentKey):
        with self.conn as cursor:
            if validate_key(cursor, CommentKey):
                try:
                    query = f'DELETE FROM ' \
                            f'    Comment ' \
                            f'WHERE ' \
                            f'    CommentKey = {CommentKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData deleted successfully from Comment\033[0m')
                except Exception as e:
                    print(f'Error while trying to delete data from \033[1;31mComment\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no comment with primary key {CommentKey}.\033[0m')
