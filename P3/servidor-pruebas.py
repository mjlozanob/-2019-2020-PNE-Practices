import socket
import termcolor
from Seq1 import *
from Seq0 import *

s1 = "AAC"
s2 = "GTC"
s3 = "TCT"
s4 = "GTA"
s5 = "TTG"
seq_list = [s1, s2, s3, s4, s5]
bases_list = ["A", "T", "G", "C"]

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("SEQ Server configured")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")


    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listening socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("A client has connected to the server!")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()

        # -- Implement PING command

        if msg == "PING":
            response = "OK!"
            termcolor.cprint("PING command!", "green")
            print(response)

        # -- Split the message to identify the command
        msg = msg.split()

        # -- Implement GET command

        if "GET" in msg:
            termcolor.cprint("GET", "green")
            index = int(msg[1])
            response = seq_list[index]
            print(response)

        # -- Implement INFO command
        elif "INFO" in msg:
            termcolor.cprint("INFO", "green")
            seq = Seq(msg[1])
            divisor = seq.len()
            print("Sequence: ", seq)
            print("Total length: ", seq.len())
            flick = ""
            for e in bases_list:
                count = seq.count_base(e)
                result = count * 100 / divisor
                flick = flick + e + ":" +str(result)+"%\n"
                print(e, ":", round(result, 2), "%")
            response = flick

        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the data socket
        cs.close()