"""Запрос на создание базы данных"""


def create_database(name):
    QUERY = fr'CREATE DATABASE {name};'
    return QUERY


"""Запрос на создание таблицы customers_data"""


def create_customers_data(table_name):
    QUERY = f"""CREATE TABLE {table_name}
                (customer_id nvarchar(10) PRIMARY KEY,
                 company_name nvarchar(100),
                 contact_name nvarchar(50));"""
    return QUERY


"""Запрос на создание таблицы employees_data"""


def create_employees_data(table_name):
    QUERY = f"""CREATE TABLE {table_name}
                (employee_id int PRIMARY KEY IDENTITY(1,1),
                 first_name nvarchar(100),
                 last_name nvarchar(100),
                 title nvarchar(100),
                birth_data date, 
                notes nvarchar(1000));"""
    return QUERY


"""Запрос на создание таблицы orders_data"""


def create_orders_data(table_name):
    QUERY = fr"""CREATE TABLE {table_name}
                (order_id int PRIMARY KEY,
                 customer_id nvarchar(10) REFERENCES customers_data (customer_id),
                 employee_id int REFERENCES employees_data (employee_id), 
                 order_date date,
                ship_city nvarchar(100));"""
    return QUERY


def fill_table_customers(table_name, data_to_fill):
    QUERY = fr"""INSERT INTO {table_name}(customer_id, company_name, contact_name)
                VALUES
                ('{data_to_fill[0]}',
                '{data_to_fill[1].replace("'", "''")}',
                '{data_to_fill[2].replace("'", "''")}'
                 );""" #'{customer['company_name'].replace("'", "''")}'
    return QUERY

# def fill_table_customers(table_name, data_to_fill):               Не работает метод. Но очень хотел его исполнить!!!!
#     QUERY = fr"""INSERT INTO {table_name}(customer_id, company_name, contact_name)
#                 VALUES(?, ?, ?)""", [data_to_fill[0], data_to_fill[1],
#                                      data_to_fill[2]]
#     return QUERY

def fill_table_employees_data(table_name, data_to_fill):
    QUERY = fr"""INSERT INTO {table_name}(first_name, last_name, title, birth_data, notes)
                VALUES
                (
                 '{data_to_fill[0].replace("'", "''")}',
                 '{data_to_fill[1].replace("'", "''")}',
                 '{data_to_fill[2].replace("'", "''")}',
                 '{data_to_fill[3].replace("'", "''")}',
                 '{data_to_fill[4].replace("'", "''")}'
                  );"""
    return QUERY
#
#
def fill_orders_data(table_name, data_to_fill):
    QUERY = fr"""INSERT INTO {table_name}(order_id, customer_id, employee_id, order_date, ship_city)
                VALUES
                ({data_to_fill[0].replace("'", "''")},
                 '{data_to_fill[1].replace("'", "''")}',
                 {(data_to_fill[2].replace("'", "''"))},
                 '{data_to_fill[3].replace("'", "''")}',
                 '{data_to_fill[4].replace("'", "''")}'
                );"""
    return QUERY
