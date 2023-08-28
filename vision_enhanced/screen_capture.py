import threading
import numpy as np
import win32gui
import win32ui
import win32con
from threading import Thread, Lock


class ScreenCapture(threading.Thread):
    stopped = True
    lock = None
    screenshot = []

    my_x = 0
    my_y = 0
    # properties
    w = 0
    h = 0
    w_init = 0
    h_init = 0

    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0

    windows_param = []
    windows_list = []

    def __init__(self, window_name=None):
        # self.send_message(f'TEST ScreenshotMaster created\n')
        threading.Thread.__init__(self)
        self.exit = threading.Event()
        self.screenshot = []
        self.lock = Lock()

        # find the handle for the window we want to capture.
        # if no window name is given, capture the entire screen
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                self.send_message(f'Window not found: {window_name}')

        # get the window size
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]
        self.w_init = window_rect[2] - window_rect[0]
        self.h_init = window_rect[3] - window_rect[1]

        self.my_x = window_rect[0]
        self.my_y = window_rect[1]

        if not window_name is None:
            # account for the window border and titlebar and cut them off
            border_pixels = 8
            titlebar_pixels = 30
            self.w = self.w - (border_pixels * 2)
            self.h = self.h - titlebar_pixels - border_pixels
            self.cropped_x = border_pixels
            self.cropped_y = titlebar_pixels

            # set the cropped coordinates offset so we can translate screenshot
            # images into actual screen positions
            self.offset_x = window_rect[0] + self.cropped_x
            self.offset_y = window_rect[1] + self.cropped_y

    def set_windows(self, windows_list):
        if windows_list:
            self.windows_list = windows_list

    def __del__(self):
        self.send_message(f'TEST ScreenshotMaster destroyed')

    # @classmethod
    def capture_screen(self, accurate=False, object_position=(0, 0), object_size=(100, 100)):

        # get the window image data
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()

        if accurate:
            (xx, yy) = object_position
            (ww, hh) = object_size
            # dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
            dataBitMap.CreateCompatibleBitmap(dcObj, ww, hh)
            cDC.SelectObject(dataBitMap)
            cDC.BitBlt((0, 0), (ww, hh), dcObj, (self.cropped_x + xx, self.cropped_y + yy), win32con.SRCCOPY)
            # cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

            # convert the raw data into a format opencv can read
            # dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
            signedIntsArray = dataBitMap.GetBitmapBits(True)
            img = np.fromstring(signedIntsArray, dtype='uint8')
            img.shape = (hh, ww, 4)
            # img.shape = (self.h, self.w, 4)

        else:
            dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
            cDC.SelectObject(dataBitMap)
            cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

            # convert the raw data into a format opencv can read
            # dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
            signedIntsArray = dataBitMap.GetBitmapBits(True)
            img = np.fromstring(signedIntsArray, dtype='uint8')
            img.shape = (self.h, self.w, 4)

        # free resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        # drop the alpha channel, or cv.matchTemplate() will throw an error like:
        #   error: (-215:Assertion failed) (depth == CV_8U || depth == CV_32F) && type == _templ.type()
        #   && _img.dims() <= 2 in function 'cv::matchTemplate'
        img = img[..., :3]

        # make image C_CONTIGUOUS to avoid errors that look like:
        #   File ... in draw_rectangles
        #   TypeError: an integer is required (got type tuple)
        # see the discussion here:
        # https://github.com/opencv/opencv/issues/14866#issuecomment-580207109
        img = np.ascontiguousarray(img)

        return [img]

    def list_window_names(self):
        temp = []
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                # temp.append([hex(hwnd), win32gui.GetWindowText(hwnd)])
                temp.append([hwnd, win32gui.GetWindowText(hwnd)])

        win32gui.EnumWindows(winEnumHandler, None)
        self.windows_param = temp

    def get_windows_param(self):
        return self.windows_param

    def get_screenshot(self, id):
        return self.screenshot

    def send_message(self, message):
        temp = 'screen_capture' + ': ' + message
        print(temp)

    def start_capturing(self):
        pass

    def run(self):
        self.start_capturing()
        while not self.exit.is_set():
            self.screenshot = self.capture_screen()
            # time.sleep(1)

    def stop(self):
        # self.send_message(f'TEST ScreenshotMaster stopped\n')
        self.exit.set()

