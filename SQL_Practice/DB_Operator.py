import os

import pyodbc
from dotenv import load_dotenv

import SQL_Queries


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

class MSSQLOperator:

    def __init__(self, conn_obj):
        self.conn = conn_obj
        self.conn_cursor = self.conn.cursor()


    def create_database(self, database_name):
        SQLCommand = SQL_Queries.create_database(database_name)
        try:
            self.conn.execute(SQLCommand)
        except pyodbc.ProgrammingError as ex:
            print(ex)

            return False
        else:

            print(f'База данных {database_name} успешно создана')