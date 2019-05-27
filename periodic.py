import time, threading

c=0
def foo():
    global c
    print(c)
    c+=1
    threading.Timer(1, foo).start()

foo()

def foo1():
    print("hop")
    threading.Timer(5, foo1).start()

foo1()
