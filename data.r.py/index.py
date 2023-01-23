file = open('index.txt')
data = []

for line in file:
    fields = line.split()
    row_data = [float(x) for x in fields]

    data.append(row_data)

data= array(data)
file.close()

print(data)
    
#arr = loadtxt('index.txt', skiprows=1, dtype=int, delimiter=',')