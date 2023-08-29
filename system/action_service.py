from time import sleep
import pynput
from pynput.mouse import Button


class ActionService:
    # mouse and keyboard stuff
    pass


class Mouse(ActionService):
    mouse = pynput.mouse.Controller()

    @classmethod
    def activate_window(cls, x, y):
        position = (x, y)
        cls.mouse.position = position
        sleep(0.02)
        cls.mouse.press(Button.left)
        sleep(0.02)
        cls.mouse.release(Button.left)
        sleep(0.03)
        cls.mouse.move(4, 4)
        sleep(0.03)

    @classmethod
    def click_left(cls, x, y):
        position = (x, y)
        cls.mouse.position = position
        sleep(0.03)
        cls.mouse.press(Button.left)
        sleep(0.07)
        cls.mouse.release(Button.left)
        sleep(0.1)

    @classmethod
    def click_right(cls, x, y):
        pass

    @classmethod
    def no_click(cls, x, y):
        cls.mouse.position = (x, y)
        sleep(.1)
        cls.mouse.release(Button.left)
        sleep(0.03)

    @classmethod
    def scroll_down(cls, x, y):
        position = (x, y)
        cls.mouse.position = position
        sleep(0.1)
        cls.mouse.press(Button.left)
        sleep(0.2)
        cls.mouse.move(0, 150)
        sleep(0.2)
        cls.mouse.release(Button.left)
        sleep(0.4)

    @classmethod
    def scroll_up(cls, x, y):
        position = (x, y)
        cls.mouse.position = position
        sleep(0.1)
        cls.mouse.press(Button.left)
        sleep(0.2)
        cls.mouse.move(0, -150)
        sleep(0.2)
        cls.mouse.release(Button.left)
        sleep(0.4)


class Keyboard(ActionService):
    pass
