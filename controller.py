import random
import threading
import time
from multiprocessing import Process
from user_props import PersonalSettings
class Controller:
    def send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))

    def __int__(self):
        '''
        The core of the program and main loop.
        :return:
        '''
        self.send_message('has been created')
        self.personal_settings = PersonalSettings()
        self.view = View(self)
        self.model_database = Model(self)
        self.relaunch_module = RelaunchModule(self)
        self.server = Server(self)
        self.l2win_manager = L2WindowManager()
        self.q = ActionQueue()
        self.wincap = WindowCapture(self.personal_settings.l2window_name)

        self.start_q()
        self._run()

    def create_fishing_service(self):
        pass

    def stop_fishing_service(self):
        pass

    def create_farming_service(self):
        pass

    def stop_farming_service(self):
        pass

    def start_q(self):
        pass

    def stop_q(self):
        pass

    def start_wincap(self):
        pass

    def stop_wincap(self):
        pass

    def start_server(self, permission_to_host):
        pass

    def stop_server(self):
        if self.server.is_running():
            self.server.stop()

    def is_running(self):
        return self.is_running

    def _run(self):
        self.send_message('starts')
        self.is_running = True
        # loop
        self.is_running = False
