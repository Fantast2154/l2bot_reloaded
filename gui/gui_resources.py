import os
import pickle

from mathematics.vectors import Vector2i


class GUISettings:
    position = Vector2i(0, 0)
    size = Vector2i(700, 300)


class GUIResources:
    __settings_file = '/gui/gui_settings.pkl'

    window_name = 'baganec & germanec'

    project_root = os.path.dirname(os.path.dirname(__file__))
    header_icon_path = project_root + '/gui/icons/header_icon380x380.png'
    icon_path = project_root + '/gui/icons/online380x380.png'
    save_icon_path = project_root + '/gui/icons/save_icon380x380.png'
    internet_connection_enabled_icon_path = project_root + '/gui/icons/online380x380.png'
    internet_connection_disabled_icon_path = project_root + '/gui/icons/offline380x380.png'
    plus_icon = project_root + '/gui/icons/plus.png'

    start_icon = project_root + '/gui/icons/start_icon380x380.png'
    stop_icon = project_root + '/gui/icons/stop_icon380x380.png'
    pause_icon = project_root + '/gui/icons/pause_icon380x380.png'
    kill_icon = project_root + '/gui/icons/kill_icon380x380.png'
    switch_icon = project_root + '/gui/icons/switch_icon380x380.png'

    active_icon = project_root + '/gui/icons/active_icon380x380.png'
    inactive_icon = project_root + '/gui/icons/inactive_icon380x380.png'
    paused_icon = project_root + '/gui/icons/paused_icon380x380.png'
    busy_icon = project_root + '/gui/icons/busy_icon380x380.png'
    delete_icon = project_root + '/gui/icons/cross.png'

    def __init__(self):
        pass

    def save_settings(self, settings: GUISettings):
        with open(os.path.dirname(os.path.dirname(__file__)) + self.__settings_file, 'wb') as f:
            pickle.dump(settings, f)

    def load_settings(self) -> GUISettings:
        with open(os.path.dirname(os.path.dirname(__file__)) + self.__settings_file, 'rb') as f:
            return pickle.load(f)
