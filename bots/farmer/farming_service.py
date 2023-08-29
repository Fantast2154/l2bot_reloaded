from multiprocessing import Process
import threading
from bots.farmer.farmer_dd import FarmerDD
from bots.service import Service
from bots.farmer.farmer_healer import FarmerHealer


class FarmingService(Service):
    def _send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))

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
