#import socket
class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("OK!")

    def __str__(self):
        return "Connection to SERVER at " + self.ip + ", PORT:" + str(self.port)