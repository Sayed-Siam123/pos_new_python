import json
import sqlite3


class DBProvider:
    def db_connect(self, dbname, dbpath):
        conn = sqlite3.connect(dbpath + "/" + dbname)
        conn.close()
        return "DB created successfully"

    @staticmethod
    def createCustomersTable(dbname):
        conn = sqlite3.connect(dbname)
        print("Opened database successfully")

        conn.execute('''CREATE TABLE IF NOT EXISTS CUSTOMER
            (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            CUSTOMERS          json    NOT NULL,
            STATUS  TEXT DEFAULT 'FALSE');''')
        print("Table created successfully")

        conn.close()

    @staticmethod
    def createProductsTable(dbname):
        conn = sqlite3.connect(dbname)
        print("Opened database successfully")

        conn.execute('''CREATE TABLE IF NOT EXISTS PRODUCT
            (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            PRODUCTS          json    NOT NULL,
            STATUS  TEXT DEFAULT 'FALSE');''')
        print("Table created successfully")

        conn.close()

    @staticmethod
    def PUSHDB_PRODUCT(dbname, data):
        print(str(data[0]["id"]))
        print(dbname)
        conn = sqlite3.connect(dbname)
        print("Opened database successfully")
        c = conn.cursor()
        c.execute("insert into PRODUCT values (?,?,?)", [1, json.dumps(data), "FALSE"])
        conn.commit()
        conn.close()

    @staticmethod
    def PUSHDB_CUSTOMER(dbname, data):
        conn = sqlite3.connect(dbname)
        print("Opened database successfully")
        c = conn.cursor()
        c.execute("select Status from CUSTOMER")
        rows = c.fetchall()
        print(len(rows))

        if len(rows) == 0:
            print("GOT IT")
            c.execute("insert into CUSTOMER values (?,?,?)", [1, json.dumps(data), "FALSE"])
            conn.commit()

        elif rows[0][0] == "TRUE":
            DBProvider.DELETEDB_CUSTOMER(dbname)
            c.execute("insert into CUSTOMER values (?,?,?)", [1, json.dumps(data), "FALSE"])
            conn.commit()
            print("CREATE TO API THEN UPDATE THE DATA IN DB")

        elif rows[0][0] == "FALSE":
            c.execute("UPDATE CUSTOMER SET CUSTOMERS = ? WHERE ID = ?", [json.dumps(data), 1])
            conn.commit()
            print("OK!")
        conn.close()

    @staticmethod
    def DELETEDB_CUSTOMER(dbname):
        conn = sqlite3.connect(dbname)
        print("Opened database successfully")
        c = conn.cursor()
        c.execute("DELETE FROM CUSTOMER")
        conn.commit()
        conn.close()

    @staticmethod
    def getALlCustomer(dbname):
        conn = sqlite3.connect(dbname)
        print("Opened database successfully")
        c = conn.cursor()
        c.execute("select CUSTOMERS from CUSTOMER")
        rows = c.fetchall()
        print(len(rows))
        if(len(rows) == 0):
            return 0
        else:
            datas = json.loads(rows[0][0])
            print(str(datas[0]['id']))
            conn.close()
            return datas

    @staticmethod
    def updateCustomerStatus(dbname,status):
        conn = sqlite3.connect(dbname)
        print("Opened database successfully")
        c = conn.cursor()
        c.execute("UPDATE CUSTOMER SET STATUS = ? WHERE ID = ?", [status, 1])
        conn.commit()
        conn.close()

