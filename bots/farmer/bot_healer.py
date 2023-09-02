from bots.bot import Bot


class BotHealer(Bot):

    def __init__(self, damager_window, q):
        self._send_message('has been created')

    def start(self):
        self._send_message('started')
        self._run()

    def stop(self):
        self._send_message('stopped')

    def _run(self):
        pass