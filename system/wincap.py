class WindowCapture:
    def send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))

    def __init__(self, winname):
        self.window_name = winname