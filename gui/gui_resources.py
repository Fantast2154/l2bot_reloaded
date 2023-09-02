import os
import pickle

from mathematics.vectors import Vector2i


class GUISettings:
    position = Vector2i(0, 0)
    size = Vector2i(700, 300)


class GUIResources:
    __settings_file = 'gui_settings.pkl'

    window_name = 'baganec & germanec'

    project_root = os.path.dirname(os.path.dirname(__file__))
    header_icon_path = project_root + '/gui/icons/header_icon380x380.png'
    icon_path = project_root + '/gui/icons/online380x380.png'
    save_icon_path = project_root + '/gui/icons/save_icon380x380.png'
    internet_connection_enabled_icon_path = project_root + '/gui/icons/online380x380.png'
    internet_connection_disabled_icon_path = project_root + '/gui/icons/offline380x380.png'
    plus_icon = project_root + '/gui/icons/plus.png'

    def __init__(self):
        pass

    def save_settings(self, settings: GUISettings):
        with open(self.__settings_file, 'wb') as f:
            pickle.dump(settings, f)

    def load_settings(self) -> GUISettings:
        with open(self.__settings_file, 'rb') as f:
            return pickle.load(f)
