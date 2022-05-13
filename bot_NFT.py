
import random
import os
import telebot
import sqlite3
from telebot import types
#import luck
#import scroll_ape


hideBoard = types.ReplyKeyboardRemove()

token = '5136783035:AAFxDeRpBQhLBsKBHfg0DoYhgQIKeTarQzo'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])

def get_collect(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("TONED APE CLUB!")
    markup.add(btn1)
    send1 = bot.send_message(message.from_user.id, "Выберите коллекцию для отслеживания:", reply_markup=markup)
    bot.register_next_step_handler(send1,get_coll_APE)

def get_coll_APE(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("История изменений")
    btn2 = types.KeyboardButton("Свойства и ранг")
    btn3 = types.KeyboardButton("К выбору коллекции")

    markup.add(btn1,btn2,btn3)


    send1 = bot.send_message(message.from_user.id, "Выберите интересуемую функцию:", reply_markup=markup)
    bot.register_next_step_handler(send1,functions)


def functions(message):


    if message.text == "История изменений" :
        send3 = bot.send_message(message.from_user.id, "Напишите номер интересующей вас обезьянки.",reply_markup=hideBoard)
        bot.register_next_step_handler(send3, changes)
    elif message.text == "Свойства и ранг":
        send3 = bot.send_message(message.from_user.id, "Напишите номер интересующей вас обезьянки.",reply_markup=hideBoard)
        bot.register_next_step_handler(send3, options_rank)
    elif message.text == "К выбору коллекции":
        get_collect(message)


def changes(message):
    connector = sqlite3.connect('nft_toned_ape.db')
    cursor = connector.cursor()
    cursor.execute(f"SELECT count(*) FROM list_NFT_APE where number_in_collection = {message.text} ORDER BY date")
    b=cursor.fetchone()
    cursor.execute(f"SELECT Name_Nft,price,owner,date,photo_adress FROM list_NFT_APE where number_in_collection = {message.text} ORDER BY date")
    a=cursor.fetchall()
    text = f'[Toned Ape Club # {message.text}]({a[0][4]})'
    bot.send_message(message.from_user.id, text, parse_mode="Markdown")

    for i in range(int(b[0])):
      bot.send_message(message.from_user.id, f""" {a[i][0]}
Цена :  {a[i][1]}
Владелец : {a[i][2]}
Время изменения : {a[i][3]}
""")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("История изменений")
    btn2 = types.KeyboardButton("Свойства и ранг")
    btn3 = types.KeyboardButton("К выбору коллекции")
    markup.add(btn1, btn2, btn3)

    send1 = bot.send_message(message.from_user.id, "Выберите интерecующую функцию:", reply_markup=markup)
    bot.register_next_step_handler(send1, functions)




def options_rank(message):

    connector = sqlite3.connect('nft_toned_ape.db')
    cursor = connector.cursor()
    cursor.execute(f"SELECT photo_adress FROM list_NFT_APE where number_in_collection = {message.text}")
    b = cursor.fetchone()
    text = f'[Toned Ape Club # {message.text}]({b[0]})'


    bot.send_message(message.from_user.id, text , parse_mode="Markdown")

    connector = sqlite3.connect('nft_toned_ape.db')
    cursor = connector.cursor()
    cursor.execute(f"SELECT * FROM options_ape where Name_Nft = {message.text}")
    a=cursor.fetchone()
    bot.send_message(message.from_user.id, f"""Рейтинг : {a[1]}
    Background :  {a[2]}
    Body : {a[3]}
    eyes : {a[4]}
    dress : {a[5]}
    hand : {a[6]}
    nails : {a[7]}
    rings : {a[8]}
    diamonds : {a[9]}
    hat : {a[10]}
    ear_right : {a[11]}
    ear_left : {a[12]}
    mouth : {a[13]}
    """)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("История изменений")
    btn2 = types.KeyboardButton("Свойства и ранг")
    btn3 = types.KeyboardButton("К выбору коллекции")
    markup.add(btn1,btn2,btn3)

    send1 = bot.send_message(message.from_user.id, "Выберите интерecующую функцию:", reply_markup=markup)
    bot.register_next_step_handler(send1, functions)

@bot.message_handler(commands=["base"])
def base_open(message):
        connector = sqlite3.connect('nft_toned_ape.db')
        cursor = connector.cursor()
        cursor.execute("SELECT count(*) FROM list_NFT_APE")
        a = cursor.fetchone()
        print(bot.send_message(message.from_user.id, a))


if 1:
    bot.infinity_polling()
