import pandas as pd
import sqlite3

data = pd.read_csv('bmi.csv', sep='\t')
connaction = sqlite3.connect('bmi.db')

bmi_data = pd.read_sql('select * from bmi', connaction)
print(bmi_data)