from bots.farmer.farming_window import FarmingWindow


class BufferWindow(FarmingWindow):
    def _send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))

    def __init__(self):
        pass