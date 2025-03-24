import os

import pyodbc
from dotenv import load_dotenv

import SQL_Queries

"""Класс соединения с базой данных"""


class ConnectDB:
    @classmethod
    def connect_to_db(cls, driver, server, pad_database, user, password):
        connection_string = f'''DRIVER={driver};
                        SERVER={server};
                        DATABASE={pad_database};
                        UID={user};
                        PWD={password};'''
        try:
            conn = pyodbc.connect(connection_string)
            conn.autocommit = True
        except pyodbc.ProgrammingError as ex:
            print(ex)
        else:
            return conn

    @classmethod
    def close_connection(cls, conn_obj):
        conn_obj.close()


"""Оператор для работы с базой данных SQL"""


class MSSQLOperator:

    def __init__(self, conn_obj):
        self.conn = conn_obj
        self.conn_cursor = self.conn.cursor()

    """Создание базы данных через sql команды"""

    def create_database(self, database_name):
        SQLCommand = SQL_Queries.create_database(database_name)
        try:
            self.conn.execute(SQLCommand)
        except pyodbc.ProgrammingError as ex:
            print(ex)

            return False
        else:

            print(f'База данных {database_name} успешно создана')

    """Создание таблицы через sql команды"""

    def create_table(self, database_name, sql_query, table_name):
        self.conn_cursor.execute(f'USE {database_name}')
        SQLQuery = sql_query(table_name)
        try:
            self.conn_cursor.execute(SQLQuery)
        except pyodbc.ProgrammingError as exPE:
            print(exPE)

            return False
        except pyodbc.OperationalError as exOE:
            print(exOE)

            return False
        else:
            print(f'Таблица {table_name} успешно создана!')

            return True


if __name__ == '__main__':
    load_dotenv()

    DRIVER = os.getenv('MS_SQL_DRIVER')
    SERVER = os.getenv('MS_SQL_SERVER')
    WORK_DATABASE = os.getenv('MS_SQL_DATABASE')
    PAD_DATABASE = os.getenv('MS_PAD_DATABASE')
    USER = os.getenv('MS_SQL_USER')
    PASSWORD = os.getenv('MS_SQL_KEY')

    my_conn = ConnectDB.connect_to_db(driver=DRIVER, server=SERVER, pad_database=PAD_DATABASE, user=USER,
                                      password=PASSWORD)
    my_db_operator = MSSQLOperator(my_conn)
    my_db_operator.create_database(WORK_DATABASE)
    my_db_operator.create_table(WORK_DATABASE, SQL_Queries.create_customers_data, 'customers_data')
    my_db_operator.create_table(WORK_DATABASE, SQL_Queries.create_employees_data, 'employees_data')
    my_db_operator.create_table(WORK_DATABASE, SQL_Queries.create_orders_data, 'orders_data')
