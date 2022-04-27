import os
import telebot

bot = telebot,telebot('5162650131:AAFv8auf17X1_CnfCmEiWQXkm2Baz4b1Sj0')

@bot.meesage_handler(commsnds=['start'])
def send_welcom(message):
    bot.reply_to(message,'hello i am ometh')

@bot.meesage_handler(commsnds=['start'])
def send_welcom(message):
     bot.reply_to(message,'moko moko')

bot.polling()     
