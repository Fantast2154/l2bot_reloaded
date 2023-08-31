from view.view import View


class GuiHandler:

    def send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))

    def __init__(self, controller):
        self.send_message('has been created')
        self.view = View(self)
        self.controller = controller
        self._start_gui()

    def stop_bot(self):
        pass

    def _start_gui(self):
        self.send_message('GUI has been launched')
        if self.view.app.exec() == 0:
            self.send_message('GUI has been called to close')
            self.controller.stop_controller()

    def start_bot(self):
        self.controller.start_observing()

    def launch_windows(self, new_windows):
        self.controller.l2win_manager.launch_extra_windows(new_windows)

    def relaunch_windows(self):
        self.controller.l2win_manager.relaunch_all_windows()

    def close_all_windows(self):
        self.controller.l2win_manager.close_all_windows()

    def login_default(self):
        self.controller.default_start_observing()

    def start_farm_default(self):
        self.controller.default_start_farming()

    def connect_windows(self):
        self.controller.l2win_manager.connect_windows()

    def relog_all_windows(self):
        self.controller.l2win_manager.relog_all_windows()

    def connect_to_server(self):
        self.controller.connect_to_server()

    def run_server(self):
        self.controller.run_server()

    def launch_and_login_character(self, name):
        self.controller.l2win_manager.launch_and_login_character(name)
