# Определение удаленного подключения по открытым портам. Вписать TOKEN и chat_id
import psutil
import telebot
import time
import requests

# Впишите токен вашего бота (в правильном формате)
TOKEN = 'Ваш_токен'

# Список портов, которые будем прослушивать
PORTS = [20, 21, 22, 23, 5900, 5901]

bot = telebot.TeleBot(TOKEN)

# Получаем имя пользователя
username = ''
users = psutil.users()
if users: # Проверяем, что список users не пустой
    username = users[0].name

def check_connections():
    """Проверяем текущие соединения"""
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == 'ESTABLISHED' and conn.laddr.port in PORTS:
            # Отправляем сообщение в Telegram
            external_ip = requests.get('https://api.ipify.org').text
            message = f"Внимание! \nПроизошло удаленное подключение!\nПользователь: {username}\nIP адрес: {external_ip}\nПорт: {conn.laddr.port}"
            bot.send_message(chat_id='Ваш_чат_id', text=message)

while True:
    check_connections()
    time.sleep(60) # Время запуска в секундах



