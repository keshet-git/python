age = int(input('how old are you?: '))

if  age == 100:
    print("you are a sentury old!")
elif age >= 18:
    print('You are an adult!')
elif age < 0:
    print("you haven't been born yet!")
else:
    print(('you are a child!'))