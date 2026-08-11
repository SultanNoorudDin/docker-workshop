import sys
import pandas as pd 


print('arguments', sys.argv)
df = pd.DataFrame({"day": [1, 2], "num_of_passengers": [3, 4]})
month = int(sys.argv[1])

df['month'] = month

df.to_parquet(f'output_month={month}.parquet')
print(df)
print(f'Running pipeline for month, month = {month}')