import pandas as pd

# dates = pd.date_range('2022-01-01', periods=6, freq='Y')
# print("Dates are: ", dates)

data=pd.read_csv('police.csv')
# print(data.head(6))
# print(data.isnull().sum())
# drop = data([''], axis=0, inplace=True)
# data['driver_gender'].fillna(data['driver_gender'].mean, inplace = True)
# data.loc[:5, ['driver_gender', 'stop_outcome']]
# data.loc
# print(data)


# print(data.duplicated().sum())

# def get_ages(driver_age_raw):
#     if pd.isna(driver_age_raw):
#         return None 
#     return 2022 - int(driver_age_raw)

# data['driver_age'] = data['driver_age_raw'].apply(get_ages)
# print(data)

# data['driver_age'] = data['driver_age_raw'].apply(lambda x: 2022 - int(x) if pd.notna(x) else None)
# print(data)


# data['driver_age_raw'] = pd.qcut(data['driver_age_raw'], q=6)
# print(data)

# pd.crosstab(data['stop_time'], data['stop_date'])
# print(data)

