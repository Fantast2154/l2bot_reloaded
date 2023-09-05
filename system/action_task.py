from enum import Enum

from mathematics.vectors import Vector2i


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
    click_position = Vector2i(0, 0)

    def __init__(self, click_type: ClickType, click_position: Vector2i, window):
        self.click_type = click_type
        self.click_position = click_position
        self.window = window


class KeyboardTask(Task):
    button = None
    hold: float = 0.0

    def __init__(self, press_type, window, hold: float = 0.0):
        self.button = press_type
        self.hold = hold
        self.window = window
