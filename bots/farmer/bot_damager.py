from bots.bot import Bot
from multiprocessing import Manager

class BotDamager(Bot):

    def __init__(self, damager_window, q):
        self._send_message('has been created')
        manager = Manager()
        self.id = damager_window.window_id
        self.q = q
        self.is_running = manager.list().append(False)
        self.kill_count = 0

    def start(self):
        self._send_message('started')
        self.is_running[0] = True
        self._run()

    def stop(self):
        self._send_message('stopped')
        self.is_running[0] = False

    def _run(self):
        self._send_message('разминаю пальчики')
        while self.is_running[0]:
            if self.is_target():
                self.start_fight()
                while self.target_is_alive():
                    self.attack()
                    self.chek_hp()
                self.inc_counter()
                self.loot_target()

    def loot_target(self):
        pass

    def chek_hp(self):
        pass

    def attack(self):
        pass

    def target_is_alive(self):
        pass

    def start_fight(self):
        pass

    def is_target(self) -> bool:
        self.click_find_mob()
        # if self.chek_mob():
        #     return True
        return False

    def inc_counter(self):
        self.kill_count += 1

    # def chek_mob(self) -> bool:
    #     return self.farming_window.is_mob()

    def click_find_mob(self):
        pass
