import multiprocessing
import time
from queue import Queue 

# queue = multiprocessing.Queue()
fifo_queue = Queue() # 队列是全局变量，这个应该没问题Queue


def handle():
    global fifo_queue
    inference_info= fifo_queue.get()
    with open('history.txt', 'a',encoding='utf-8') as f:
        f.write(f'{inference_info}\n')
        f.flush()  # 立刻写入磁盘


while True:
    for i in range(100):
        fifo_queue.put(f"你好当前时间戳{time.ctime()}")
        handle()



