import os
import time
import win32con
import win32gui
from system.l2window import L2window
from multiprocessing import Manager
from system.login_module import LoginModule
import collections
from system.character import Character


class L2WindowManager:
    # l2windows = []

    # l2windows_name = []
    # l2windows_id = []
    # l2windows_hwnd = []
    # l2windows_owner = []

    def send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))

    def __init__(self, controller):
        manager = Manager()
        self.personal_settings = controller.personal_settings
        self.q = controller.q
        self.wincap = controller.wincap
        self.l2windows = []
        self.view = controller.view
        self.screenshot = manager.list()
        self.screenshot.append(0)

        self.delay_between_launching_windows = 40

        self.loginer = LoginModule(controller.wincap, controller.q)
        self.characters = self.characters()

        self.available_characters = self.characters.copy()

        self.init_windows_connection()

    def init_windows_connection(self):
        if self.get_l2hash_launched():
            self.initial_connect_windows()

    def characters(self):
        temp_characters = []
        for i in range(len(self.personal_settings.logins)):
            character = Character(self.personal_settings.logins[i], self.personal_settings.passwords[i],
                                  self.personal_settings.names[i], self.personal_settings.rb_names[i])
            temp_characters.append(character)

        return temp_characters

    def default_characters_observer(self):
        temp_characters = []
        for i in range(len(self.personal_settings.default_logins_observer)):
            character = Character(self.personal_settings.default_logins_observer[i],
                                  self.personal_settings.default_passwords_observer[i],
                                  self.personal_settings.default_names_observer[i],
                                  self.personal_settings.default_rb_names_observer[i])
            temp_characters.append(character)

        return temp_characters

    def default_characters_farmer(self):
        temp_characters = []
        for i in range(len(self.personal_settings.default_logins_farmer)):
            character = Character(self.personal_settings.default_logins_farmer[i],
                                  self.personal_settings.default_passwords_farmer[i],
                                  self.personal_settings.default_names_farmer[i],
                                  self.personal_settings.default_rb_names_farmer[i])
            temp_characters.append(character)

        return temp_characters

    def find_character_by_name(self, name: str):
        if not name or type(name) != str:
            return

        for character in self.available_characters:
            if character.name == name:
                return character

    def remove_character_from_available_list(self, character):
        if character not in self.available_characters:
            return False

        for i, chr in enumerate(self.available_characters):
            if character == chr:
                self.available_characters.pop(i)
                # self.view.refresh_available_character_list(self.available_characters)
                return True

        return False

    def scan_windows(self):
        pass

    def login_window(self, character, window):
        self.loginer.window_login(character.login, character.password, window)
        return True

    def launch_and_login_character(self, name):
        if not name:
            return

        character = self.find_character_by_name(name)
        self.send_message(f'Launching and logging {character.name}')
        number_of_connected_windows = len(self.get_l2hash_connected())
        self.send_message(f'Number of connected windows {number_of_connected_windows}')

        self.launch_window()
        time.sleep(5)
        if len(self.l2windows) == number_of_connected_windows + 1:
            self.send_message(f'launch window {self.l2windows[-1].hwnd} was successful')
            self.login_window(character, self.l2windows[-1])
            self.remove_character_from_available_list(character)
            self.send_message(f'Character {character.name} was successfully logged in')
            self.l2windows[-1].character = character
            self.l2windows[-1].logged = True

            self.send_message('СМАЗАЛ ВАШЕГО МУРЛОКА: 15 1 ПРОВОКАЦИЯ, РЫВОК, ЩИТ, ПРЕДСМЕРТНЫЙ ХРИП.')
            self.send_message('ЗАПУСК УСПЕШЕН. ИДИ С БОГОМ.')
        else:
            self.send_message(f'RELOG FAILED')

    def default_login(self, param):
        # todo после кликов connect windows, default login, загрузился модуль, но ничего не произошло
        self.send_message('Login default')
        if param == 'observer':
            self.default_chars = self.default_characters_observer()
        elif param == 'farmer':
            self.default_chars = self.default_characters_farmer()

        self.close_all_windows()
        time.sleep(2)
        name_list, hash_list = self._get_l2windows_param()
        number_of_opened_windows = len(name_list)

        if number_of_opened_windows:
            return

        self.l2windows = []

        for _ in range(len(self.default_chars)):
            self.launch_window()

        successfull_login_list = []
        for i, window in enumerate(self.l2windows):

            new_character = self.default_chars[i]
            successfull_login = self.login_window(new_character, window)

            if successfull_login:
                successfull_login_list.append(1)
                window.character = new_character

                window.logged = True
                self.send_message(f'Window {window.hwnd} successfully logged in. Character:  {window.character.name}')
                self.send_message(f'login_default Connected characters: {self.get_character_names_connected()}')
                self.send_message('Приятной охоты.')

        time.sleep(2)
        if sum(successfull_login_list) == len(self.default_chars):
            return True

    def launch_extra_windows(self, new_windows=1):
        self.send_message(f'launch {new_windows} windows')
        if type(new_windows) != int:
            return

        available_to_launch = 3 - len(self.l2windows)
        if new_windows <= available_to_launch:
            for _ in range(new_windows):
                self.launch_window()

    def update_wincap(self):
        self.send_message('update_wincap')
        name_list, hash_list = self._get_l2windows_param()
        if not self.l2windows:
            self.wincap.set_windows([])
            return
        windows_for_wincap = [window for window in self.l2windows if window.hwnd in hash_list]
        self.wincap.set_windows(windows_for_wincap)

    def launch_window(self):

        self.send_message('launching L2 window')
        time.sleep(1)
        os.startfile(self.personal_settings.launcher_path)
        t = time.time()
        time.sleep(4)
        hash1 = self.get_l2hash_launched()
        self.send_message(f'number of windows: {len(hash1)}')
        counter = 0

        while time.time() - t < self.delay_between_launching_windows:
            time.sleep(1)
            hash2 = self.get_l2hash_launched()
            if len(hash2) == (len(hash1) + 1):
                break
            counter += 1
            # self.send_message(f'Launching..{counter}')
        time.sleep(4)
        self.connect_windows()

    def launch_default_configuration(self):
        '''
        launches 1 window for application (and skips if it is running)
        '''

        self.send_message('launchBasicConfiguration')
        name_list, _ = self._get_l2windows_param()
        n = len(name_list)
        if n < self.personal_settings.basic_number_of_windows:
            # place for L2 FATALITY ERROR
            # TODO
            for _ in range(self.personal_settings.basic_number_of_windows - n):
                self.launch_window()
        # self.classify_launched_windows()

    def close_window(self, window):
        if window not in self.l2windows:
            return

        self.close_l2_window(window.hwnd)
        id = self.l2windows.index(window)

        self.available_characters.append(window.character)
        self.l2windows.pop(id)

        self.update_wincap()

    def close_all_windows(self):
        self.send_message('Closing all L2 windows')
        l2windows_hwnd = self.get_l2hash_launched()

        if not l2windows_hwnd:
            return

        self.send_message('ready to close')

        if self.get_character_names_connected():
            self.send_message(f'Used characters: {self.get_character_names_connected()}')
            self.available_characters.extend(self.get_characters_connected())
            self.send_message(f'Available characters: {self.get_available_character_names()}')

        self.l2windows = []

        self.update_wincap()

        for hwnd in l2windows_hwnd:
            self.close_l2_window(hwnd)

    def relaunch_window(self, window):
        pass

    def relaunch_all_windows(self):

        l2win_hwnds = self.get_l2hash_launched()
        self.send_message(f'Relaunching all L2 windows: {l2win_hwnds}')
        number_of_launched_windows = len(l2win_hwnds)
        if not number_of_launched_windows:
            return

        self.close_all_windows()

        self.send_message(f'Launching {number_of_launched_windows} windows')
        for _ in range(number_of_launched_windows):
            self.launch_window()

        self.send_message('relaunch_all_windows ENDING')
        self.send_message(f'Relaunching all L2 windows is complete: {self.get_l2hash_connected()}')

    def relog_window(self, window):

        self.send_message(f'Window to relog: {window.hwnd}')
        self.send_message(f'Character to relog: {window.character.name}')
        self.send_message(f'Connected characters: {self.get_character_names_connected()}')
        self.send_message(f'Number of connected windows {self.get_l2hash_connected()}')

        if not self.l2windows or not window.logged:
            return

        character = window.character

        self.close_l2_window(window.hwnd)
        self.drop_window_from_list(window)
        self.send_message(f'Number of connected windows_2 {self.get_l2hash_connected()}')
        self.update_wincap()

        number_of_connected_windows = len(self.l2windows)
        self.launch_window()
        self.send_message(f'Number of connected windows_3 {self.get_l2hash_connected()}')
        if len(self.l2windows) == number_of_connected_windows + 1:
            self.login_window(character, self.l2windows[-1])
            self.send_message(f'Window {self.l2windows[-1].hwnd} completed relog')
            self.l2windows[-1].character = character
            self.l2windows[-1].logged = True
        else:
            self.send_message(f'РЕЛОГ ПОШЕЛ ПО ПИЗДЕ. НАЧАЛСЯ КОШМАР В ПОЕЗДЕ.')

        return self.l2windows[-1].hwnd

    def relog_fatal_windows(self):
        self.update_wincap()
        time.sleep(1)
        launched_unique, connected_unqiue = self.verify_launched_and_connected_hwnds()
        number_of_logged_windows = len(self.get_logged_windows())
        old_hwnds = []
        new_hwnds = []
        if not connected_unqiue:
            self.send_message('PIZDEC............def relog_fatal_windows')

        for hwnd in connected_unqiue:
            window = self.find_hwnd_in_windows(hwnd)
            if window.logged:
                old_hwnds.append(hwnd)
                new_hwnd = self.relog_window(window)
                new_hwnds.append(new_hwnd)

        self.send_message(f'Launched windows {self.get_l2hash_launched()}')
        self.send_message(f'Connected windows: {self.get_l2hash_connected()}')
        self.send_message(f'Connected characters: {self.get_character_names_connected()}')

        if len(self.get_logged_windows()) != number_of_logged_windows:
            _, new_hwnds = self.relog_all_windows()
            time.sleep(2)

        self.send_message('Fatal error is complete')

        return old_hwnds, new_hwnds

    def drop_window_from_list(self, window):
        id = self.l2windows.index(window)
        self.l2windows.pop(id)

    def relog_all_windows(self):

        l2_hwnds_launched = self.get_l2hash_connected()

        if not len(l2_hwnds_launched):
            return

        old_l2_hwnds_connected = self.get_l2hash_connected()
        self.send_message(f'Relog all L2 windows: {old_l2_hwnds_connected}')
        connected_characters = self.get_characters_connected()

        self.close_all_windows()

        time.sleep(3)
        new_hwnds = []
        for character in connected_characters:
            number_of_connected_windows = len(self.l2windows)
            self.send_message(f'Number of connected windows_00 {self.get_l2hash_connected()}')
            self.launch_window()
            self.send_message(f'Number of connected windows_11 {self.get_l2hash_connected()}')
            if len(self.l2windows) == number_of_connected_windows + 1:
                self.login_window(character, self.l2windows[-1])
                new_hwnds.append(self.l2windows[-1].hwnd)
                self.send_message(f'Window {self.l2windows[-1].hwnd} completed relog')
                self.l2windows[-1].character = character
                self.l2windows[-1].logged = True
            else:
                self.send_message(f'РЕЛОГ ПОШЕЛ ПО ПИЗДЕ. НАЧАЛСЯ КОШМАР В ПОЕЗДЕ.')

        self.send_message(f'Launched windows {self.get_l2hash_launched()}')
        self.send_message(f'Connected windows: {self.get_l2hash_connected()}')
        self.send_message(f'Connected characters: {self.get_character_names_connected()}')
        self.send_message('Я ЗАКОНЧИЛ РЕЛОГИН. ЧТО ДАЛЬШЕ?')

        return old_l2_hwnds_connected, new_hwnds

    def verify_launched_and_connected_hwnds(self):
        """
        returns list of launched hwnds, list of connected hwnds
        """
        l2windows_name, hwnd_laucnhed_list = self._get_l2windows_param()
        hwnd_connected_list = [window.hwnd for window in self.l2windows if window]

        if collections.Counter(hwnd_laucnhed_list) == collections.Counter(hwnd_connected_list):
            return [], []

        f = lambda list1, list2: list(filter(lambda element: element not in list2, list1))

        hwnd_connected_unique = f(hwnd_connected_list, hwnd_laucnhed_list)
        hwnd_laucnhed_unique = f(hwnd_laucnhed_list, hwnd_connected_list)

        return hwnd_laucnhed_unique, hwnd_connected_unique

    def verify_launched_and_connected_winnames(self):
        """
        returns list of launched hwnds, list of connected hwnds
        """
        winname_laucnhed_list, hwnd_laucnhed_list = self._get_l2windows_param()
        winname_connected_list = [window.hwnd for window in self.l2windows if window]

        if collections.Counter(winname_laucnhed_list) == collections.Counter(winname_connected_list):
            return [], []

        f = lambda list1, list2: list(filter(lambda element: element not in list2, list1))

        winname_connected_unique = f(winname_connected_list, winname_laucnhed_list)
        winname_laucnhed_unique = f(winname_laucnhed_list, winname_connected_list)

        return winname_laucnhed_unique, winname_connected_unique

    def connect_new_window(self, hwnd, window_name):
        """
        запускается в самом начале программы и при каждом запуске окна

        """
        first_unused_id = self.find_first_unused_window_id()
        temp_window = L2window(first_unused_id, self.wincap, window_name, hwnd, self.screenshot)
        temp_window.connected = True
        self.l2windows.append(temp_window)
        temp_window.enum_handler()

    def find_first_unused_window_id(self):
        ids = []
        if self.l2windows:
            ids = [window.window_id for window in self.l2windows]
            self.send_message(f'find_first_unused_window_id ids {ids}')
        if not ids:
            return 0
        first_unused_id = max(ids) + 1
        ids.sort()
        for i in range(len(self.l2windows)):
            if i != ids[i]:
                first_unused_id = i
        self.send_message(f'first_unused_id {first_unused_id}')
        return first_unused_id

    def initial_connect_windows(self):
        winname_laucnhed_list, hwnd_laucnhed_list = self._get_l2windows_param()

        def callback(hwnd, extra):
            rect = win32gui.GetWindowRect(hwnd)
            x = rect[0]
            y = rect[1]
            w = rect[2] - x
            h = rect[3] - y
            print("Window %s:" % win32gui.GetWindowText(hwnd))
            print(f"Location: x = {x} y = {y}")

        new_hwnd_list = []
        for hwnd in hwnd_laucnhed_list:
            rect = win32gui.GetWindowRect(hwnd)
            x = rect[0]
            y = rect[1]
            # win32gui.EnumWindows(callback, None)
            self.send_message(f'TEST x, y = {x}, {y}')
            for i in range(len(hwnd_laucnhed_list)):
                if x == L2window.width * i:
                    new_hwnd_list.append(hwnd)

        if len(new_hwnd_list) != len(hwnd_laucnhed_list):
            self.send_message('error initial_connect_windows')
            new_hwnd_list = hwnd_laucnhed_list

        for hwnd in new_hwnd_list:
            id = hwnd_laucnhed_list.index(hwnd)
            window_name = winname_laucnhed_list[id]

            self.connect_new_window(hwnd, window_name)

        self.update_wincap()

    def connect_windows(self):
        """
        the function establishes a dependency between hwnds of declared windows and hwnds of launched windows

        3 situations:

        case 1. launched windows = 0, connected windows > 0
        case 2. connected windows < launched windows
        case 3. launched windows = connected windows
        case 4. connected windows > launched windows
        """
        self.send_message('Connecting windows')
        hwnd_laucnhed_unique, hwnd_connected_unique = self.verify_launched_and_connected_hwnds()
        winnames_launched_unique, winnames_connected_unique = self.verify_launched_and_connected_winnames()

        # for window in self.l2windows:
        #     if window.hwnd in hwnd_connected_unique:
        #         window.hwnd = hwnd_laucnhed_unique.pop()

        for hwnd in hwnd_laucnhed_unique:
            id = hwnd_laucnhed_unique.index(hwnd)
            window_name = winnames_launched_unique[id]
            self.connect_new_window(hwnd, window_name)

        self.update_wincap()

    def find_hwnd_in_windows(self, hwnd):
        if self.l2windows:
            for window in self.l2windows:
                if window.hwnd == hwnd:
                    return window
        return None

    def find_id_in_windows(self, id):
        if self.l2windows:
            for window in self.l2windows:
                if window.window_id == id:
                    return window
        return None

    def _get_l2windows_param(self):
        hash_list = []
        name_list = []

        for window in self._list_window_names():
            if window[1] == self.personal_settings.l2window_name_login or window[
                1] == self.personal_settings.l2window_name_game:
                name_list.append(window[1])
                hash_list.append(window[0])
        return name_list, hash_list

    def _list_window_names(self):
        temp = []

        def win_enum_handler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                temp.append([hwnd, win32gui.GetWindowText(hwnd)])

        win32gui.EnumWindows(win_enum_handler, None)

        windows_param = temp
        return windows_param

    def get_l2hash_launched(self):
        l2windows_name, l2windows_hwnd = self._get_l2windows_param()
        return l2windows_hwnd

    def get_l2hash_connected(self):
        if self.l2windows:
            return [window.hwnd for window in self.l2windows]
        else:
            return []

    def get_logged_windows(self):
        logged_windows = []
        if self.l2windows:
            logged_windows.extend([window for window in self.l2windows if window.logged])
        return logged_windows

    def get_characters_connected(self):
        characters = []
        if self.l2windows:

            for window in self.l2windows:
                if window.character is not None:
                    characters.append(window.character)
        return characters

    def get_character_names_connected(self):
        character_names = []
        if self.l2windows:
            for window in self.l2windows:
                if window.character is not None:
                    character_names.append(window.character.name)
        return character_names

    def get_available_character_names(self):
        character_names = []
        if self.available_characters:
            for character in self.available_characters:
                character_names.append(character.name)
            return character_names

    def close_l2_window(self, hwnd):
        try:
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
        except:
            pass
