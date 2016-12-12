import vk
import time
import datetime

print('VKBot')
# Авторизуем сессию с помощью access token
session = vk.Session('6320d6c84cd67fe2f4814434057aba0a2db4464a73f21c9da31cf117b8f1242c40d3e1ad888eb33d6222c')

# или с помощью id приложения и данных авторизации пользователя
# session = vk.AuthSession(app_id='5772300', user_login='89381146850', user_password='klava1234xz')

# session = vk.AuthSession('api приложения','логин','пароль',scope='messages')

api = vk.API(session)

while (True):
    # Получим 20 последних входящих сообщений
    messages = api.messages.get()
    # Создадим список поддерживаемых комманд
    commands = ['Привет', 'Как дела?']

    # Найдем среди них непрочитанные сообщения с поддержанием командами
    # такими образом получим список в формате [ (id_пользователь, id_сообщения, команда),...]
    messages = [(m['uid'], m['mid'], m['body'])
                for m in messages[1:] if m['body'] in commands and m['read_state'] == 0]
    # Отвечаем на полученные команды
    for m in messages:
        user_id = m[0]
        message_id = m[1]
        comand = m[2]

        # Сформируем строку с датой и временим сервера
        date_time_string = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')

        if comand == 'Привет':
            api.messages.send(user_id=user_id,
                              message=date_time_string + '\n>VKBoot v0.1\n>Разработал: KL')

        if comand == 'Как дела?':
            api.messages.send(user_id=user_id,
                              message=date_time_string + '\n>VKBoot v0.1\n>Разработал: KL')
    # Сформируем список id всех сообщений с командами через запятую
    ids = ','.join([str(m[1]) for m in messages])

    # Помечаем полученные сообщения как прочитаные
    if ids:
        api.messages.markAsRead(message_ids=ids)

    # Проверяем сообщения каждые 3 секунды
    time.sleep(3)
