import socket
import threading


class Server:
    def __init__(self):
        self.HOST = ''
        self.PORT = 27015

        self.ADDRESS = (self.HOST, self.PORT)
        self.BUFFERSIZE = 64

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDRESS)
        self.server.listen(10)

        self.clients = []
        self.clients_threads = []

        self.is_running = False

    def send_data_to(self, client):
        pass

    def receive_data_from(self, client):
        print('New thread started:', client)
        while self.is_running:
            message = client.recv(self.BUFFERSIZE)
            if message:
                print(message)
            else:
                continue

    def accept_new_client(self):
        print('Listening...')
        while self.is_running:
            client, address = self.server.accept()
            self.clients.append(client)

            client_thread = threading.Thread(target=self.receive_data_from, args=(client,))
            client_thread.start()
            self.clients_threads.append(client_thread)

    def delete_client(self, client):
        index = self.clients.index(client)
        self.clients.pop(index)
        client_thread = self.clients_threads.pop(index)
        client_thread.join()

    def start(self):
        self.is_running = True
        self.accept_new_client()

    def stop(self):
        self.is_running = False


if __name__ == '__main__':
    server = Server()
    server.start()
