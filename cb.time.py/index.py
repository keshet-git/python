import time

my_time = int(input("Enter the time in seconds"))

for x in range(my_time, 0,-1):
    secondse = x % 60
    mintes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{mintes:02}:{secondse:02}")
    time.sleep(1)

print("Time i's up")