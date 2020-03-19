from time import sleep

import telebot
from telebot import apihelper
from telegram import ParseMode

token = "890068491:AAHce1A-j3UNAlqpKqGCFIfINKYTfnFqkv0"

apihelper.proxy = {'https': 'socks5://96.96.1.165:1080/'}
bot = telebot.TeleBot(token)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('CIB')
keyboard1.row('MIB', 'Я просто посмотреть', 'Практика')
keyboard1.row('Дартс')
keyboard1.add('')

keyboardLine = [[telebot.types.InlineKeyboardButton('Задание 1', callback_data='quest1'),
                 telebot.types.InlineKeyboardButton('Задание 2', callback_data='quest2')],
                [telebot.types.InlineKeyboardButton('Задание 3', callback_data='quest3')]]
inlinekeyBoard1 = telebot.types.InlineKeyboardMarkup(keyboardLine)

keyboardLineDallasHelp = [telebot.types.InlineKeyboardButton('ПОМОГИТЕ КАК НИБУЛЬ', 'dallashelpwin')]
inlinekeyBoardDallasHelp = telebot.types.InlineKeyboardMarkup(keyboardLine)

keyWord = '#осистаил'

users = {'chat_id': 'nickname'}
user_messages = {'chat_id': ['nickname', 'text']}
users_rights = {}
with open('Data\\user_rights', 'r') as file:
    data = file.readline()
data = data.split(' ')
for i in data[0:-1]:
    i = i.split(':')
    users_rights.update({int(i[0]): int(i[1])})

def saveRights():
    with open('Data\\user_rights', 'w') as file:
        for i in users_rights:
            file.write(str(i) + ':' + str(users_rights[i]) + ' ')

@bot.message_handler(commands=['start'])
def start_message(message):
    if message.chat.id not in users_rights:
        bot.send_message(message.chat.id, 'Хелоу Юный Цибовец\nВведи правильное слово чтобы начать...')
        users.update({message.chat.id: message.chat.first_name})
        user_messages.update({message.chat.id: []})
        user_messages[message.chat.id].append(message.text)
        users_rights.update({message.chat.id: 0})
        saveRights()
        saveDialog(message)
        print(users_rights)
    elif users_rights[message.chat.id] == 2:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAO5XnLOeKWG9bL5XBzH3M8VYaoGsFwAAk8AA9ofmw8rNRfyuYUgexgE')
    elif users_rights[message.chat.id] == 1:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAOwXnLLjKy_heXw7eagdJdu7ChRKp0AArUAA90AAS8IoN24ZHH1a30YBA',
                         reply_markup=keyboard1)


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, 'CAACAgIAAxkBAAIBGV5y7QE3V9NpCyJJHjRMgLADcbuKAAIHAAPDokAIwTbssS05u54YBA',
                     reply_markup=inlinekeyBoardDallasHelp)


@bot.message_handler(content_types=['text'])
def send_text(message):
    try:
        try:
            print('tyt')
            with open('Dialogs\\' + str(message.chat.id), 'r') as file:
                user_messages[message.chat.id] = file.readlines()
            print('i tyt')
        except FileNotFoundError:
            with open('Dialogs\\' + str(message.chat.id), 'w') as file:
                file.write(message.text + '\n')
        user_messages[message.chat.id].append(message.text)
        if message.text == keyWord:
            users_rights.update({message.chat.id: 1})
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAOwXnLLjKy_heXw7eagdJdu7ChRKp0AArUAA90AAS8IoN24ZHH1a30YBA',
                             reply_markup=keyboard1)
            saveRights()
        if users_rights[message.chat.id] == 1:

            if message.text.lower() == 'привет':
                bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAOLXnHcX-sAAZ5ygy6uluamMreFOMkwAALGAQACioxxA1LyZu-JUIKRGAQ')
            elif message.text.lower() == 'пока':
                bot.send_message(message.chat.id, 'Пока')
            elif message.text.lower() == 'cib':
                bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
            elif message.text.lower() == 'mib':
                bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAOCXnHFGCRHz-jb5M5GOoflsOEgi-8AAuICAAK6wJUFgOcY7jS__3IYBA')
            elif message.text.lower() == "я просто посмотреть":
                bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=UFFic-USmrU')
            elif message.text.lower() == 'практика':
                bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAOXXnHdaSTf1iPmzfVmxAJ1LOn8yw0AAu8BAALdAAEvCIU6sYcxKu2OGAQ',
                                 reply_markup=inlinekeyBoard1)
                bot.register_next_step_handler(message, bestDallasEver)
        elif users_rights[message.chat.id] == 2:
            bot.send_message(message.chat.id, 'Вы были отключены на {%s} минут')
        else:
            print(user_messages[message.chat.id])
            if user_messages[message.chat.id].__len__() < 3:
                bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAO3XnLN0e84Nyt-eHjxcsuvcwxCOkcAAgoAA9ofmw_4Fqq260kSiRgE')
            elif user_messages[message.chat.id].__len__() < 5:
                bot.send_sticker(message.chat.id,
                                 'CAACAgQAAxkBAAO2XnLNjAlNCDDvmr4ZBZknMWrl9IkAAkMAAy_f-Al2WPTzFar4fhgE')
            elif user_messages[message.chat.id].__len__() < 7:
                bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAO4XnLOavIXY5230oDlLZ56cUdRGo4AAkIAA9ofmw_V_6ehBc6LYRgE')
            else:
                bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAO5XnLOeKWG9bL5XBzH3M8VYaoGsFwAAk8AA9ofmw8rNRfyuYUgexgE')
                users_rights.update({message.chat.id: 2})
                saveRights()

        print(message.text)
        saveDialog(message)
    except Exception as e:
        print(e)
        print(users_rights)


def bestDallasEver(message):
    bot.send_message(message.chat.id,
                     'Задача: Установить СЗИ Dallas lock 8.0-К на одну из машин по адресу\nhttps://192.168.10.50:8006\nOSITest:AAAbbb123')


@bot.message_handler(content_types=['sticker'])
def show_message(message):
    print(message)


@bot.message_handler()
def saveDialog(message):
    try:
        with open('Dialogs\\' + str(message.chat.id), 'a') as file:
            file.write(message.text + '\n')
    except FileNotFoundError:
        with open('Dialogs\\' + str(message.chat.id), 'w') as file:
            file.write(message.text + '\n')


bot.polling()
