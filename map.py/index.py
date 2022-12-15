store= [("shirt",20.00),
        ("pants",25.00),
        ("jacket",50.00),
        ("socks",10.00)]

to_euros = lambda data: (data[0],data[1]*0.82)
to_dollars = lambda data: (data[0],data[1]/0.82)

store_dollers = list(map(to_dollars, store))

for i in store_dollers:
    print(i)