from abc import ABC, abstractmethod
from enum import Enum


class BotStatus(Enum):
    CREATED = 0
    WORKING = 1
    PAUSED = 2
    WAITING = 3
    ERROR = 4


class Bot(ABC):
    """
    abstract class for bots
    TODO: USE BotStatus enum for declaring bot status
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
