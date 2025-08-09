import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Numbers:{i}")
def print_letters():
    for i in 'abcde':
        time.sleep(2)
        print(f"letter:{i}")

t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)
t1=time.time()
t1.start()
t2.start()
t1.join(t2)
