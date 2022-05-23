import socket
##inner
import datetime
from Actor import Actor


class Client:
    
    PORT = 5555
    HEADER = 256
    HD_FORMAT = "utf-8"

    def __init__(self, SRV, PORT, DISSCN_MESSAGE):
        self.SRV = SRV
        self.ADDR = (SRV, PORT)
        self.DISSCN_MESSAGE = DISSCN_MESSAGE
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(self.ADDR)
        except:
            print("connecton fail")

    def send(self, msg):
        message = msg.encode(self.HD_FORMAT)
        msgSize = len(message)
        sendSize = str(msgSize).encode(self.HD_FORMAT)
        sendSize += b" " * (self.HEADER - len(sendSize))
        self.client.send(sendSize)
        self.client.send(message)



# testClient1 = Client(socket.gethostbyname(socket.gethostname()), 5555, "Disconnected")
# newA = Actor("Test", "Test", datetime.datetime.now(), "Test", 2137, "Test")
# 
# testClient1.send(newA.dataBundle())
# testClient1.send(testClient1.DISSCN_MESSAGE)