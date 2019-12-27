# !/usr/bin/env python

import telebot
from telebot.types import Message
from telebot import types
import config_level
import functionForBot as fBot
import copy
import keyActivators

TOKEN = '995249108:AAHv_znFEX_m9Z5Ggoo_M8AxhvxEoUuhsVE'
bot = telebot.TeleBot(TOKEN)
markup_inline_lvl = types.InlineKeyboardMarkup()
btn_light = types.InlineKeyboardButton('Начальный', callback_data='Light')
btn_medium = types.InlineKeyboardButton('Средний', callback_data='Medium')
btn_hard = types.InlineKeyboardButton('Продвинутый', callback_data='Hard')
markup_inline_lvl.add(btn_light, btn_medium, btn_hard)

markup_inline_next_light = types.InlineKeyboardMarkup()
markup_inline_next_medium = types.InlineKeyboardMarkup()
markup_inline_next_hard = types.InlineKeyboardMarkup()

btn_nextCard_light = types.InlineKeyboardButton('Следующая карточка', callback_data='Light')
btn_nextCard_medium = types.InlineKeyboardButton('Следующая карточка', callback_data='Medium')
btn_nextCard_hard = types.InlineKeyboardButton('Следующая карточка', callback_data='Hard')
btn_chooseCategory = types.InlineKeyboardButton('К выбору категории', callback_data='ChooseCategory')

markup_inline_next_light.add(btn_nextCard_light, btn_chooseCategory)
markup_inline_next_medium.add(btn_nextCard_medium, btn_chooseCategory)
markup_inline_next_hard.add(btn_nextCard_hard, btn_chooseCategory)

markup_inline_state = types.InlineKeyboardMarkup()
btn_hot = types.InlineKeyboardButton('Было горячо', callback_data='Hot')
btn_miss = types.InlineKeyboardButton('Пасс', callback_data='Miss')
markup_inline_state.add(btn_hot, btn_miss)

markup_donate = types.ReplyKeyboardMarkup()
btn_donate = types.InlineKeyboardButton('Donate🆘')
markup_donate.add(btn_donate)

activatorDict = {}
# Словарь для отслеживания кол-во фотографий использованных пользователем.
photosDict = {}


@bot.message_handler(commands=['start', 'help'])
def command_handler(message):
    global photosDict
    photosDict[message.chat.id] = [copy.deepcopy(config_level.listPhotosLight),
                                   config_level.listPhotosMedium, config_level.listPhotosHard]
    sumea = photosDict.get(message.chat.id)[1]
    print(sumea)

    bot.send_message(message.chat.id,
                     """
Hello, agents
Well, are you ready to play and get even closer to each other?

I have three levels of sinfulness for you 🔥
Let's check how brave you are and if you can reach the end?

Damn, the rules are simple - I am sending assignments - you are completing them.

‼️If you like the game and want to support its development. 
Donate button available. For more information, click on it ‼️
                     """, reply_markup=markup_donate)

    bot.send_message(message.chat.id, 'С какого уровня начнем?', reply_markup=markup_inline_lvl)


@bot.message_handler(func=lambda message: True)
def echo_gigits(message):
    if message.text == 'Donate🆘':
        bot.send_message(message.chat.id, 'Выберите категорию:',
                         reply_markup=markup_inline_lvl)
    # global activatorDict
    # activatorDict[message.chat.id] = 1
    # bot.send_message(message.chat.id, 'Регистрация успешно пройдена!')
    # bot.send_message(message.chat.id, 'С какого уровня начнем?', reply_markup=markup_inline_lvl)
    # if len(activatorDict) == 2:


#  f = open('logUsers.txt', 'w')
#  for index in activatorDict:
# 	 f.write(str(index) + ':' + str(activatorDict[index]) + '\n')
# f.close()

@bot.callback_query_handler(func=lambda call: True)
def call_back_love(call):
    listPhotos = photosDict.get(call.message.chat.id)
    if call.data == 'Light':
        if len(listPhotos[0]) != 0:
            strPhoto = fBot.getStringPhotos(listPhotos[0])
            photo = open('photos/light/{}'.format(strPhoto), 'rb')
            bot.send_photo(call.message.chat.id, photo, reply_markup=markup_inline_next_light)
        else:
            bot.send_message(call.message.chat.id, text='''
            
            Congratulations🎉🎊🎉
            
            You have passed all the tests in this category✅✅✅
            
            You can repeat these tests or go to the next level 😏⚡️🔥''',
                             reply_markup=markup_inline_next_light)
            print(len(listPhotos))
            print(listPhotos)
            print('from confib {}'.format(config_level.listPhotosLight))
        # photosDict.get(call.message.chat.id)[0].remove(stringPhoto)




    # elif call.data == 'Medium':
    #     indexLvL = random.randint(0, (len(config_level.listPhotosMedium) - 1))
    #     stringPhoto = config_level.listPhotosMedium[indexLvL]
    #     photo = open('photos/medium/{}'.format(stringPhoto), 'rb')
    #     bot.send_photo(call.message.chat.id, photo, reply_markup=markup_inline_next_medium)
    # elif call.data == 'Hard':
    #     indexLvL = random.randint(0, (len(config_level.listPhotosHard) - 1))
    #     stringPhoto = config_level.listPhotosHard[indexLvL]
    #     photo = open('photos/hard/{}'.format(stringPhoto), 'rb')
    #     bot.send_photo(call.message.chat.id, photo, reply_markup=markup_inline_next_hard)
    elif call.data == 'Hot' or call.data == 'Miss':
        bot.send_message(call.message.chat.id, text='Спасибо за отзыв, мы учтём его!',
                         reply_markup=markup_inline_next_light)
    elif call.data == 'ChooseCategory':
        bot.send_message(call.message.chat.id, text='Выберите категорию:',
                         reply_markup=markup_inline_lvl)
    elif call.data == 'Donate':
        bot.send_message(call.message.chat.id, text='Выберите категорию:',
                         reply_markup=markup_inline_lvl)

bot.polling(timeout=60)

print(str(photosDict.items()))
fBot.backUpData(photosDict)