'''

'''
from controler import producer

import time

def get_producer():
    # queue = producer()    
    while True:
        queue = producer()            
        print('queue',queue)
        # if not queue.empty():
        if queue != None:
            print(queue.qsize())
            item = queue.get()
            print(f"[modeler]: {item} ")
        else:
            time.sleep(1)

def get_value():
    while True:
        print('1')
        queue = producer()
        if not queue.empty():

            print('Got data:', queue,queue.qsize())
        else:
            time.sleep(1)

if __name__ == "__main__":
    get_producer()