from abc import ABC, abstractmethod

class Bot(ABC):

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
