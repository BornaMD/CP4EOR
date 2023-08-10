import numpy as np
import pyodbc as db
import pandas as pd


# how to install pyodbc
#
# conda install -c conda-forge pyodbc
# pip install pyodbc
# pip install --user pyodbc

def connection():
    try:
        # connect to network database
        # change settings for specific user and database
        conn = None
        conn = db.connect("Driver={SQL Server};"
                          "Server=uvtsql.database.windows.net;"
                          "Database=db1;"  # change to your own database
                          "uid=user17;"  # change to your username
                          "pwd=CompEco1234;")

        # if connected do
        if conn is not None:
            print("The connection is established")
            sql_query = 'SELECT * FROM customers;'

            # read table into dataframe
            # make a dataframe with records from table
            dfObj = pd.read_sql_query(sql_query, conn)

            # inspect result
            print(dfObj)

            # read into list
            cursor = conn.cursor()
            cursor.execute(sql_query)

            # put cursor to list
            cursor_list = list(cursor.fetchall())

            # inspect result
            for row in cursor_list:
                print(row)

            # make copy of original data
            # drop table if it already exists
            # sql_string = 'select * into tmp_customers from customers;'
            # conn.execute(sql_string)
            # conn.commit()

    except db.Error as e:
        print(e)

    finally:
        if conn is not None:
            cursor.close()
            conn.close()
            print("The connection is closed")
        else:
            print("No connection established")


def main():
    connection()


main()
