from bots.bot import Bot

class FarmerDD(Bot):
    def send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))

    def __init__(self, id):
        self.id = id
        self.send_message('has been created')

    def start(self):
        self.send_message('started')

    def stop(self):
        self.send_message('stopped')

