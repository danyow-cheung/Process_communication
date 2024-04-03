# from controler import only_producer 
from controler import queue

import time

def get_producer():
    # queue = only_producer()
    # 在这里可以使用 queue_a 进行操作，获取队列中的数据等
    # while not queue.empty():
    while True:
        
        if not queue.empty():
            item = queue.get()
            print(f"[modeler]: {item} ")
        else:
            time.sleep(1)

if __name__ == "__main__":
    get_producer()