from bots.bot import Bot
from multiprocessing import Manager
from mathematics.vectors import Vector2i
from system.action_task import MouseTask, ClickType

class BotDamager(Bot):

    def __init__(self, damager_window, q):
        self._send_message('has been created')
        manager = Manager()
        self.id = damager_window.window_id
        self.damager_window = damager_window
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
                if not self.start_fight():
                    continue
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
        self.left_click(self.damager_window.get_autoattack())
        pass

    def target_is_alive(self):
        pass

    def start_fight(self) -> bool:
        if not self.check_buff():
            return False
        if not self.check_hp():
            return False
        if not self.chek_mp():
            return False
        self.attack()
        return True

    def is_target(self) -> bool:
        self.click_find_mob()
        if self.damager_window.is_hp_mob():
            return True
        return False

    def inc_counter(self):
        self.kill_count += 1

    # def chek_mob(self) -> bool:
    #     return self.farming_window.is_mob()

    def click_find_mob(self):
        mob_position = self.damager_window.find_mob_button()
        self.left_click(mob_position)

    def left_click(self, position: Vector2i):
        self.q.create_new_task(MouseTask(ClickType.LEFT, position, self.damager_window))
