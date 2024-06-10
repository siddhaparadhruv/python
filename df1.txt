# pip install pandas
# pip install openpyxl
# pip install sqlalchemy
# pip install mysql-connector-python

import pandas as pd
import sqlalchemy as sql

df = pd.read_excel("mydata.xlsx")
#print(df)

#help(df.to_sql)
 
# Create the engine to connect to the PostgreSQL database
engine = sql.create_engine('mysql+mysqlconnector://root:root@localhost:3306/dummy_db')
#print(engine)

x = df[['name','city']].to_sql("test1",engine,index=False,if_exists="append")
print(x)
#print(df)