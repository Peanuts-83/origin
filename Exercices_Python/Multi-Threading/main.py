import threading, time

def func(amount):
    print('Start')
    time.sleep(amount)
    print('End')

threads = []
for i in range(5):
    t1 = threading.Thread(target=func, args=(i,))
    threads.append(t1)
    t1.start()

for thread in threads:
    thread.join()

print(threading.active_count())