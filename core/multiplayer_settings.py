from pygame import *
import time
from core.key_bindings import KeyBindings
from objects.interface.button import Button
from objects.interface.selector import Selector
from objects.interface.text import Text
from settings import server_port

class MultiplayerSettings:
    def __init__(self, menu):
        self.menu = menu
        self.step1()

    def step1(self):
        w = self.menu.screen.get_width()
        self.selector = None
        self.selector = Selector([
            Button("Запустить сервер", (w / 2, 240)),
            Button("Подключиться к серверу", (w / 2, 360)),
        ])
        self.menu.objects = self.selector.buttons
        time.sleep(0.1) # ждем, пока пользователь отпустит кнопку пробела
        KeyBindings.register(K_SPACE, self.step1_handler)

    def step1_handler(self):
        KeyBindings.deregister(K_SPACE)
        self.selector.close()
        self.menu.clear_screen()
        self.menu.game.loop.force_rerender()

        if self.selector.active == 0: # мы сервер
            self.server_step1()
        else: # мы клиент
            pass

    def server_step1(self):
        print('server step 1')
        w = self.menu.screen.get_width()
        self.menu.objects.append(Text("Ждем подключений", offset=(w / 2, 100), size=20, type=Text.TYPE__BOLD))

        self.pos = 150

        def log(text, type=Text.TYPE__REGULAR):
            self.pos += 30
            self.menu.objects.append(Text(text, offset=(w / 2, self.pos), size=18, type=type))


        print('server start')
        log("Запуск сервера...")
        self.menu.game.loop.force_rerender()

        print('getting ip')
        self.menu.game.create_server()
        log('Сервер запущен. Получаем внешний IP-адрес...')
        self.menu.game.loop.force_rerender()

        ip = self.menu.game.server.get_machine_ip()
        print(ip)
        log('IP получен')
        log('Ваш IP адрес: %s, порт: %s' % (ip, server_port), Text.TYPE__BOLD)
        log('Ждем подключения второго игрока...')
        self.menu.game.loop.force_rerender()

        print('waiting for connections')
        self.menu.game.server.waiting_for_connect()
