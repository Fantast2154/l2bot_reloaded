from bots.farmer.farming_window import FarmingWindow
from system.vision import Vision


class DamagerWindow(FarmingWindow):
    """
        This class contains all information about the window, image recognition, search and positioning

        Also contains the following important variables:
        screenshot
        wincap
        hwnd
        window_id

        and functions:
        def _send_message()
        def find()
        """
    def __init__(self, l2window):
        super().__init__(l2window.personal_settings, l2window.window_id, l2window.wincap, l2window.window_name, l2window.hwnd, l2window.screenshot)





