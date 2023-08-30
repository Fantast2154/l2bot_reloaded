import time

import keyboard
import pyperclip

from system.vision import Vision
from system.l2window import L2window


class LoginModule:
    library = {}
    screenshot = None
    win_capture = None

    def __init__(self, wincap, q):
        self.send_message(f'login module created')
        self.q = q
        self.library = {}
        self.logins = {}
        self.passwords = {}
        self.win_capture = wincap
        self.accurate_search = False
        self.screenshot_accurate = None
        self.init_image_database = [

            ['pumping', 'images/fishing/pumping.jpg', 0.87],
            ['reeling', 'images/fishing/reeling.jpg', 0.87],
            ['logging', 'images/login/stages/logging.jpg', 0.6],
            ['login', 'images/login/stages/login.jpg', 0.8],
            ['login_field', 'images/login/stages/login_field2.jpg', 0.99],
            ['pass_field', 'images/login/stages/pass_field2.jpg', 0.97],
            ['select', 'images/login/stages/select.jpg', 0.6],
            ['server', 'images/login/stages/server.jpg', 0.6],
            ['terms', 'images/login/stages/terms.jpg', 0.6],
            ['character', 'images/login/stages/character.jpg', 0.6],
            ['loading', 'images/login/stages/loading_icon.jpg', 0.6],
            ['menu', 'images/login/stages/menu_quests.jpg', 0.91],
            ['cancel', 'images/login/stages/cancel.jpg', 0.91],
            ['relogin', 'images/login/stages/relogin.jpg', 0.92],
            ['disagree', 'images/login/stages/disagree.jpg', 0.92]]

        self.init_images()

    def window_login(self, log, pas, window):
        self.passwords[window.hwnd] = pas
        self.logins[window.hwnd] = log
        self.window = window
        # self.send_message(f'login: {log}')
        # self.send_message(f'password:{pas}')
        self.send_message(f'hwnd: {window.hwnd}')

        self.join_the_game(window)


    def __del__(self):
        self.send_message(f"login module destroyed")

    def join_the_game(self, window):
        # windows_to_restart = []

        # self.q.new_task('LEFT', [[(100, 100)]], window)
        # self.click([[(100, 100)]], window)
        # time.sleep(1)
        self.send_message('join_the_game')
        joined, win = self.stages(window)
        if not joined:
            self.send_message(f'window {window.whnd} NOT JOINED ')
            # windows_to_restart.append(win)
        # return windows_to_restart

    def stages(self, window):
        self.send_message('1')
        login_password_stage_delay_started = False
        terms_stage_delay_started = False
        select_server_stage_delay_started = False
        select_character_stage_delay_started = False
        loading_stage_delay_started = False
        joined = False
        fisrt_time = True
        t_prev = 0
        time_stage_delay = 0

        login_field = []
        pass_field = []
        login = []
        while not joined:
            self.send_message('2')
            login_pos = self.find('login', window)
            terms_pos = self.find('terms', window)
            server_pos = self.find('server', window)
            select_pos = self.find('select', window)
            menu_pos = self.find('menu', window)
            cancel_pos = self.find('cancel', window)
            disagree_pos = self.find('disagree', window)
            relogin_pos = self.find('relogin', window)

            if login_pos:
                stage = 'login_password'
                if not login_password_stage_delay_started:
                    login_password_stage_delay_started = True
                    time_stage_delay = time.time()

            elif terms_pos:
                stage = 'terms_of_conditions'
                if not terms_stage_delay_started:
                    terms_stage_delay_started = True
                    time_stage_delay = time.time()
            elif server_pos:
                stage = 'select_server'
                if not select_server_stage_delay_started:
                    select_server_stage_delay_started = True
                    time_stage_delay = time.time()
            elif select_pos:
                stage = 'select_character'
                if not select_character_stage_delay_started:
                    select_character_stage_delay_started = True
                    time_stage_delay = time.time()
            elif menu_pos:
                self.send_message(f'{window.hwnd} И Г Р А!!!')
                stage = 'game'
                time_stage_delay = time.time()
                return True, 0

            else:
                stage = 'loading'
                if not loading_stage_delay_started:
                    loading_stage_delay_started = True
                    time_stage_delay = time.time()

            self.send_message('3')
            if time.time() - time_stage_delay >= 5:

                if cancel_pos:
                    (x, y) = cancel_pos[-1]
                    cancel = [(x, y)]
                    self.click(cancel, window)
                    loading_stage_delay_started = False

                elif disagree_pos:
                    (x, y) = disagree_pos[-1]
                    disagree = [(x, y)]
                    self.click(disagree, window)
                    loading_stage_delay_started = False

                elif relogin_pos:
                    (x, y) = relogin_pos[0]
                    relogin = [(x, y)]
                    self.click(relogin, window)
                    loading_stage_delay_started = False

                login_password_stage_delay_started = False
                terms_stage_delay_started = False
                select_server_stage_delay_started = False
                select_character_stage_delay_started = False

                if time.time() - time_stage_delay >= 35:
                    print('Окно', window.hwnd, 'вход неуспешный.')
                    print('ТРЕБУЕТСЯ ПОЛНЫЙ ПЕРЕЗАПУСК')
                    return False, window
            self.send_message('4')
            if stage == 'login_password':
                # print(window.hwnd, 'Стадия ввода логина и пароля')
                # print(window.hwnd, 'Расчитываю...')
                # time.sleep(0.5)
                # print(window.hwnd, 'Вычисляю...')
                self.send_message('5')
                if fisrt_time:
                    while not login:
                        login = self.find('login', window)
                    (x, y) = login[0]
                    login_field = [(x, y - 60)]
                    pass_field = [(x, y - 35)]
                    fisrt_time = False

                self.login(window, login_field, pass_field)
                # print(window.hwnd, 'Авторизация прошла успешно. Вроде...')
                time.sleep(2)

            elif stage == 'terms_of_conditions':
                # print(window.hwnd, 'Принятие пользовательского соглашения. БОТЫ ЗАПРЕЩЕНЫ!!!')
                # keyboard.send('enter')
                self.q.new_task('ctrlv', 'enter', window)
                time.sleep(2)

            elif stage == 'select_server':
                # print(window.hwnd, 'Стадия выбора сервера')
                # keyboard.send('enter')
                self.q.new_task('ctrlv', 'enter', window)
                time.sleep(2)

            elif stage == 'select_character':
                # print(window.hwnd, 'Стадия выбора персонажа')
                # keyboard.send('enter')
                self.q.new_task('ctrlv', 'enter', window)
                time.sleep(3)

            elif stage == 'loading':
                continue

            elif stage == 'game':
                print('Login is complete')
                return True, 0

    def click(self, button_pos, window):
        # self.q.new_task('mouse',
        #                 [button_pos, True, 'LEFT', False, 'double', 'NoRand'],
        #                 window)
        self.q.new_task('LEFT', [button_pos], window)

    def double_click(self, button_pos, window):
        # self.q.new_task('mouse',
        #                 [button_pos, True, 'LEFT', False, 'double', 'NoRand'],
        #                 window)
        self.q.new_task('DOUBLE', [button_pos], window)

    def login(self, window, login_field, pass_field):
        if login_field and pass_field:
            # self.q.new_task('mouse',
            #                 [login_field, True, 'LEFT', False, False, False],
            #                 window)
            self.click(login_field, window)
            time.sleep(0.1)
            # self.q.new_task('mouse',
            #                 [login_field, True, 'LEFT', False, 'double', 'NoRand'],
            #                 window)
            self.double_click(login_field, window)
            time.sleep(1)
            pyperclip.copy(self.logins[window.hwnd])
            time.sleep(0.1)
            # keyboard.send('ctrl+v')
            self.q.new_task('ctrlv', 'ctrl+v', window)
            time.sleep(1)
            # self.q.new_task('mouse',
            #                 [pass_field, True, 'LEFT', False, False, False],
            #                 window)
            self.click(pass_field, window)
            time.sleep(0.1)
            # self.q.new_task('mouse',
            #                 [pass_field, True, 'LEFT', False, 'double', 'NoRand'],
            #                 window)
            self.double_click(pass_field, window)
            time.sleep(1)
            pyperclip.copy(self.passwords[window.hwnd])
            time.sleep(0.1)
            # keyboard.send('ctrl+v')
            self.q.new_task('ctrlv', 'ctrl+v', window)
            time.sleep(0.5)
            self.q.new_task('ctrlv', 'enter', window)
            # keyboard.send('enter')
            time.sleep(1)

    def update_screenshot(self, window):
        while True:
            screenshot = window.screenshot
            if not screenshot[0]:
                continue
            hwnd = window.hwnd

            # print(screenshot)
            temp = screenshot[-1][hwnd][0]
            if len(temp) != 0:
                return temp
            else:
                self.send_message('no screenshot')
                return []

    def send_message(self, message):
        print(str(self.__class__.__name__) + ': ' + str(message))

    def find(self, object, window):  # returns list of positions
        try:
            position = self.library[object][0].find(window.update_screenshot())
            return position
        except KeyError:
            # self.send_message(f'find function ERROR object search')
            # self.send_message(f'{KeyError}')
            return []

    def init_images(self):
        for obj in self.init_image_database:
            try:
                self.library[f'{obj[0]}'] = [Vision(obj[1], obj[2]), None]
            except:
                print('Error finding images')


