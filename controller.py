from threading import Thread
from time import sleep
from multiprocessing import Process

from user_props.personal_settings import PersonalSettings
from system.model import Model
from system.server import Server
from system.queue import ActionQueue
from system.l2window_manager import L2WindowManager
from system.wincap import WindowCapture
from view_props.view import View, GUIHandler

from bots.broker.broker_service import BrokerService
from bots.farmer.farming_service import FarmingService
from bots.fisher.fishing_service import FishingService
from bots.manor_exchanger.manor_service import ManorService
from user_props.personal_settings_blank import PersonalSettingsBlank


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
    is_running = False

    manor_service = None
    fishing_service = None
    farming_service = None
    broker_service = None

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
        self.personal_settings = PersonalSettingsBlank()
        self.model = Model(self)
        self.server = Server(self)
        self.l2win_manager = L2WindowManager(self)

        self._init_controller()
        self.start_service(self.farming_service)
        self._start_controller_thread()
        self.handler = GUIHandler(self)

    def _init_controller(self):
        self._start_q()
        self._start_wincap()
        # self.launch_and_login_character()
        self.create_services()

    def launch_and_login_character(self, name='ПреображенскийЕВ'):
        self.send_message('launch_and_login_character')
        self.l2win_manager.launch_and_login_character(name)

    def stop_fishing_service(self):
        pass

    def create_services(self):
        self.broker_service = BrokerService()
        self.farming_service = FarmingService(self.l2win_manager, self.q)
        self.fishing_service = FishingService()
        self.manor_service = ManorService()

    def start_service(self, service):
        service.start()

    def stop_service(self, service):
        service.stop()

    def stop_all_services(self):
        self.broker_service.stop()
        self.farming_service.stop()
        self.fishing_service.stop()
        self.manor_service.stop()

    def _start_q(self):
        self.q_process = Process(target=self.q.start)
        self.q_process.daemon = True
        self.q_process.start()
        sleep(1)

    def _stop_q(self):
        self.stop_all_services()
        self.q.stop()
        self.q_process.join()

    def _start_wincap(self):
        self.wincap.set_windows(self.l2win_manager.l2windows)
        self.wincap_process = Process(target=self.wincap.start_capturing, args=(self.l2win_manager.screenshot,))
        #self.wincap_process.daemon = True
        self.wincap_process.start()

    def _stop_wincap(self):
        self.wincap.stop()
        self.wincap_process.join()

    def _start_server(self, permission_to_host):
        pass

    def _stop_server(self):
        if self.server.is_running():
            self.server.stop()

    def _start_controller_thread(self):
        self.is_running = True
        controller_thread = Thread(target=self._run)
        controller_thread.start()

    def _run(self):

        # main loop
        while self.is_running:  # WARNING: НИКАКИХ СУКА EXIT_IS_SET. ТЫ ПО-РУССКИ ПИШИ. self._is_running НЕ ИСПРАВЛЯТЬ
            sleep(5)

        self.send_message('CONTROLLER STOPPED')

    def stop_controller(self):
        self._stop_wincap()
        self._stop_q()
        self.is_running = False
