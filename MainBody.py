import telebot
from telebot import apihelper
from TestBot import Commands, TextMessages, Quests

######################################################################################################################

token = "890068491:AAHce1A-j3UNAlqpKqGCFIfINKYTfnFqkv0"
socks5 = '96.96.1.165'
port = 1080
apihelper.proxy = {'https': 'socks5://' + socks5 + ':' + str(port) + '/'}
bot = telebot.TeleBot(token)

######################################################################################################################

# {'chat_id': 'nickname'}
users = {}
# {'chat_id': ['nickname', 'text']}
user_messages = {}
# {'chat_id': {'rights': 'num', 'text_style': 'num', 'current_quest': 'num', 'hint_num': 'num'}}
users_rights = {}

######################################################################################################################

with open(r'Data\users_rights', 'r') as file:
    data = file.readline()
data = data.split(' ')
for i in data:
    if i == '':
        continue
    i = i.split(':')
    users_rights.update(
        {int(i[0]): {'rights': int(i[1]), 'text_style': int(i[2]), 'current_quest': int(i[3]), 'hint_num': int(i[4])}})
print(users_rights)


######################################################################################################################

# @bot.message_handler(content_types=['sticker'])
# def show_message(message):
#     print(message)


@bot.message_handler(commands=['start'])
def start(message):
    Commands.start_message(message, users_rights, bot, users, user_messages)


@bot.message_handler(commands=['help'])
def help(message):
    Commands.help(message, users_rights, bot)


@bot.message_handler(content_types=['text'])
def send_text(message):
    TextMessages.chat(message, users_rights, bot)


######################################################################################################################
# Задания для практики
######################################################################################################################

@bot.callback_query_handler(func=lambda c: c.data == 'quest1')
def quest1(callBackQuery):
    Quests.dallasLockWin(users_rights, callBackQuery, bot)


@bot.callback_query_handler(func=lambda c: c.data == 'quest2')
def quest2(callBackQuery):
    Quests.sns(users_rights, callBackQuery, bot)


@bot.callback_query_handler(func=lambda c: c.data == 'quest3')
def quest3(callBackQuery):
    Quests.ViPNet(users_rights, callBackQuery, bot)


@bot.callback_query_handler(func=lambda c: c.data == 'quest4')
def quest4(callBackQuery):
    Quests.lsp(users_rights, callBackQuery, bot)


@bot.callback_query_handler(func=lambda c: c.data == 'quest5')
def quest5(callBackQuery):
    Quests.sobol(users_rights, callBackQuery, bot)

######################################################################################################################
#
######################################################################################################################

if __name__ == "__main__":
    bot.polling()
