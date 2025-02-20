# import mysql.connector as mysql
# import pandas as pd

# con = {
#     'name': 'fidelity',
#     'user': 'root',
#     'password': 'Shivam@123',
#     'host': 'localhost',
#     'port': 3306
# }

# try:
#     conn = mysql.connect(
#         host=con['host'],
#         user=con['user'],
#         password=con['password'],
#         database=con['name']
#     )
#     cursor = conn.cursor()
#     query = "SELECT * FROM tips"
#     cursor.execute(query)
#     rows = cursor.fetchall()
#     column_names = [desc[0] for desc in cursor.description]
#     df = pd.DataFrame(rows, columns=column_names)
    
#     print(df)
#     cursor.close()
#     conn.close()

# except mysql.Error as e:
#     print("Error:", e)




import pandas as pd
from sqlalchemy import create_engine
import urllib.parse

con = {
    'name': 'fidelity',
    'user': 'root',
    'password': urllib.parse.quote_plus('Shivam@123'),
    'host': 'localhost',
    'port': 3306
}

try:
    engine = create_engine(
        f"mysql+pymysql://{con['user']}:{con['password']}@{con['host']}:{con['port']}/{con['name']}"
    )
    df = pd.read_sql("SELECT * FROM tips", con=engine)
    print(df)
    df.to_sql('tips_backup', con=engine, if_exists='replace', index=False)
    print("Data stored in 'tips_backup' table successfully!")

except Exception as e:
    print("Error:", e)
