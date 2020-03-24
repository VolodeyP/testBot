from TestBot import KeyBoards, Commands


def dallasLockWin(user_rights, callback, bot):
    if (user_rights[callback.message.chat.id]['text_style'] == 1):
        bot.answer_callback_query(callback.id,
                                  text='Задача: Установить СЗИ Dallas lock 8.0-К на одну из машин по адресу\n' +
                                       'https://192.168.10.50:8006\nOSITest:AAAbbb123',
                                  show_alert=True)
        if user_rights[callback.message.chat.id]['current_quest'] != 10:
            user_rights[callback.message.chat.id].update({'current_quest': 10, 'hint_num': 0})
            Commands.updateRights(user_rights)
    else:
        bot.answer_callback_query(callback.id,
                                  text='Umsebenzi: Faka ilokhi yeEbmmbt fohv-8.0-L TAJ komunye wemishini e-\n' +
                                       'https://192.168.10.50:8006\nOSITest:AAAbbb123',
                                  show_alert=True)
        # if user_rights[callback.message.chat.id]['current_quest'] != 10:
        #     user_rights[callback.message.chat.id].update({'current_quest': 10, 'hint_num': 0})
        #     Commands.updateRights(user_rights)


def sns(user_rights, callback, bot):
    if (user_rights[callback.message.chat.id]['text_style'] == 1):
        bot.answer_callback_query(callback.id,
                                  text='Задача: Установить СЗИ SNS на одну из машин по адресу\n' +
                                       'https://192.168.10.50:8006\nOSITest:AAAbbb123', show_alert=True)
        if user_rights[callback.message.chat.id]['current_quest'] != 11:
            user_rights[callback.message.chat.id].update({'current_quest': 11, 'hint_num': 0})
            Commands.updateRights(user_rights)
    else:
        bot.answer_callback_query(callback.id,
                                  text='ภารกิจ: ติดตั้ง TAJ TOT บนหนึ่งในเครื่องที่\n' +
                                       'https://192.168.10.50:8006\nOSITest:AAAbbb123', show_alert=True)
        # if user_rights[callback.message.chat.id]['current_quest'] != 11:
        #     user_rights[callback.message.chat.id].update({'current_quest': 11, 'hint_num': 0})
        #     Commands.updateRights(user_rights)


def ViPNet(user_rights, callback, bot):
    if (user_rights[callback.message.chat.id]['text_style'] == 1):
        bot.answer_callback_query(callback.id,
                                  text='Задача: Установить СКЗИ ViPNet на одну из машин по адресу\n' +
                                       'https://192.168.10.50:8006\nOSITest:AAAbbb123', show_alert=True)
        if user_rights[callback.message.chat.id]['current_quest'] != 12:
            user_rights[callback.message.chat.id].update({'current_quest': 12, 'hint_num': 0})
            Commands.updateRights(user_rights)
    else:
        bot.answer_callback_query(callback.id,
                                  text='କାର୍ଯ୍ୟ: WjQOfu କ୍ରିପ୍ଟୋଗ୍ରାଫିକ୍ ସୂଚନା ସୁରକ୍ଷା ସିଷ୍ଟମକୁ ଗୋଟିଏ ଯନ୍ତ୍ରରେ ସ୍ଥାପନ କରନ୍ତୁ |\n' +
                                       'https://192.168.10.50:8006\nOSITest:AAAbbb123', show_alert=True)
        # if user_rights[callback.message.chat.id]['current_quest'] != 12:
        #     user_rights[callback.message.chat.id].update({'current_quest': 12, 'hint_num': 0})
        #     Commands.updateRights(user_rights)


def lsp(user_rights, callback, bot):
    if (user_rights[callback.message.chat.id]['text_style'] == 1):
        bot.answer_callback_query(callback.id,
                                  text='Задача: Установить СЗИ SN LSP на одну из машин по адресу\n' +
                                       'https://192.168.10.50:8006\nOSITest:AAAbbb123', show_alert=True)
        if user_rights[callback.message.chat.id]['current_quest'] != 13:
            user_rights[callback.message.chat.id].update({'current_quest': 13, 'hint_num': 0})
            Commands.updateRights(user_rights)
    else:
        bot.answer_callback_query(callback.id,
                                  text='ټاسک: په یو ماشین کې TAJ TO MTQ نصب کړئ\n' +
                                       'https://192.168.10.50:8006\nOSITest:AAAbbb123', show_alert=True)
        # if user_rights[callback.message.chat.id]['current_quest'] != 13:
        #     user_rights[callback.message.chat.id].update({'current_quest': 13, 'hint_num': 0})
        #     Commands.updateRights(user_rights)


def sobol(user_rights, callback, bot):
    if (user_rights[callback.message.chat.id]['text_style'] == 1):
        bot.answer_callback_query(callback.id,
                                  text='Задача: Установить СДЗ Соболь на что нибудь, куда подойдет\n'
                                  , show_alert=True)
        if user_rights[callback.message.chat.id]['current_quest'] != 14:
            user_rights[callback.message.chat.id].update({'current_quest': 14, 'hint_num': 0})
            Commands.updateRights(user_rights)
    else:
        bot.answer_callback_query(callback.id,
                                  text='Iṣẹ-ṣiṣe: Fi TEA Tbcmf sori ohun kan, nibiti o ti jẹ deede\n'
                                  , show_alert=True)
        # if user_rights[callback.message.chat.id]['current_quest'] != 14:
        #     user_rights[callback.message.chat.id].update({'current_quest': 14, 'hint_num': 0})
        #     Commands.updateRights(user_rights)
