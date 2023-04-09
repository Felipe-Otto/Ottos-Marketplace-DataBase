from model.Employee import Employee
from connection.sqlserver_connection import SQLServerConnection


def validate_key(cursor, EmployeeKey):
    try:
        query = f'SELECT ' \
                f'    * ' \
                f'FROM ' \
                f'    Employee ' \
                f'WHERE ' \
                f'    EmployeeKey = {EmployeeKey};'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return True
        else:
            return False
    except Exception as e:
        print(f'Error while trying to validate employee key from \033[1;31mEmployee\033[0m:\n{e}')


def define_key(cursor):
    try:
        query = f'SELECT ' \
                f'    MAX(EmployeeKey) ' \
                f'FROM ' \
                f'    Employee;'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return row[0] + 1
    except Exception as e:
        print(f'Error while trying to select the greater employee key from \033[1;31mEmployee\033[0m:\n{e}')


class EmployeeDAO:
    def __init__(self):
        self.conn = SQLServerConnection()

    def select_all_employees(self):
        try:
            query = 'SELECT ' \
                    '    * ' \
                    'FROM ' \
                    '    Employee;'
            with self.conn as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                return [Employee(*row) for row in rows]
        except Exception as e:
            print(f'Error while trying to select all data from \033[1;31mEmployee\033[0m:\n{e}')

    def select_employee_by_key(self, EmployeeKey):
        try:
            query = f'SELECT ' \
                    f'    * ' \
                    f'FROM ' \
                    f'    Employee ' \
                    f'WHERE ' \
                    f'    EmployeeKey = {EmployeeKey};'
            with self.conn as cursor:
                cursor.execute(query)
                row = cursor.fetchone()
                if row is not None:
                    return Employee(*row)
                else:
                    print(f'\033[1;31mThere is no employee with primary key {EmployeeKey}.\033[0m')
        except Exception as e:
            print(f'Error while trying to select data from \033[1;31mEmployee\033[0m with specific key:\n{e}')

    def insert_employee(self, employee):
        with self.conn as cursor:
            EmployeeKey = define_key(cursor)
            try:
                query = f'INSERT INTO ' \
                        f'    Employee (EmployeeKey, FirstName, LastName, EmployeeAddress, EmployeeEmail, EmployeePhone, PositionKey) ' \
                        f'VALUES ' \
                        f'    ({EmployeeKey}, \'{employee.get_first_name()}\', \'{employee.get_last_name()}\', \'{employee.get_employee_address()}\', \'{employee.get_employee_email()}\', \'{employee.get_employee_phone()}\', {employee.get_position_key()});'
                cursor.execute(query)
                cursor.commit()
                print('\033[1;32mData successfully inserted in Employee.\033[0m')
            except Exception as e:
                print(f'Error while trying to insert data into \033[1;31mEmployee\033[0m:\n{e}')

    def update_employee(self, employee, EmployeeKey):
        with self.conn as cursor:
            if validate_key(cursor, EmployeeKey):
                try:
                    query = f'UPDATE ' \
                            f'    Employee ' \
                            f'SET ' \
                            f'    FirstName = \'{employee.get_first_name()}\', ' \
                            f'    LastName = \'{employee.get_last_name()}\', ' \
                            f'    EmployeeAddress = \'{employee.get_employee_address()}\', ' \
                            f'    EmployeeEmail = \'{employee.get_employee_email()}\', ' \
                            f'    EmployeePhone = \'{employee.get_employee_phone()}\', ' \
                            f'    PositionKey = {employee.get_position_key()} '\
                            f'WHERE ' \
                            f'    EmployeeKey = {EmployeeKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData successfully updated in Employee.\033[0m')
                except Exception as e:
                    print(f'Error while trying to update data from \033[1;31mEmployee\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no employee with primary key {EmployeeKey}.\033[0m')

    def delete_employee(self, EmployeeKey):
        with self.conn as cursor:
            if validate_key(cursor, EmployeeKey):
                try:
                    query = f'DELETE FROM ' \
                            f'    Employee ' \
                            f'WHERE ' \
                            f'    EmployeeKey = {EmployeeKey};'
                    cursor.execute(query)
                    cursor.commit()
                    print('\033[1;32mData deleted successfully from Employee\033[0m')
                except Exception as e:
                    print(f'Error while trying to delete data from \033[1;31mEmployee\033[0m:\n{e}')
            else:
                print(f'\033[1;31mThere is no employee with primary key {EmployeeKey}.\033[0m')
