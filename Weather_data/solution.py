import requests 
import pandas as pd
import sqlite3 
import os

url = 'https://api.open-meteo.com/v1/forecast'

print('Hi')
params = {

    'latitude' : '39.7392',
    'longitude' : '-104.9847',
    'hourly' : 'temperature_2m',
    'start_date' : '2025-08-23',
    'end_date' : '2025-08-30'
}

response = requests.get(url, params = params)

print('Hi2')
data = response.json()

data_df = pd.DataFrame(data)

print(data_df.shape)

# Transpose the dataframe to make columns rows and rows columns

print("Original shape:", data_df.shape)


data_df = data_df['hourly']

print("Original hourly data structure:")
print(data_df.head(5))



converted_data=pd.DataFrame({'time':data_df.loc['time'], 'Temp':data_df.loc['temperature_2m']})
print(converted_data.head(5))

converted_data.to_csv('converted_data.csv')

converted_data['date'] = converted_data['time'].str[:10]
converted_data['hour'] = converted_data['time'].str[11:13].astype(int)

print(converted_data.head(5))

print(converted_data.dtypes)



converted_data.loc[2, 'Temp'] = None

converted_data.loc[4, 'Temp'] = None

print(converted_data.head())

print(converted_data.info())

# converted_data['Temp'].fillna(converted_data["Temp"].expanding().mean().shift(1), inplace=True)

# converted_data['T_from_previous'] = converted_data['Temp'].fillna(
#     converted_data['Temp']
#     .expanding()
#     .mean()
#     .shift(1)
# )

tmp = converted_data['Temp'].copy()

for i in range(len(tmp)):
    if pd.isna(tmp.iloc[i]):
        if i == 0:
            tmp.iloc[i] = None
        else:
            tmp.iloc[i] = tmp.iloc[:i].mean()

converted_data['T_from_avg'] = tmp
converted_data['T_avg'] = converted_data['Temp'].fillna(
    converted_data['Temp']
    .expanding()
    .mean()
    .shift(1)
    )
converted_data['avg'] = converted_data['T_avg'].mean()

converted_data['avg_grpb'] = converted_data.groupby('date')['T_avg'].transform('mean')

print(converted_data.head(5))
converted_data.to_csv('converted_data.csv')


conn = sqlite3.connect(":memory:")

converted_data.to_sql('temperature', conn, index = False, if_exists = 'replace')
query = '''
    with cte as (
        select 
            date, 
            max(Temp) as T_max, 
            avg(Temp) as T_avg
        from temperature 
        group by date
        order by date
    )
    select *,
        Lag(T_max) over (order by date) as previous_day_T_max
    from cte 
'''


result = pd.read_sql(query, conn).reset_index(drop=True)

print(result)

directory = '/Users/doni/Desktop/Max/projects/Weather_data/result'
file_name = 'sql_table.csv'

os.makedirs(directory, exist_ok = True)

result.to_csv(os.path.join(directory, file_name), index = False)