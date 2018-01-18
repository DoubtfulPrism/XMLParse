import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def create_order(conn, order):
    sql = '''INSERT INTO orders(ATGOrderNumber,CustomerID)
              VALUES (?,?)'''
    cur = conn.cursor()
    cur.execute(sql, order)
    return cur.lastrowid

def main():
    database = "/home/doug/PycharmProjects/XMLParse/orders.db"
    conn = create_connection(database)
    with conn:
        order =('o356451','00U3PJ1E');
        orderid =create_order(conn, order)

if __name__ == '__main__':
    main()