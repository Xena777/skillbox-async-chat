#
# Серверное приложение для соединений
#
import asyncio
from asyncio import transports
from typing import Optional


class ServerProtocol(asyncio.Protocol):
    login: str = None
    server: 'Server'
    transport: transports.Transport

    def __init__(self, server: 'Server'):
        self.server = server

    def data_received(self, data: bytes):
        print(data)

        decoded = data.decode()

        if self.login is not None:
            self.send_message(decoded)
        else:
            if decoded.startswith("Login:"):
                self.login = decoded.replace("Login:", "").replace("\r\n", "")

                if self.login not in self.server.login_list:  # Если такого логина нет в списке
                    self.server.login_list.append(self.login)  # то добавляем его в список
                    self.transport.write(
                        f"Привет, {self.login}!\n".encode()
                    )
                    self.send_history()
                else:
                    self.transport.write(f"логин {self.login} занят, попробуйте другой\n".encode())
                    self.login = None
                    self.transport.close()
            else:
                self.transport.write("Неправильный логин\n".encode())

    def connection_made(self, transport: transports.Transport):
        self.server.clients.append(self)
        self.transport = transport
        print("Пришел новый клиент")

    def connection_lost(self, exception):
        self.server.clients.remove(self)
        if self.login is not None:
            self.server.login_list.remove(self.login)
        print("Клиент вышел")

    def send_message(self, content: str):
        message = f"{self.login}:{content}\n"
        self.server.history.append(message)

        for user in self.server.clients:
            user.transport.write(message.encode())

    def send_history(self):
        # делаем срез последних 10 элементов списка, в котором хранится история сообщений
        current_history = self.server.history[-10::]
        for message in current_history:
            self.transport.write(message.encode())


class Server:
    clients: list
    history: list = []
    login_list: list = []

    def __init__(self):
        self.clients = []

    def build_protocol(self):
        return ServerProtocol(self)

    async def start(self):
        loop = asyncio._get_running_loop()

        coroutine = await loop.create_server(
            self.build_protocol,
            '127.0.0.1',
            8888
        )

        print("Сервер запущен ...")  # Automate the boring stuff with python

        await coroutine.serve_forever()


process = Server()

try:
    asyncio.run(process.start())
except KeyboardInterrupt:
    print("Сервер остановлен вручную")
