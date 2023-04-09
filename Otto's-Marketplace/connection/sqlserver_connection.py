import pyodbc


class SQLServerConnection:
    def __init__(self, driver='SQL Server Native Client 11.0', server='DESKTOP-46GU3DG', database='OttosMarketplaceDB',
                 username=None, password=None, trusted_connection='yes'):
        try:
            conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};' \
                       f'TRUSTED_CONNECTION={trusted_connection}'
            self.cnxn = pyodbc.connect(conn_str)
            self.cursor = self.cnxn.cursor()
        except pyodbc.Error as e:
            print(f'Error while connecting to the database:\n{e}')
            self.cnxn = None
            self.cursor = None

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.cnxn:
            self.cnxn.close()

    def open_connection(self):
        try:
            if not self.cnxn:
                self.cnxn = pyodbc.connect(self.conn_str)
                self.cursor = self.cnxn.cursor()
        except pyodbc.Error as e:
            print(f'Error while opening the connection:\n{e}')
            self.cnxn = None
            self.cursor = None
