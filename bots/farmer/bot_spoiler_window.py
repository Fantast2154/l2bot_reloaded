from bots.farmer.farming_window import FarmingWindow


class SpoilerWindow(FarmingWindow):
    def __init__(self, l2window):
        super().__init__(l2window.personal_seetings, l2window.window_id, l2window.wincap, l2window.window_name, l2window.hwnd, l2window.screenshot)