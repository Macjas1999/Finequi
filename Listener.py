from concurrent.futures import thread
import socket
import threading


class Listener:

    PORT = 5555
    HEADER = 256
    HD_FORMAT = "utf-8"

    # DISSCN_MESSAGE = "Disconnected"
    # SRV = socket.gethostbyname(socket.gethostname())
    # ADDR = (SRV, PORT)

    def __init__(self, SRV, PORT, DISSCN_MESSAGE):
        self.SRV = SRV
        self.ADDR = (SRV, PORT)
        self.DISSCN_MESSAGE = DISSCN_MESSAGE
        try:
            self.srvBind = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.srvBind.bind(self.ADDR)
            ##ctrl
            #print(srvBind)
        except:
            print("Unable to bind the socket")

    def handleClient(self, conn, addr):
        print(f"New connection established: {addr}")
        connEstablished = True
        while connEstablished:
            msgSize = conn.recv(self.HEADER).decode(self.HD_FORMAT)
            if msgSize:
                msgSize = int(msgSize)
                msg  = conn.recv(msgSize).decode(self.HD_FORMAT)
                print(f"From {addr}: {msg}")
                if msg == self.DISSCN_MESSAGE:
                    connEstablished = False

        conn.close()
    
    def listenStart(self):
        self.srvBind.listen()
        print(f"Started listening on {self.SRV}")
        srvListeninig = True
        while srvListeninig:
            conn, addr = self.srvBind.accept()
            newThread = threading.Thread(target = self.handleClient, args = (conn, addr))
            newThread.start()
            print(self.threadControll())  

    def threadControll(self):
        return f"Actice threads {threading.active_count()}"  


# listenerTest = Listener(socket.gethostbyname(socket.gethostname()), 5555, "Disconnected")
# listenerTest.listenStart()