try:
    number = int(input('enter a number to divide: '))
    dinominator = int(input('enter a number to divide by: '))
    result = number / dinominator
    
except ZeroDivisionError as e:
    print(e)
    print("you can't divide by ziro! idiot")
except ValueError as e:
    print(e)
    print('enter only number plz')
except Exception as e:
    print(e)
    print('something went wrong :(')
else:
    print(result)
finally:
    print('this will always execute')