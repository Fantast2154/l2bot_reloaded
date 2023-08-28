from multiprocessing import Process
import threading
from bots.farmer.farmer_dd import FarmerDD
from bots.farmer.farmer_healer import FarmerHealer

class FarmingService:
    def _send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))

    def __init__(self):
        self._send_message('has been created')
        farmer_dd1 = FarmerDD()

    def _run(self):
        pass
