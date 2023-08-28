from controller import Controller


class Application:
    '''    main application class  '''

    def __init__(self):
        self.send_message('has been created')
        self.launch_application()

    @staticmethod
    def launch_application():
        Controller()

    def send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))
