def create_database(name):
    QUERY = fr'CREATE DATABASE {name};'
    return QUERY


def create_customers_data(table_name):
    QUERY = f"""CREATE TABLE {table_name}
                (customer_id nvarchar(10) PRIMARY KEY,
                 company_name nvarchar(100),
                 contact_name - nvarchar(50));"""
    return QUERY


def create_employees_data(table_name):
    QUERY = f"""CREATE TABLE {table_name}
                (employee_id int PRIMARY KEY,
                 first_name nvarchar(100),
                 last_name nvarchar(100),
                 title nvarchar(100),
                birth_data date, 
                notes nvarchar(1000));"""
    return QUERY


def create_orders_data(table_name, references_table =None, references_column=None):
    QUERY = f"""CREATE TABLE {table_name}
                (order_id int PRIMARY KEY,
                 customer_id nvarchar(10) REFERENCES {references_table} ({references_column}),
                 employee_id int REFERENCES {references_table} ({references_column}), 
                 order_date date,
                ship_city nvarchar(100));"""
    return QUERY