
friends = [("Rachel",19),
            ("Monical",18),
            ("Pheoebe",17),
            ("Joey",16),
            ("Chandler",21),
            ("Ross",20)]

age = lambda data:data[1] >= 18

drinking_budddies = list(filter(age, friends))

for i in drinking_budddies:
    print(i)