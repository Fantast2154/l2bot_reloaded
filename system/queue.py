from time import sleep
from multiprocessing import Manager

from mathematics.vectors import Vector2i
from system.task import MouseTask, KeyboardTask, ClickType
from system.action_service import Mouse, Keyboard


class ActionQueue:
    def send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))

    def __init__(self):
        self.send_message('has been created')
        manager = Manager()
        self.is_running = manager.list()
        self.is_running.append(True)
        self.tasks = manager.list()
        self.queue_list = manager.list()
        self.last_active_window = 0
        self.queue_delay = 0.2

    def start(self):
        self.send_message('start queueing')
        self.is_running[0] = True
        self._run()

    def stop(self):
        self.send_message('stop queueing')
        self.is_running[0] = False

    def new_task(self, pending_task: MouseTask | KeyboardTask) -> None:
        self.queue_list.append(1)
        self.tasks.append(pending_task)

    def coords_local_to_global(self, coordinates: Vector2i, window) -> Vector2i:
        deltaX = window.wincap.offset_x[window.window_id]
        deltaY = window.wincap.offset_y[window.window_id]

        return coordinates + Vector2i(deltaX, deltaY)

    def task_execution(self, task: MouseTask | KeyboardTask):
        """
        action: LEFT, RIGHT, drag_n_drop, turn, double, no_click
        coordinates: [(x, y)] or [(x1, y1), (x2, y2), ..]
        """

        if type(task) is MouseTask:
            position = self.coords_local_to_global(task.click_position, task.window)

            if task.window.hwnd != self.last_active_window:
                self.last_active_window = task.window.hwnd
                Mouse.activate_window(position)

            if task.click_type == ClickType.LEFT:
                Mouse.click_left(position)
            elif task.click_type == ClickType.DOUBLE_LEFT:
                Mouse.double_click_left(position)
            elif task.click_type == ClickType.RIGHT:
                Mouse.click_right(position)
            elif task.click_type == ClickType.NO_CLICK:
                Mouse.no_click(position)
            elif task.click_type == ClickType.SCROLL_DOWN:
                Mouse.scroll_down(position)
            elif task.click_type == ClickType.SCROLL_UP:
                Mouse.scroll_up(position)
        else:
            Keyboard.ctrlv(task.button)

    def _run(self):

        while self.is_running[0]:
            self.send_message('Run')
            sleep(self.queue_delay)
            try:
                if self.tasks:
                    task = self.tasks.pop(0)
                else:
                    continue

                self.task_execution(task)
            finally:
                pass
