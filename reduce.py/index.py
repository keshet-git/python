import functools

#letters = ["H","E","L","L","O"]
#word = functools.reduce(lambda x, y,:x + y, letters)
#print(word)

fectorial = [5,4,3,2,1]
result= functools.reduce(lambda x, y,:x * y, fectorial)
print(result)