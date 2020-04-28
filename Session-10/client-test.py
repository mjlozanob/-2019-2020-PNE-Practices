from Client0 import *

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)

msg_list = ["0","1","2","3","4"]

for element in msg_list:
    c.debug_talk("Message: "+element)