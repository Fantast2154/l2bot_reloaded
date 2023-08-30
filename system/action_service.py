from time import sleep
import pynput
import keyboard
from pynput.mouse import Button
from mathematics.vectors import Vector2i


class ActionService:
    # mouse and keyboard stuff
    pass


class Mouse(ActionService):
    mouse = pynput.mouse.Controller()

    @classmethod
    def activate_window(cls, position: Vector2i):
        cls.mouse.position = (position.x, position.y)
        sleep(0.02)
        cls.mouse.press(Button.left)
        sleep(0.02)
        cls.mouse.release(Button.left)
        sleep(0.03)
        cls.mouse.move(4, 4)
        sleep(0.03)

    @classmethod
    def click_left(cls, position: Vector2i):
        cls.mouse.position = (position.x, position.y)
        sleep(0.03)
        cls.mouse.press(Button.left)
        sleep(0.07)
        cls.mouse.release(Button.left)
        sleep(0.1)

    @classmethod
    def double_click_left(cls, position: Vector2i):
        cls.mouse.position = (position.x, position.y)
        sleep(0.03)
        cls.mouse.press(Button.left)
        sleep(0.07)
        cls.mouse.release(Button.left)
        sleep(0.07)
        cls.mouse.press(Button.left)
        sleep(0.07)
        cls.mouse.release(Button.left)
        sleep(0.07)

    @classmethod
    def click_right(cls, position: Vector2i):
        pass

    @classmethod
    def no_click(cls, position: Vector2i):
        cls.mouse.position = (position.x, position.y)
        sleep(.1)
        cls.mouse.release(Button.left)
        sleep(0.03)

    @classmethod
    def scroll_down(cls, position: Vector2i):
        cls.mouse.position = (position.x, position.y)
        sleep(0.1)
        cls.mouse.press(Button.left)
        sleep(0.2)
        cls.mouse.move(0, 150)
        sleep(0.2)
        cls.mouse.release(Button.left)
        sleep(0.4)

    @classmethod
    def scroll_up(cls, position: Vector2i):
        cls.mouse.position = (position.x, position.y)
        sleep(0.1)
        cls.mouse.press(Button.left)
        sleep(0.2)
        cls.mouse.move(0, -150)
        sleep(0.2)
        cls.mouse.release(Button.left)
        sleep(0.4)


class Keyboard(ActionService):
    @classmethod
    def press_button(cls, keyboard_button: str):
        if keyboard_button:
            sleep(0.1)
            keyboard.send(keyboard_button)
            sleep(0.1)
