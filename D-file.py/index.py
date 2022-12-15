import os
import shutil

path = 'fol'

try:
    #os.remove(path)
    #os.rmdiree(path)
    shutil.rmtree(path)
except FileNotFoundError:
    print('the file was not found')
except PermissionError:
    print('you do nat have permission to delete that')
except OSError:
    print('you cannot delete that using that functionn')
else:
    print(path+' was deleted')