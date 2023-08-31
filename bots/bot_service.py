from abc import ABC, abstractmethod
from time import sleep

class BotService(ABC):
    bot_processes = []
    bots = []
    exit_is_set = False

    # @abstractmethod
    # def create_bot(self):
    #     pass

    def _send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))

    def start_bot(self, bot):
        sleep(1)
        if bot in self.bots and len(self.bots) == len(self.bot_processes):
            self._send_message('bot started')
            self.bot_processes[bot.id].start()
        else:
            raise 'Error start_bot'

    def stop_bot(self, bot):
        sleep(1)

        if bot in self.bots and len(self.bots) == len(self.bot_processes):
            self._send_message('bot stopped')
            bot.stop()
            self.bot_processes[bot.id].join()
        else:
            raise 'Error stop_bot'

    def stop_bots(self):
        if len(self.bots) == len(self.bot_processes):
            self._send_message('all bots stopped')
            for bot in self.bots:
                bot.stop()

            for process in self.bot_processes:
                process.join()

    def pause_bot(self, bot):

        if bot in self.bots and len(self.bots) == len(self.bot_processes):
            self._send_message('bot paused')
            bot.pause()
        else:
            raise 'Error pause_bot'

    def resume_bot(self, bot):
        if bot in self.bots and len(self.bots) == len(self.bot_processes):
            bot.resume()
        else:
            raise 'Error resume_bot'

    def resume_bots_which_paused(self):
        pass

    # @abstractmethod
    # def _run(self):
    #     pass

    def stop(self):
        self.exit_is_set = True
        self.stop_bots()
        sleep(3)
        self._send_message('stopped')
