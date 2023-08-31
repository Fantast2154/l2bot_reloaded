from bots.bot_service import BotService

class BrokerService(BotService):
    def _send_message(self, message) -> None:
        print(str(self.__class__.__name__) + ': ' + str(message))

    def __init__(self):
        self._send_message('has been created')