# from view.view import View
from view.view_old import View
from time import sleep

class GuiHandler:

    def send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))

    def __init__(self, controller):
        self.send_message('has been created')
        self.view = View(self)
        self.controller = controller
        self._start_gui()

    def stop_bot(self):  # TODO: какого конкретно бота будет останавливать эта функция? Нужно передавать id
        pass

    def _start_gui(self):
        self.send_message('GUI has been launched')
        if self.view.app.exec() == 0:
            self.send_message('GUI has been called to close')
            self.controller.stop_controller()

    def start_bot(self):  # TODO: какого конкретно бота будет запускать эта функция? Нужно передавать id
        self.controller.farming_service.start_bot(0)

    def launch_windows(self, new_windows):
        self.controller.l2win_manager.launch_extra_windows(new_windows)

    def relaunch_windows(self):
        self.controller.l2win_manager.relaunch_all_windows()

    def close_all_windows(self):
        self.controller.l2win_manager.close_all_windows()

    def login_default(self):
        self.controller.default_start_observing()

    def start_farm_default(self):
        self.controller.farming_service.create_damager()
        sleep(3)
        self.controller.farming_service.start_bot(0)

    def connect_windows(self):
        self.controller.l2win_manager.connect_windows()

    def relog_all_windows(self):
        self.controller.l2win_manager.relog_all_windows()

    def connect_to_server(self):
        self.controller.connect_to_server()

    def run_server(self):
        self.controller.run_server()

    def launch_and_login_char(self, name):
        self.controller.launch_and_login_character(name)
