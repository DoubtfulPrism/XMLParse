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
                        CustomerID nvarchar NOT NULL,
                        SalesChannel text NOT NULL ,
                        Origin text NOT NULL ,
                        Webstore text NOT NULL,
                        Language text NOT NULL,
                        SaleCurrency text NOT NULL,
                        TransferCurrency text NOT NULL,
                        DistributionCentre text NOT NULL,
                        OrderTotal REAL  NOT NULL ,
                        DateEntered, INT NOT NULL,
                        Source text NOT NULL,
                        IsStaffOrder BOOLEAN NOT NULL,
                        IsGift BOOLEAN NOT NULL);"""

    SQLCreateTableAddresses = """CREATE TABLE IF NOT EXISTS Addresses (ATGOrderNumber nvarchar PRIMARY KEY,
                                 Type text NOT NULL,
                                 ShipToStoreID nvarchar,
                        FirstName text NOT NULL,
                        LastName text,
                        Address1 text NOT NULL,
                        Address2 text,
                        City text NOT NULL,
                        StateProvince text,
                        PostalCode text NOT NULL,
                        Country text NOT NULL,
                        ContactPhone INT,
                        ContactEmail text,
                                  FOREIGN KEY (orders_ATGOrderNumber) REFERENCES orders (ATGOrderNumber));"""

    SQLCreateTableShippingGroup ="""CREATE TABLE IF NOT EXISTS ShippingGroup (ATGOrderNumber nvarchar PRIMARY KEY,
                                    GWSOrderNumber INT NOT NULL,
                        ShippingTotal REAL NOT NULL,
                        IsShippingTotalTaxInclusive BOOLEAN NOT NULL,
                        ShippingMethod text NOT NULL,
                        OrderType text NOT NULL,
                                    FOREIGN KEY (orders_ATGOrderNumber) REFERENCES orders (ATGOrderNumber)    );"""

    SQLCreateTableShippingTax ="""CREATE TABLE IF NOT EXISTS ShippingTax(GWSOrderNumber INT NOT NULL PRIMARY KEY ,
                                  Type text NOT NULL, 
                        Rate REAL  NOT NULL,
                        Amount REAL  NOT NULL,
                                  FOREIGN KEY (ShippingGroup_GWSOrderNumber) REFERENCES ShippingGroup (GWSOrderNumber));"""

    SQLCreateTableOrderDetails ="""CREATE TABLE IF NOT EXISTS OrderDetails(GWSOrderNumber INT NOT NULL PRIMARY KEY,
                                    ProductCode  INT NOT NULL,
                        Description text NOT NULL,
                        LineNumber int NOT NULL ,
                        QuantityOrdered INT NOT NULL,
                        RetailPrice REAL NOT NULL,
                        SalesPrice REAL NOT NULL,
                        TransferPrice REAL NOT NULL,
                        IsTaxInclusive BOOLEAN NOT NULL,
                        IsBundleHeader BOOLEAN NOT NULL,
                                    FOREIGN KEY (ShippingGroup_GWSOrderNumber) REFERENCES ShippingGroup (GWSOrderNumber)        );"""

    SQLCreateTableTaxes = """CREATE TABLE IF NOT EXISTS Taxes(GWSOrderNumber INT NOT NULL PRIMARY KEY,
                              LineNumber INT NOT NULL,
                        Type text NOT NULL,
                        Rate REAL NOT NULL,
                        Amount REAL NOT NULL,
                              FOREIGN KEY (OrderDetails_GWSOrderNumber) REFERENCES OrderDetails (GWSOrderNumber));"""

    SQLCreateTablePayment = """CREATE TABLE IF NOT EXISTS  Payment(ATGOrderNumber nvarchar PRIMARY KEY,
                                Type text NOT NULL,
                        Amount REAL NOT NULL,
                        Reference NVARCHAR NOT NULL,
                        PaidInStoreID TEXT,
                                FOREIGN KEY (orders_ATGOrderNumber) REFERENCES orders (ATGOrderNumber));"""

    conn = create_connection(database)
    if conn is not None:
        createTable(conn, SQLCreateTableorders)
        createTable(conn, SQLCreateTableAddresses)
        createTable(conn, SQLCreateTableShippingGroup)
        createTable(conn, SQLCreateTableShippingTax)
        createTable(conn, SQLCreateTableOrderDetails)
        createTable(conn, SQLCreateTableTaxes)
        createTable(conn, SQLCreateTablePayment)
    else:
        print("error! cannot create database connection.")


if __name__=='__main__':
    main()

