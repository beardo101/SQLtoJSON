import pyodbc
import json

###sample connection
SERVER = 'US22-1\SQLEXPRESS'
DATABASE = 'AdventureWorksLT2022'
USERNAME = 'sa'
PASSWORD = '123qwe'

connectionString = (f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                    f'SERVER={SERVER};'
                    f'DATABASE={DATABASE};'
                    f'UID={USERNAME};'
                    f'PWD={PASSWORD}')

conn = pyodbc.connect(connectionString)

sql_query = """
select * from SalesLT.Customer
 """

cursor = conn.cursor()
cursor.execute(sql_query)

###fetchall creates a list based on query
records = cursor.fetchall()


###create a python dictionary based on the results of sql query
customers_dict= {}
for record in records:
    customers_dict[record.CustomerID] = {'email': record.EmailAddress,
                                         'password': record.PasswordSalt,
                                         'company': record.CompanyName,
                                         'first_name': record.FirstName,
                                         'last_name': record.LastName,}

###convert from python dictionary to json file
with open("sample.json", "w") as outfile:
    json.dump(customers_dict, outfile)

cursor.close()
conn.close()

