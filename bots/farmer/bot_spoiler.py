from bots.bot import Bot


class BotSpoiler(Bot):

    def __init__(self, damager_window, q):
        pass

    def start(self):
        self._send_message('started')
        self._run()

    def stop(self):
        self._send_message('stopped')

    def _run(self):
        pass
