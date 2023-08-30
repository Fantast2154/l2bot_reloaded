from bots.bot import Bot

class FarmerDD(Bot):
    def send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))

    def __init__(self, id):
        self.id = id
        self.send_message('has been created')
        self.exit_is_set = True
        self.kill_count = 0

    def start(self):
        self.send_message('started')
        self._run()

    def stop(self):
        self.send_message('stopped')

    def _run(self):
        self.send_message('разминаю пальчики')
        while not self.exit_is_set:
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


