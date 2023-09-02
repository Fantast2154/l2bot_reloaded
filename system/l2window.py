import win32gui


class L2window:

    width = 800
    height = 800

    def send_message(self, message):
        print('{} {}: {}'.format(self.__class__.__name__, self.window_id, str(message)))

    def __init__(self, personal_settings, window_id, wincap, window_name, hwnd, screenshot):
        print('1')

        self.window_id = window_id
        self.personal_settings = personal_settings
        x = 0
        y = 0
        # self.width = 630
        # self.height = 710
        self.width = 800
        self.height = 800
        self.left_top_x = self.width * window_id + x
        self.left_top_y = y
        self.width = self.width
        self.height = self.height
        print('2')
        self.screenshot = screenshot
        print('3')
        self.window_name = window_name
        print('4')
        self.hwnd = hwnd
        self.wincap = wincap
        print('5')
        self.owner = None

        self.send_message(f'has been created')

    def update_screenshot(self):
        temp = self.screenshot[-1][self.hwnd][0]
        if len(temp) != 0:
            return temp
        else:
            return []

    def enum_handler(self):
        if win32gui.IsWindowVisible(self.hwnd):
            if self.window_name in win32gui.GetWindowText(self.hwnd):
                win32gui.MoveWindow(self.hwnd, self.left_top_x, self.left_top_y, self.width, self.height, True)
