import pandas as pd
from pandas_profiling import ProfileReport
df=pd.read_csv(r"C:\Users\UMAPRIYA\Desktop\Employee_Salaries_2022\EDA\Employee_Salaries_-_2022_EDA.csv")
print(df.head())
profile = ProfileReport(df,title='Employee_Salaries_-_2022_EDA')
profile.to_file('Employee_Salaries_-_2022_EDA.html')


