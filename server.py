import socket

class server_11:
    def __init__(self):
        self.host = ''
        self.port = 9900
        self.s = socket.socket()
    try:
        pass
    except socket.error as msg:
        print('Socket creation error: '+str(msg))

    def bind_socket(self):
        try:
            print('Binding the Port: '+ str(self.port))

            self.s.bind((self.host, self.port))
            self.s.listen(5)

        except socket.error as msg:
            print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
            self.bind_socket()

    def socket_accept(self):
        self.conn, address = self.s.accept()
        print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
        self.start_msg()
        self.conn.close()

    def start_msg(self):
        while True:
            msg_send = input('Enter your text ')
            if msg_send == 'quit':
                self.conn.close()
                self.s.close()
            elif len(str.encode(msg_send)) > 0:
                self.conn.send(msg_send.encode("utf-8"))
                rec_msg= str(self.conn.recv(1024),"utf-8")
                print(rec_msg)

    def run(self):
        self.bind_socket()
        self.socket_accept()

a = server_11()
a.run()



