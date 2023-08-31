from bots.bot_service import BotService

class ManorService(BotService):
    def __init__(self):
        self._send_message('has been created')