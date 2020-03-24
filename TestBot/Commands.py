import os

from TestBot import KeyBoards


#######################################################################################################################

def start_message(message, user_rights, bot, users, user_messages):
    if message.chat.id not in user_rights:
        bot.send_message(message.chat.id, 'Хелоу Юный Цибовец\nВведи правильное слово чтобы начать...',
                         reply_markup=KeyBoards.help())
        users.update({message.chat.id: message.chat.first_name})
        user_messages.update({message.chat.id: [message.text]})
        user_rights.update({message.chat.id: {'rights': 0, 'text_style': 0, 'current_quest': 0, 'hint_num': 0}})
        updateRights(user_rights)
        saveDialog(message)
        print(user_rights)
    elif user_rights[message.chat.id]['rights'] == 2:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAO5XnLOeKWG9bL5XBzH3M8VYaoGsFwAAk8AA9ofmw8rNRfyuYUgexgE')
        print('Авторизуется забаненый')
    elif user_rights[message.chat.id]['rights'] == 1:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIDjl55q1Egrk-Vx01TZa3swZscp67vAAITAwACtXHaBjRI6dwM54DXGAQ',
                         reply_markup=KeyBoards.mainBoard())


def help(message, user_rights, bot):
    if user_rights[message.chat.id]["current_quest"] == 0:
        if user_rights[message.chat.id]['hint_num'] == 0:
            bot.send_message(message.chat.id, '<s>Хорошенько</s> подумай как называется отдел',
                             parse_mode='HTML')
            user_rights[message.chat.id]['hint_num'] += 1
            updateRights(user_rights)
        elif user_rights[message.chat.id]['hint_num'] == 1:
            bot.send_message(message.chat.id, 'Попробуй еще чуть чуть подумать')
            user_rights[message.chat.id]['hint_num'] += 1
            updateRights(user_rights)
        elif user_rights[message.chat.id]['hint_num'] == 2:
            bot.send_message(message.chat.id,
                             '<s>Взгляни вокруг, оглянись назад...</s>\nПосмотри на дверь, там написанно название',
                             parse_mode='HTML')
            user_rights[message.chat.id]['hint_num'] += 1
            updateRights(user_rights)
        elif user_rights[message.chat.id]['hint_num'] == 3:
            bot.send_message(message.chat.id, 'Напиши название отдела сокращенно (3 буквы)')
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBGV5y7QE3V9NpCyJJHjRMgLADcbuKAAIHAAPDokAIwTbssS05u54YBA')
            user_rights[message.chat.id]['hint_num'] += 1
        elif user_rights[message.chat.id]['hint_num'] == 4:
            bot.send_message(message.chat.id, 'Ну пропробуй подумать еще чуть чуть, начинается на О...')
            user_rights[message.chat.id]['hint_num'] += 1
        elif user_rights[message.chat.id]['hint_num'] == 5:
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAIDOV55pGLqs0uWGjC_GPGoij3yvCwRAAIEAQACCRI0AAHV58uOwFMObhgE')
            user_rights[message.chat.id]['hint_num'] += 1
        elif user_rights[message.chat.id]['hint_num'] == 6:
            bot.send_message(message.chat.id, 'Спроси уже у тех кто рядом, как отдел сокращенно называется')
    elif user_rights[message.chat.id]['current_quest'] == 1:
        if user_rights[message.chat.id]['hint_num'] == 0:
            bot.send_message(message.chat.id, 'Если не знаешь что делать, то выбери раздел с практикой')
            user_rights[message.chat.id]['hint_num'] += 1
            updateRights(user_rights)
        elif user_rights[message.chat.id]['hint_num'] == 1:
            bot.send_message(message.chat.id, '', reply_markup=KeyBoards.practiceBoard())
    elif user_rights[message.chat.id]['current_quest'] == 2:
        if user_rights[message.chat.id]['hint_num'] == 0:
            bot.send_message(message.chat.id, 'Если попросить, то текст откроется')
            user_rights[message.chat.id]['hint_num'] += 1
        elif user_rights[message.chat.id]['hint_num'] == 1:
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAIDml55tx5fuE6uByG8Z3tqtKBo0XrEAAIYAgACN4QwAAHuqUPmkRggBhgE',
                             reply_markup=KeyBoards.help())
            user_rights[message.chat.id]['hint_num'] += 1
        elif user_rights[message.chat.id]['hint_num'] == 2:
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAIDm155tyBnY2V7eHWk22rdVmnfJwMkAAIaAgACN4QwAAGAqiDeD0I-LRgE',
                             reply_markup=KeyBoards.help())
            user_rights[message.chat.id]['hint_num'] += 1
        elif user_rights[message.chat.id]['hint_num'] == 3:
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAIDnF55tyKssN6NVpjp2ybn38ANTAiWAAIcAgACN4QwAAFWVhzgnFfVORgE',
                             reply_markup=KeyBoards.help())
            user_rights[message.chat.id]['hint_num'] += 1
        elif user_rights[message.chat.id]['hint_num'] == 4:
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAIDnV55tyTYTXHxx3PIh3pDDDFC2w0jAAIeAgACN4QwAAEgYmSoSzaeNRgE',
                             reply_markup=KeyBoards.help())
            user_rights[message.chat.id]['hint_num'] += 1
        elif user_rights[message.chat.id]['hint_num'] == 5:
            bot.send_message(message.chat.id, 'напиши "открой текст"', )
    elif user_rights[message.chat.id]['current_quest'] == 10:
        if user_rights[message.chat.id]['hint_num'] == 0:
            bot.send_message(message.chat.id,
                             'Почитай гайды администратора по установке\n' +
                             'Не советую пробовать на авось, можно и систему убить')


#######################################################################################################################
# Help functions
#######################################################################################################################

def updateRights(users_rights):
    with open(os.path.normpath('Data\\users_rights'), 'w') as file:
        for i in users_rights:
            file.write(
                str(i) + ':' + str(users_rights[i]['rights']) + ':' + str(users_rights[i]['text_style']) + ':' + str(
                    users_rights[i]['current_quest']) + ':' + str(users_rights[i]['hint_num']) + ' ')


def saveDialog(message):
    try:
        with open('Dialogs\\' + str(message.chat.id), 'a') as file:
            file.write(message.text + '\n')
    except FileNotFoundError:
        with open('Dialogs\\' + str(message.chat.id), 'w') as file:
            file.write(message.text + '\n')
