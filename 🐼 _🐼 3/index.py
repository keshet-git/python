import pandas as pd

column = ['Elon', 'Jeff', 'Steve']
titled_column = {"name": column,
                 "height": [1.67, 1.9, 0.25],
                "age": [21, 43, 70]}
data = pd.DataFrame(titled_column)
select_column=data['age'][0]
bmi = []

for i in range(len(data)):
    bmi_score = data['age'][i]/(data['height'][i]**2)
    bmi.append(bmi_score)


data['bmi'] = bmi

data.to_csv('bmi.bd', index=False, sep='\t')

print(data)