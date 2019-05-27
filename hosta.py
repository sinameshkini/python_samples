import random
random.seed()

def pair():
        host_A = 0
        while host_A %10 == 0:                  #if last digit is zero, all of table will be zero!
            host_A = random.randrange(0,999999) #Generate random number depended sys time
        print("Your time is:",host_A)
        host_B = int(input("What the destination time?"))                       #host B sys time (recive from host B)
        auth = (host_A * host_B) % 1000000      #Generate first key
        this_auth = auth
        print("Authentication code is:",this_auth)
        key_table = [0]                        #Define key table
        for i in range(0,100):
            key_table.append(0)
        key_table[0] = auth
        key_table[1] = (auth**2)%1000000
        for i in range(2,101):                  #Fill key table
            key_table[i] = (key_table[i-2]*key_table[i-1])%1000000
        for i in range(0,100):                  #Sort key table
            key_table[i] = str(key_table[i]).zfill(6)
        print("Piar is Done!")


        msg = input("Enter your message (must be 10 character):")
        counter = int(input("Enter the counter value:"))
        step1 = msg+key_table[counter]          #create text of plain message
        cod = int(key_table[counter])
        cod = (cod**2)%100000000
        codprime = (999999999999-cod)%100000000
        hashcod = str(cod)+str(codprime)
        hashcod = hashcod.zfill(16)
        fcode = ['0']
        for i in range(0,15):
            fcode.append('0')
        cnt = 0
        for i in range(0,10):
            for j in range(0,16):
                if int(hashcod[j]) == i:
                    fcode[j] = str(cnt)
                    cnt+=1
        fmsg = ['0']
        for i in range(0,15):
            fmsg.append('0')
        for i in range(0,16):
            fmsg[i]=step1[int(fcode[i])]

        send = fmsg[0]
        for i in range(1,16):
            send += fmsg[i]
        print("Coded message is: ",send)



print("***********************************************"\
,"\n**************  WELLCOM TO CAP  ***************",\
"\n********  Developed by: Sina Meshkini  ********",\
"\n***********************************************\n\n")
while 1:
    print("help:\ntype [pair] command for pair with other devices\n")
    print("type [start] to start messaging\n")
    command = input("command:")
    if command == "pair":
        pair()
    elif command == "start":
        messaging()

    print("_______________________________________________________________")
