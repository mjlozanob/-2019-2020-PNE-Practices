from Client0 import *

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)

msg = "COMP AACCGTA"
response = c.talk(msg)
print(msg)
print(response)