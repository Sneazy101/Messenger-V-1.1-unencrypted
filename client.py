import socket
class client_11:

    def __init__(self):
        self.host='127.0.0.1'
        self.port=9900
        self.s = socket.socket()
        self.s.connect((self.host, self.port))

    def msg_recieve(self):
        self.data = self.s.recv(1024)
        rec_msg = str(self.data.decode('utf-8'))
        if len(rec_msg) >0:
            print(rec_msg)

    def msg_send(self):
        msg_send = input("Enter your text")
        self.s.send(msg_send.encode('utf-8'))


    def run(self):
        while True:
            self.msg_recieve()
            self.msg_send()

a = client_11()
a.run()


