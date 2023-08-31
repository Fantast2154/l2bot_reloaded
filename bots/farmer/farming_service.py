from multiprocessing import Process
import threading
from bots.farmer.farmer_dd import FarmerDD
from bots.bot_service import BotService
from bots.farmer.farmer_healer import FarmerHealer


class FarmingService(BotService):

    def __init__(self):
        self._send_message('has been created')
        bot = self.create_bot()
        self.start_bot(bot)
        self.stop_bot(bot)

    def create_bot(self):
        self._send_message('bot has been created')
        bot = FarmerDD(0)
        self.bots.append(bot)
        self.bot_processes.append(Process(target=bot.start))
        return bot

    def _run(self):
        pass
