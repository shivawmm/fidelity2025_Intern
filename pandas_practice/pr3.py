import pandas as pd


data=pd.read_csv('tips.csv')
# print(data.head(6))
# print(data['sex'].unique())
# print(data[['sex', 'tip']].isnull().sum())
# data = data.dropna(subset=['sex', 'tip'])

# avg_tips = data.groupby('sex')['tip'].mean()
# print(avg_tips)
# total_tips = data.groupby('sex')['tip'].sum()
# print(total_tips)
# tip_counts = data.groupby('sex')['tip'].count()
# print(tip_counts)

# print(data[['size', 'tip']].isnull().sum())
# data = data.dropna(subset=['size', 'tip'])
# print("")
# avg_tip_by_size = data.groupby('size')['tip'].mean()
# print(avg_tip_by_size)
# print("")
# correlation = data[['size', 'tip']].corr()
# print(correlation)

# data['smoker'] = data['smoker'].apply(lambda x: 1 if x.lower() == 'yes' else 0)
# print(data.head(5))
# data.to_csv('tips.csv', index=False)
# print("Dataset saved successfully as 'tips.csv'")

# data.to_sql('tips', con=mysql.connect('tips.db'), if_exists='replace')

from sqlalchemy import create_engine
import urllib.parse
db={
    'name': 'fidelity',
    'user': 'root',
    'password': urllib.parse.quote_plus('Shivam@123'),
    'host': 'localhost',
    'port': 3306
}

engine = create_engine(f"mysql+pymysql://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['name']}")

data.to_sql('tips', con=engine, if_exists='replace', index=False)
print("Data saved successfully in MySQL database")




