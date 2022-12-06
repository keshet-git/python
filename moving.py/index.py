import os

source = 'ron.txt'
destination = 'C:\\Users\\keshe\\OneDrive\\שולחן העבודה\\test.txt'

try:
    if os.path.exists(destination):
        print('ther is already a file there')
    else:
        os.replace(source, destination)
        print(source+' was moved')
except FileNotFoundError:
    print(source+'was not found')