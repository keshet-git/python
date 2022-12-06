try:
    with open('test.tx') as file:
        print(file.read())
except FileNotFoundError:
    print('that file was not found :(')