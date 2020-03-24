import telebot.types


def OpenQuestKeyboard() -> telebot.types.InlineKeyboardMarkup:
    keyboardLineOpen = [telebot.types.InlineKeyboardButton('Dallas The Best', callback_data='quest1'),
                        telebot.types.InlineKeyboardButton('SNS или Смэрть', callback_data='quest2'),
                        telebot.types.InlineKeyboardButton('Попытка не пытка,\nили как поставить ViPNet',
                                                           callback_data='quest3'),
                        telebot.types.InlineKeyboardButton('Ты сам это выбрал', callback_data='quest4'),
                        telebot.types.InlineKeyboardButton('Главное не сожги мать', callback_data='quest5')
                        ]

    inlinekeyBoardOpen = telebot.types.InlineKeyboardMarkup()
    for i in range(len(keyboardLineOpen)):
        inlinekeyBoardOpen.add(keyboardLineOpen[i])
    return inlinekeyBoardOpen


def CloseQuestKeyboard() -> telebot.types.InlineKeyboardMarkup:
    keyboardLineClose = [telebot.types.InlineKeyboardButton('Umsebenzi wokuqala', callback_data='quest1'),
                         telebot.types.InlineKeyboardButton('ਟਾਸਕ ਨੰਬਰ ਦੋ', callback_data='quest2'),
                         telebot.types.InlineKeyboardButton('Opdrag nommer drie', callback_data='quest3'),
                         telebot.types.InlineKeyboardButton('ଚାକିରି ସଂଖ୍ୟା ଚାରି |', callback_data='quest4'),
                         telebot.types.InlineKeyboardButton('ภารกิจหมายเลขห้า', callback_data='quest5')]
    inlinekeyBoardClose = telebot.types.InlineKeyboardMarkup()
    for i in range(len(keyboardLineClose)):
        inlinekeyBoardClose.add(keyboardLineClose[i])
    return inlinekeyBoardClose


def dallasHelpBoard() -> telebot.types.InlineKeyboardMarkup:
    keyboardLineDallasHelp = [telebot.types.InlineKeyboardButton('ПОМОГИТЕ КАК НИБУЛЬ', 'q1help'),
                              telebot.types.InlineKeyboardButton('ПОМОГИТЕ КАК НИБУЛЬ', 'q1help'),
                              telebot.types.InlineKeyboardButton('ПОМОГИТЕ КАК НИБУЛЬ', 'q1help'),
                              telebot.types.InlineKeyboardButton('ПОМОГИТЕ КАК НИБУЛЬ', 'q1help'),
                              telebot.types.InlineKeyboardButton('ПОМОГИТЕ КАК НИБУЛЬ', 'q1help')]
    inlinekeyBoardDallasHelp = telebot.types.InlineKeyboardMarkup()
    for i in range(len(keyboardLineDallasHelp)):
        inlinekeyBoardDallasHelp.add(keyboardLineDallasHelp[i])
    return inlinekeyBoardDallasHelp


def mainBoard() -> telebot.types.ReplyKeyboardMarkup:
    keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard1.row('CIB', '/help')
    keyboard1.row('MIB', 'Я просто посмотреть', 'Практика')
    keyboard1.row('Дартс')
    return keyboard1


def help() -> telebot.types.ReplyKeyboardMarkup:
    kb = telebot.types.ReplyKeyboardMarkup(True, True)
    kb.row('/help')
    return kb


def practiceBoard() -> telebot.types.ReplyKeyboardMarkup:
    kb = telebot.types.ReplyKeyboardMarkup(True, True)
    kb.row('Практика')
    return kb

def CIB() -> telebot.types.InlineKeyboardMarkup:
    kb = telebot.types.InlineKeyboardMarkup()
    bt = [telebot.types.InlineKeyboardButton('ОСИ','osi'), telebot.types.InlineKeyboardButton('ОЗИ','OZI'), telebot.types.InlineKeyboardButton('Менеджеры','Managers'), telebot.types.InlineKeyboardButton('',''),]