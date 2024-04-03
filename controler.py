import multiprocessing
import time
from queue import Queue 

from flask import Flask 
app = Flask(__name__)
queue = multiprocessing.Queue()

tep = Queue()

def producer():
    global queue ,tep 
    if  not tep.empty():
        queue.put(tep.get())
        return queue 

@app.route("/",methods=['POST'])
def hello():
    global queue ,tep
    print(queue.qsize())

    item = time.time()
    tep.put(item)
    producer()

    return "ok"


if __name__ == "__main__":

    # prod_process = multiprocessing.Process(target=producer)
    # prod_process.start()
    app.run(host='192.168.0.37',debug=True)