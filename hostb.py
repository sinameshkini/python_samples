import random
random.seed()

print("***********************************************"\
,"\n**************  WELLCOM TO CAP  ***************",\
"\n********  Developed by: Sina Meshkini  ********",\
"\n***********************************************\n\n")
print("help:\ntype [pair] command for pair with other devices\n")
command = input("command:")

host_B = 0
while host_B %10 == 0:                  #if last digit is zero, all of table will be zero!
    host_B = random.randrange(0,999999)
print("Host B time is:",host_B)
host_A = int(input("Host A time?"))
auth = (host_A * host_B) % 1000000      #Generate first key
this_auth = auth
print("Authentication code is:",this_auth)
