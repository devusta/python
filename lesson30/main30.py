# -*- coding: utf-8 -*-
"""
33-video
30-dars. KIRILL-LOTIN TRANSLITERATOR BOT
Created on Fri Feb 23 15:54:01 2024

@author: Asadbek (devusta)
"""

from transliterate import to_cyrillic, to_latin

import telebot

TOKEN = '7122496448:AAE-aA91H8A71_6HqCfebPE_cR8M2P98eMY'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    answer = "Assalomu alaykum, Xush kelibsiz!"
    answer += "\nBiror matn kiriting!"
    bot.reply_to(message, answer)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg =  message.text
    answer = to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, answer)   
    

bot.infinity_polling()








































