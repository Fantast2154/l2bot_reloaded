import socket


class Client:
    def __init__(self):
        self.server = None

    def connect_to(self, HOST, PORT):
        ADDRESS = (HOST, PORT)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect(ADDRESS)
        self.server.send(b'2')

    def receive_data(self):
        pass

    def send_data(self, data):
        pass


if __name__ == '__main__':
    client = Client()
    client.connect_to('5.137.131.229', 27015)
