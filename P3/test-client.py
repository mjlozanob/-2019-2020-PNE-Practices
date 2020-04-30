from Client0 import *

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)

response = c.talk("GET 2")
response_2 = c.talk("INFO AAATT")
print(response)
print(response_2)