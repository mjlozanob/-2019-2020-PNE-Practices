from Client0 import *

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)

print ('*Testing PING...')
print (c.talk('OK!'))

print('*Testing GET...')
list = [0,1,2,3,4]
for element in list:
    print (c.talk(str(element)))
