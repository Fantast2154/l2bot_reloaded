from multiprocessing import Manager
import time
import os
import win32gui
import win32con


class L2WindowManager:
    def send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))

    def __init__(self, controller):
        self.controller = controller
        self.personal_settings = controller.personal_settings
        self.wincap = controller.wincap
        self.manager = Manager()
        self.screenshot = self.manager.list()
        self.screenshot.append(0)
        self.number_of_opened_windows = 0

    def _get_l2windows_param(self):
        hash_list = []
        name_list = []

        for window in self._list_window_names():
            if window[1] == self.personal_settings.l2window_name:
                name_list.append(window[1])
                hash_list.append(window[0])
        return name_list, hash_list

    def _list_window_names(self):
        temp = []

        def win_enum_handler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                # temp.append([hex(hwnd), win32gui.GetWindowText(hwnd)])
                temp.append([hwnd, win32gui.GetWindowText(hwnd)])

        win32gui.EnumWindows(win_enum_handler, None)

        windows_param = temp
        return windows_param

    def launch_window(self):
        self.send_message('launching L2 window')
        name_list, hash_list = self._get_l2windows_param()
        n = len(name_list)

        os.startfile(self.personal_settings.launcher_path)
        t = time.time()
        counter = 0
        while time.time() - t < 40:
            _, l2windows_hwnd = self._get_l2windows_param()
            if len(l2windows_hwnd) == n + 1:
                time.sleep(2)
                break
            counter += 1
            time.sleep(1)
            self.send_message(f'Launching..{counter}')

    def close_window(self, hwnd):
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
