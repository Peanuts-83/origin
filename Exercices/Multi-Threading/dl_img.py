import threading, time, os 
import datetime, requests

os.chdir('Multi-Threading')

def download_images(images_amount):
    for num in range(images_amount):
        random_img = f'https://picsum.photos/id/{num}/1920/1080'
        req = requests.get(random_img, stream=True)
        if req.status_code == 200:
            with open(f'images/{num}.png', 'wb') as f:
                for chunk in req:
                    f.write(chunk)
            print(f'{num} downloaded!')

start_time = datetime.datetime.now()
threads = []
for i in range(5):
    t1 = threading.Thread(target=download_images, args=(20,))
    threads.append(t1)
    t1.start()

for thread in threads:
    thread.join()

end_time = datetime.datetime.now()
print(f'This program took {end_time - start_time}')

# print(threading.active_count())