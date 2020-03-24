import os
import random
from time import sleep

from TestBot import Commands, KeyBoards

######################################################################################################################
# Переменные
######################################################################################################################

user_messages = {}
keyWord = ['osi', 'оси']
with open('Data\\relax', 'r') as file:
    youtubeVideo = file.readlines()

######################################################################################################################
# Загрузка переменных
######################################################################################################################

for i in os.listdir('Dialogs'):
    with open('Dialogs\\' + i, 'r') as file:
        user_messages.update({int(i): file.readlines()})


######################################################################################################################
#
######################################################################################################################

def chat(message, user_rights, bot):
    # try:
        try:
            user_messages[message.chat.id].append(message.text)
        except Exception:
            with open('Dialogs\\' + str(message.chat.id), 'w') as file:
                file.write(message.text + '\n')
            print('Ошибка работе с файлом ' + str(message.chat.id))
        if keyWord.__contains__(message.text.lower()) and user_rights[message.chat.id]['rights'] != 1:
            user_rights[message.chat.id].update({'rights': 1})
            if user_rights[message.chat.id]['hint_num'] == 6:
                bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAIDN155o9nkwoL4SfvLtJNErcyoeNkgAAJzAQACCRI0AAHBjBRMuV-ApBgE',
                                 reply_markup=KeyBoards.mainBoard())
            else:
                bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAOwXnLLjKy_heXw7eagdJdu7ChRKp0AArUAA90AAS8IoN24ZHH1a30YBA',
                                 reply_markup=KeyBoards.mainBoard())
            Commands.updateRights(user_rights)
            user_rights[message.chat.id]['hint_num'] = 0
            user_rights[message.chat.id]['current_quest'] = 1
            return
        if user_rights[message.chat.id]['rights'] == 1:
            if message.text.lower() == 'привет':
                bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAOLXnHcX-sAAZ5ygy6uluamMreFOMkwAALGAQACioxxA1LyZu-JUIKRGAQ')
            elif message.text.lower() == 'пока':
                bot.send_message(message.chat.id, 'Пока')
            elif message.text.lower() == 'cib':
                bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
                bot.send_message(message.chat.id, 'Общее устройство ЦИБ', reply_markup=KeyBoards.CIB())
            elif message.text.lower() == 'mib':
                msg = bot.send_sticker(message.chat.id,
                                       'CAACAgIAAxkBAAOCXnHFGCRHz-jb5M5GOoflsOEgi-8AAuICAAK6wJUFgOcY7jS__3IYBA')
                sleep(1)
                bot.delete_message(message.chat.id, message.message_id)
                bot.delete_message(msg.chat.id, msg.message_id)
            elif message.text.lower() == "я просто посмотреть":
                bot.send_message(message.chat.id, youtubeVideo[random.randint(0, len(youtubeVideo))],
                                 reply_markup=KeyBoards.mainBoard())
            elif message.text.lower() == 'практика':
                user_rights[message.chat.id].update({'hint_num': 0, 'current_quest': 2})
                if user_rights[message.chat.id]['text_style'] != 1:
                    bot.send_sticker(message.chat.id,
                                     'CAACAgIAAxkBAAIDjl55q1Egrk-Vx01TZa3swZscp67vAAITAwACtXHaBjRI6dwM54DXGAQ',
                                     reply_markup=KeyBoards.CloseQuestKeyboard())
                else:
                    bot.send_sticker(message.chat.id,
                                     'CAACAgIAAxkBAAIBnV50JqIzWOS6VoP1xixel6jhySzYAALrAgACusCVBfWVIenFy-uoGAQ',
                                     reply_markup=KeyBoards.OpenQuestKeyboard())
            elif message.text.lower() == 'дартс':
                bot.send_message(message.chat.id, 'Иди РАБотать')
            elif message.text.lower() == 'открой текст':
                user_rights[message.chat.id].update({'text_style': 1})
                bot.send_message(message.chat.id, 'Так бы сразу', reply_markup=KeyBoards.mainBoard())
                bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAIBnV50JqIzWOS6VoP1xixel6jhySzYAALrAgACusCVBfWVIenFy-uoGAQ',
                                 reply_markup=KeyBoards.OpenQuestKeyboard())
                Commands.updateRights(user_rights)
                user_rights[message.chat.id].update({'hint_num': 0})
            else:
                bot.send_message(message.chat.id, 'Не знаю таких команд\nпопробуй еще что нибудь',
                                 reply_markup=KeyBoards.mainBoard())
        elif user_rights[message.chat.id]['rights'] == 2:
            bot.send_message(message.chat.id, 'Вы были забанены, обратитесь к администратору')
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
                print('Забанил ' + str(message.chat.id))
                user_rights[message.chat.id].update({'rights': 2})
                Commands.updateRights(user_rights)

        print(str(message.chat.id) + ': ' + str(message.chat.first_name) + ': ' + message.text)
        Commands.saveDialog(message)
    # except Exception as e:
    #     print(e)
    #     print('SendTextError')

######################################################################################################################
