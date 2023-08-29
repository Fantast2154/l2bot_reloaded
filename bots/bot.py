from abc import ABC, abstractmethod


class Bot(ABC):
    """
    abstract class for bots

    status values:
    0 - created
    1 - working
    2 - paused
    3 - waiting
    4 - error
    """

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def _run(self):
        pass
