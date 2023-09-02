from multiprocessing import Process
from time import sleep
from enum import Enum

from bots.bot_service import BotService

from bots.bot_window import BotWindow
from bots.farmer.farming_window import FarmingWindow
from bots.farmer.bot_damager_window import DamagerWindow
from bots.farmer.bot_healer_window import HealerWindow
from bots.farmer.bot_spoiler_window import SpoilerWindow

from bots.bot import Bot
from bots.farmer.bot_damager import BotDamager
from bots.farmer.bot_healer import BotHealer
from bots.farmer.bot_spoiler import BotSpoiler


class FarmingRoles(Enum):
    DAMAGER = 0
    HEALER = 1
    SPOILER = 2
    TANK = 3
    BD = 4
    SVS = 5
    BUFFERWK = 6
    BUFFERPP = 7


class FarmingService(BotService):
    farmers = {}
    dds = {}
    healers = {}
    suppliers = {}
    tanks = {}
    bds = {}
    svses = {}
    buffers = {}

    def __init__(self, l2win_manager, q):
        self._send_message('has been created')
        self.q = q
        self.l2win_manager = l2win_manager

    def create_damager(self):
        self.create_bot(FarmingRoles.DAMAGER, self.l2win_manager.l2windows[0])

    def find_index(self, dct: dict):
        for key, val in dct.items():
            if val is None:
                return key
        return len(dct.items())

    def create_bot(self, role: FarmingRoles, bot_window: BotWindow) -> Bot:
        self._send_message('creating bot')
        match role:
            case FarmingRoles.DAMAGER:
                self._send_message('damager1')
                self._send_message(bot_window.window_id)
                self._send_message(bot_window.hwnd)
                farming_window = DamagerWindow(bot_window)
                self._send_message('damager11')
                bot = BotDamager(farming_window, self.q)
                self._send_message('damager111')
            case FarmingRoles.HEALER:
                farming_window = HealerWindow(bot_window)
                bot = BotHealer(farming_window, self.q)
            case FarmingRoles.SPOILER:
                farming_window = SpoilerWindow(bot_window)
                bot = BotSpoiler(farming_window, self.q)
            # case FarmingRoles.TANK:
            #     bot_window = FarmingWindow()
            # case FarmingRoles.BD:
            #     bot_window = FarmingWindow()
            # case FarmingRoles.SVS:
            #     bot_window = FarmingWindow()
            # case FarmingRoles.BUFFERWK:
            #     bot_window = FarmingWindow()
            # case FarmingRoles.BUFFERPP:
            #     bot_window = FarmingWindow()
            case _:
                farming_window = None
                self._send_message('ERROR def create_bot_window NO MATCH ')
                raise 'ERORR create_bot_window'

        self._send_message('damager2')
        if bot is None:
            self._send_message('ERROR def create_bot')
            raise 'ERROR def create_bot'
        self._send_message('damager3')
        self.bots[self.find_index(self.bots)] = bot
        self._send_message('damager4')
        self.bot_processes[self.find_index(self.bot_processes)] = Process(target=bot.start)
        self._send_message(len(self.bots))
        return bot

    def _run(self):
        while self.is_running:
            sleep(2)
            # self.network.send_netmessage("RaidBoss {observer.rb_name} появился! ОГОНЬ ИЗ ВСЕХ ОРУДИЙ.")
            if not self.farmers:
                continue
