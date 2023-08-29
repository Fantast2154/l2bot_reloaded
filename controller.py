import random
import threading
import time
from multiprocessing import Process
from view.view import View
from user_props.personal_settings import PersonalSettings
from system.model import Model
from system.relaunch import RelaunchModule
from system.server import Server
from system.queue import ActionQueue
from system.l2window_manager import L2WindowManager
from system.wincap import WindowCapture

from bots.farmer.farming_service import FarmingService


class Controller:
    def send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))

    def __init__(self):
        '''
        The core of the program and main loop.
        :return:
        '''
        self.send_message('has been created')
        self.__personal_settings = PersonalSettings()
        self.__view = View(self)
        self.__model = Model(self)
        self.__relaunch_module = RelaunchModule()
        self.__server = Server(self)
        self.__l2win_manager = L2WindowManager(self)
        self.__q = ActionQueue()
        self.__wincap = WindowCapture(self.__personal_settings.l2window_name)

        self._init_controller()

        self._start_controller_thread()
        self._start_gui()

    def _init_controller(self):
        self.start_q()

    def personal_settins(self):
        return self.__personal_settings

    def view(self):
        return self.__view

    def model(self):
        return self.__model

    def relaunch_module(self):
        return self.__relaunch_module

    def server(self):
        return self.__server

    def l2win_manager(self):
        return self.__l2win_manager

    def queue(self):
        return self.__q

    def wincap(self):
        return self.__wincap

    def create_fishing_service(self):
        pass

    def stop_fishing_service(self):
        pass

    def create_farming_service(self):
        farming_service = FarmingService()

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
        if self.__server.is_running():
            self.__server.stop()

    def is_running(self):
        return self.is_running

    def _start_gui(self):
        self.send_message('GUI has been launched')
        if self.__view.app.exec() == 0:
            self._stop_controller()

    def _start_controller_thread(self):
        controller_thread = threading.Thread(target=self._run)
        controller_thread.start()

    def _stop_controller(self):
        self.is_running = False

    def _run(self):
        self.send_message('starts')
        self.create_farming_service()  # test
        self.is_running = True

        # main loop
        while self.is_running:
            pass
