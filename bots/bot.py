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
    bot_id = 0

    def _send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))


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

    @abstractmethod
    def _run(self):
        pass
