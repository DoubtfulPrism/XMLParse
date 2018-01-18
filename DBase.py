import sqlite3
from sqlite3 import Error

# def create_connection(db_file):
#     try:
#         conn =  sqlite3.connect(db_file)
#         print(sqlite3.version)
#     except Error as e:
#         print(e)
#     finally:
#         conn.close()
#
#
# if __name__=='__main__':
#     create_connection("/home/doug/PycharmProjects/XMLParse/orders.db")


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None


def createTable(conn, create_table_sql):
    try:
        c= conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = "/home/doug/PycharmProjects/XMLParse/orders.db"

    SQLCreateTableorders = """CREATE TABLE IF NOT EXISTS orders (
                        ATGOrderNumber nvarchar NOT NULL PRIMARY KEY,
                        CustomerID nvarchar NOT NULL
                        );"""
    conn = create_connection(database)
    if conn is not None:
        createTable(conn, SQLCreateTableorders)
    else:
        print("error! cannot create database connection.")


if __name__=='__main__':
    main()

