import pandas as pd

data = pd.read_csv('bmi.csv', sep='\t')
connection = sqlite3.connection('mbi.csv')
print(data)