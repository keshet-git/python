import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You eat bteakfast")


def drink_tee():
    time.sleep(4)
    print("you drank tee")


def study():
    time.sleep(5)
    print("you finish studying")

#eat_breakfast()
#drink_tee()
#study()

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_tee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())