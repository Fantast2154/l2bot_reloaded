import win32gui


class L2window:

    width = 800
    height = 800

    def send_message(self, message):
        print('{} {}: {}'.format(self.__class__.__name__, self.window_id, str(message)))

    def __init__(self, window_id, wincap, window_name, hwnd, screenshot):

        self.window_id = window_id
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

        self.screenshot = screenshot
        self.window_name = window_name
        self.hwnd = hwnd
        self.wincap = wincap
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
