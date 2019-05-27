from threading import Timer

#counter = 0
#def count():
#    global counter
#    counter+=1
#    print ("Hop")
#    timer1.start()

#timer1 = Timer(5.0,count)
#timer1.start()

counter1 = 0
def count1():
    global counter1
    counter1+=1
    print (counter1)
    #Timer(1.0,count1).start()
    timer2.reset()
    timer2.start()


timer2 = Timer(1.0,count1)
timer2.start()
