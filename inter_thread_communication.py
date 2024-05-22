
## Inter pthread communication using Condition Object 
from threading import  * 
import time 
import random

buffer=[] 
buffer_size=5 
condition=Condition() 
def producer(): 
    while True:
        item=random.randint(0,100) 
        time.sleep(2) 
        print("Produced an item and not yet inserted in buffer:",item) 
        with condition: 
            while buffer_size<=len(buffer): 
                condition.wait() 
        
            buffer.append(item) 
            print("appended item to buffer")
            condition.notifyAll() 
def consumer(): 
    while True: 
        with condition: 
            while len(buffer)==0: 
                condition.wait()  
            item=buffer.pop(0) 
            print("item consumed:",item) 
            condition.notifyAll() 
pthread=Thread(target=producer) 
cthread=Thread(target=consumer) 
pthread.start() 
cthread.start() 
pthread.join() 
cthread.join()
