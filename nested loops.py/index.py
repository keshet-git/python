rows = int(input('how mani rows?: '))
columns = int(input('how meny columns?: '))
symbol = input('enter a symbol to use: ')

for i in range(rows):
    for j in range(columns):
        print(symbol, end='')
    print()