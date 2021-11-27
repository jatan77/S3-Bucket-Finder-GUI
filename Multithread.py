from urllib.parse import urlparse
from threading import Thread
import http.client, sys
from queue import Queue
import requests

concurrent = 15

def doWork():
    while True:
        url = q.get()
        r = requests.get(url.strip(),timeout=3)
        print(r.status_code)
        if r.status_code == 200:
            file = open('temp-result.txt','a') 
            file.write(url) 
            file.close() 
        else:
            print("notworking-- "+url)
        file = open('c.txt','a') 
        file.write(url) 
        file.close() 
        q.task_done()


q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:
    with open("temp-url.txt",'r') as f:
        for line in f:
            url=line
            q.put(url)
    q.join()
except KeyboardInterrupt:
    sys.exit(1)
