import pandas as pd

column = ['Elon', 'Jeff', 'Steve']
titled_column = {"name": column,
                 "height": [1.67, 1.9, 0.25],
                "age": [21, 43, 70]}
data = pd.DataFrame(titled_column)
select_column=data['age'][0]
print(select_column)