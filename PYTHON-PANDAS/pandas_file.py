import pandas as pd 
import sqlite3


# df=pd.read_csv('housewares.csv')
# df=pd.read_json('sample.json')
# df=pd.read_json('Indian_Number_plates.json',encoding='utf-8') hata veriyor 
# df=pd.read_excel('Book2.xlsx')
connection=sqlite3.connect("sample.db")
df=pd.read_sql_query('SELECT *FROM students',connection)
print(df)
