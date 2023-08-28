class Server:
    def send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))

    def __init__(self, controller):
        self.controller = controller
        self.is_running = False

    def is_running(self):
        return self.is_running

    def stop(self):
        self.is_running = False
