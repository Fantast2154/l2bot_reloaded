from time import sleep
from threading import Thread
from abc import ABC, abstractmethod
from bots.bot import Bot
import warnings

class BotService(ABC):
    bot_processes = {}
    bots = {}
    is_running = False

    def _send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))

    def _warn_message(self, message):
        warnings.warn(str(self.__class__.__name__) + ': ' + str(message))

    # @abstractmethod
    # def create_bot(self):
    #     pass

    def start(self):
        self._send_message('>> started <<')
        self.is_running = True
        thread = Thread(target=self._run)
        thread.start()


    def stop(self):
        self.is_running = False

    def _run(self):
        while self.is_running:
            sleep(5)

    def start_bot(self, bot: int | Bot):
        sleep(2)
        if not len(self.bots) == len(self.bot_processes):
            raise 'Error start_bot'

        if type(bot) == Bot:
            process = self.bot_processes.get(bot.bot_id, None)
            if process is not None:
                process.start()
            else:
                self._warn_message('Could not start the bot')
        elif type(bot) == int:
            process = self.bot_processes.get(bot, None)
            if process is not None:
                process.start()
            else:
                self._warn_message('Could not start the bot')

    def stop_bot(self, bot):
        sleep(1)

        if bot in self.bots and len(self.bots) == len(self.bot_processes):
            self._send_message('bot stopped')
            bot.stop()
            self.bots.pop(bot.id)
            self.bot_processes[bot.id].join()
            self.bot_processes.pop(bot.id)
        else:
            raise 'Error stop_bot'

    def stop_bots(self):
        if len(self.bots) == len(self.bot_processes):
            self._send_message('all bots stopped')
            for i, bot in enumerate(self.bots):
                bot.stop()
                self.bots.pop(i)


            for i, process in enumerate(self.bot_processes):
                process.join()
                self.bot_processes.pop(i)

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
