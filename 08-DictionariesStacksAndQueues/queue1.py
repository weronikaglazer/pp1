queue = [3,4,5,6,7]

def push(value):    
    queue.append(value)  

def pop():
    queue.pop(0)

def empty():    
    return len(queue) == 0

def display():    
    for i in queue:        
        print(i)    
    print(" ")

