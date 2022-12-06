import os

#path = "C:\\Users\\keshe\\OneDrive\\שולחן העבודה\\New Text Document(.txt)"
path ="C:\\Users\\keshe\\OneDrive\\שולחן העבודה\\folder"
if os.path.exists(path):
    print('this path exists')
    if os.path.isfile(path):
        print('this is a file')

    elif os.path.isdir(path):
        print('thes is a directory')
else:
    print("this path doesn't exists")