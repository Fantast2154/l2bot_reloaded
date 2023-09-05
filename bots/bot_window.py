from system.l2window import L2window
from system.vision import Vision
import warnings
from enum import Enum
from mathematics.vectors import Vector2i, EmptyVector


class SearchParam(Enum):
    SEARCH_FULL_WINDOW = 0
    SEARCH_SCREEN_CENTER = 1
    SEARCH_CHAT = 2
    SEARCH_ITEMS = 3
    SEARCH_BROKER_MENU = 4


class VisionLibrary:

    def __init__(self):
        self.library = {}

    def add_image(self, name:str, vision_obj: Vision):
        if not self.library.get(name, False):
            self.library[name] = vision_obj

    def get_image(self, name) -> Vision | None:
        return self.library.get(name, None)


class LastPositionLibrary:

    def __init__(self):
        self.library = {}

    def add_pos(self, name: str, pos: Vector2i) -> None:
        if not self.library.get(name, False):
            self.library[name] = pos

    def get_pos(self, name) -> Vector2i | EmptyVector:
        return self.library.get(name, Vector2i.empty())


class BotWindow(L2window):
    vision_library = VisionLibrary()
    last_pos = LastPositionLibrary()
    """The database of images that are required to find on the screen after launching"""
    init_image_database = {
        'disconnect_window': ('images/disconnect_EN.jpg', 0.40)
    }

    extended_image_database = [

    ]

    def _send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))

    def _warn_message(self, message):
        warnings.warn(str(self.__class__.__name__) + ': ' + str(message))

    def init_images(self, input_images: dict):

        for key, value in input_images.items():
            try:
                image_name = key
                image_path = value[0]
                image_recognition_accuracy = value[1]
                vision_obj = Vision(image_path, image_recognition_accuracy)
                self.vision_library.add_image(image_name, vision_obj)
            except:
                self._warn_message('Error loading images')

    def get_screenshot(self):
        temp = self.screenshot[-1][self.hwnd][0]
        if len(temp) != 0:
            return temp
        else:
            return []

    def get_sliced_screenshot(self, pos1: Vector2i, pos2: Vector2i):
        screenshot = self.get_screenshot()
        sliced_screenshot = screenshot[pos1.y: pos1.y + pos2.y, pos1.x: pos1.x + pos2.x]
        return sliced_screenshot

    def _find(self, elem: str, search_param: SearchParam = SearchParam.SEARCH_FULL_WINDOW) -> Vector2i | EmptyVector:
        try:
            if search_param == SearchParam.SEARCH_FULL_WINDOW:
                vision_obj = self.vision_library.get_image(elem)
                if vision_obj is not None:
                    position = vision_obj.find(self.get_screenshot())
                    vec = position[0]
                else:
                    vec = Vector2i.empty()

            else:
                vec = Vector2i.empty()

            return vec

        except KeyError:
            self._warn_message(f'find function ERROR object search')
            self._warn_message(f'{KeyError}')
            return Vector2i.empty()

    def get_object(self, name: str, search: bool = False, save_pos: bool = False,
                   search_param: SearchParam = None) -> Vector2i | EmptyVector:
        if search:
            pos = self._find(name, search_param=search_param)
            if pos:
                if save_pos:
                    self.last_pos.add_pos(name, pos)
                return pos
            else:
                return Vector2i.empty()
        else:
            temp_pos = self.last_pos.get_pos(name)
            if temp_pos:
                return temp_pos
            else:
                temp = 'get_object function ERROR referring to the unknown object: ' + str(name)
                self._warn_message(temp)
                return Vector2i.empty()
