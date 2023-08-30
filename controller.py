import random
import threading
from time import sleep
from multiprocessing import Process
from view.view import View
from user_props.personal_settings import PersonalSettings
from system.model import Model
from system.server import Server
from system.queue import ActionQueue
from system.l2window_manager import L2WindowManager
from system.wincap import WindowCapture

from bots.farmer.farming_service import FarmingService


class Controller:
    q = None
    q_process = None
    wincap_process = None
    personal_settings = None
    view = None
    model = None
    relaunch_module = None
    server = None
    l2win_manager = None
    wincap = None

    def send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))

    def __init__(self):
        '''
        The core of the program and main loop.
        :return:
        '''

        self.send_message('has been created')
        self.q = ActionQueue()
        self.wincap = WindowCapture()
        self.personal_settings = PersonalSettings()
        self.model = Model(self)
        self.server = Server(self)
        self.view = View(self)
        self.l2win_manager = L2WindowManager(self)

        self._init_controller()
        self._start_controller_thread()
        self._start_gui()

    def _init_controller(self):
        self.start_q()
        self.start_wincap()
        sleep(3)
        self.launch_and_login_character()
        self.create_farming_service()  # test

    def launch_and_login_character(self, name='ПреображенскийЕВ'):
        self.l2win_manager.launch_and_login_character(name)

    def create_fishing_service(self):
        pass

    def stop_fishing_service(self):
        pass

    def create_farming_service(self):
        farming_service = FarmingService()

    def stop_farming_service(self):
        pass

    def start_q(self):
        self.q_process = Process(target=self.q.start)
        self.q_process.start()

    def stop_q(self):
        self.q.stop()
        self.q_process.join()

    def start_wincap(self):
        self.wincap.set_windows(self.l2win_manager.l2windows)
        self.wincap_process = Process(target=self.wincap.start_capturing, args=(self.l2win_manager.screenshot,))
        self.wincap_process.start()

    def stop_wincap(self):
        self.q.stop()
        self.q_process.join()

    def start_server(self, permission_to_host):
        pass

    def stop_server(self):
        if self.server.is_running():
            self.server.stop()

    def is_running(self):
        return self.is_running

    def _start_gui(self):
        self.send_message('GUI has been launched')
        if self.view.app.exec() == 0:
            self._stop_controller()

    def _start_controller_thread(self):
        controller_thread = threading.Thread(target=self._run)
        controller_thread.start()

    def _stop_controller(self):
        self.stop_q()
        self.stop_wincap()
        self.is_running = False

    def _run(self):
        self.send_message('starts')
        self.is_running = False

        # main loop
        while self.is_running:
            pass
