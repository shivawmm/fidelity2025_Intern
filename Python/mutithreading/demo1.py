from threading import *
import time
# def dsp():
#     for i in range(1,10):
#         print("child thread")
# t = Thread(target=dsp)
# t.start()
# for i in range(1,5):
#     print("main thread")

def twopower():
    start_time = time.perf_counter()
    for i in range(1,10):
        print(2**i)
        time.sleep(0.25)
    end_time = time.perf_counter()
    print(f"Execution time for twopower: {end_time - start_time:.4f} seconds")
t = Thread(target=twopower)
t.start()
def fivepower():
    start_time = time.perf_counter()
    for i in range(1,10):
        print(5**i)
        time.sleep(0.35)
    end_time = time.perf_counter()
    print(f"Execution time for fivepower: {end_time - start_time:.4f} seconds")
t = Thread(target=fivepower)
t.start()
# def f2():
#     for i in range(1,100):
#         t.time(1)
