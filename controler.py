import multiprocessing
import time

queue = multiprocessing.Queue()

def producer():
    global queue 
    for i in range(20):
        time.sleep(1)  # 模拟生产数据的耗时操作
        item = f"Item {i}"
        queue.put(item)
        print(f"[controler] Produced: {item} [time]{time.time()}")
    return queue 

if __name__ == "__main__":
    prod_process = multiprocessing.Process(target=producer)
    prod_process.start()
    prod_process.join()
    