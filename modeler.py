from controler import producer 
import time
def get_producer():
    queue = producer()
    # 在这里可以使用 queue_a 进行操作，获取队列中的数据等
    while not queue.empty():
        item = queue.get()
        
        print(f"[modeler]: {item} [time]{time.time()}")

if __name__ == "__main__":
    get_producer()