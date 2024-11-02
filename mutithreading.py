import threading
import time
def print_number():
    for i in range(5):
        time.sleep(2)
        print(f'Number:{1}')

def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter:{letter}")


t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letters)
t=time.time()
t1.start()
t2.start()
t1.join()
t2.join()
finished_line=time.time()-t
print(finished_line)