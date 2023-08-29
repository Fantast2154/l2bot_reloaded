from enum import Enum


class ClickType(Enum):
    LEFT = 0
    DOUBLE_LEFT = 1
    RIGHT = 2
    SCROLL_UP = 3
    SCROLL_DOWN = 4
    DRAG_N_DROP_LEFT = 5
    DRAG_N_DROP_RIGHT = 6
    WHEEL_SCROLL = 7
    NO_CLICK = 8


class Task:
    pass


class MouseTask(Task):
    """
    click options: LEFT, RIGHT, scroll_up, drag_n_drop_left, drag_n_drop_right
    """
    click_type = ClickType.LEFT
    coordinates = None

    def __init__(self, cl_type: ClickType, cl_coordinates, window):
        self.click_type = cl_type
        self.coordinates = cl_coordinates
        self.window = window


class KeyboardTask(Task):
    button = None
    hold = False

    def __init__(self, press_type, hold, window):
        self.button = press_type
        self.hold = hold
        self.window = window
