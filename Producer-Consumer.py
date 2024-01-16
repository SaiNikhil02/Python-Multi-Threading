from threading import *
import random
import time
N=50
buffer=[0]*N 
fill_slots=Semaphore(0) 
empty_slots=Semaphore(N) 

def produce(): 
    return 1    

def producer(buffer): 
    font=0 
    while True: 
        x=produce() 
        empty_slots.acquire() 
        buffer[font]=x  
        print("Intem produced:")
        time.sleep(2)
        font=(font+1)%N 
        fill_slots.release()
         
def consume(y): 
    print("one item consumed:",y)
def consumer(buffer): 
    rear=0 
    while True: 
        fill_slots.acquire() 
        x=buffer[rear] 
        time.sleep(2) 
        consume(x)  
        rear=(rear+1)%N   
        empty_slots.release()    
        

p=Thread(target=producer,args=(buffer,)) 
c=Thread(target=consumer,args=(buffer,)) 
p.start() 
c.start()