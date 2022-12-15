import threading
import time

def timer():
    print()
    caunt = 0
    while True:
        time.sleep(1)
        caunt += 1
        print("logged in for: ".count, "seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()

x




answer = input("Do you wish to exit?")