from Client0 import *

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)

# TEST GET
print("* Testing GET...")
for n in range(0,5):
    print("Gene", n, c.talk(f"GET {n}"))