def hello(**kwargs):
   # print('hello ' + kwargs['first'] +' '+ kwargs['last'])
   print('Hello',end=' ')
   for key,value in kwargs.items():
    print(value,end=' ')

hello(title='lyde', first='keshet',middel='rychel', last='avrahami')