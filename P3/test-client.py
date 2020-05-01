from Client0 import *

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)

# Testing GET
print("* Testing GET...")
for n in range(0,5):
    print("Gene", n, c.talk(f"GET {n}"))

# Testing INFO
print("* Testing INFO...")
print("Sequence: AAC")
print(c.talk("INFO AAC"))

# Testing COMP
print("* Testing COMP...")
print(c.talk("COMP AAC"))

# Testing REV
print("* Testing REV...")
print(c.talk("REV AAC"))

# Testing GENE
gene_list = ["REV U5", "REV FRAT1", "REV ADA", "REV FXN", "REV RNU6_269P"]
for item in gene_list:
    print(c.talk(item))