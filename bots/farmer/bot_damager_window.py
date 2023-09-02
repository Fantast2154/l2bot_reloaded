from bots.farmer.farming_window import FarmingWindow
from user_props.personal_settings_blank import PersonalSettingsBlank
# from system.vision import Vision


class DamagerWindow(FarmingWindow):
    def __init__(self, l2window):
        super().__init__(l2window.personal_settings, l2window.window_id, l2window.wincap, l2window.window_name, l2window.hwnd, l2window.screenshot)


