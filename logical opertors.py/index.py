

temp = int(input("what is the temperature outsid? "))

#if temp >= 0 and temp<=30:
 #   print("the temperature is good today!")
  #  print("go outsid!")
#elif temp < 0 or temp > 30:
 #   print("the temp is bad today!")
  #  print("stay inside")

if not(temp >= 0 and temp <= 30):
    print("the temp is bad today!")
    print("stay inside")
elif not(temp < 0 or temp > 30):
    print("the temperature is good today!")
    print("go outsid!")
   