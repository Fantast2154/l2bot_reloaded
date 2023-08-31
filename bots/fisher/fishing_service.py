from bots.bot_service import BotService

class FishingService(BotService):

    def __init__(self):
        self._send_message('has been created')