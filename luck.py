import telebot
import sqlite3
from telebot import types
import time


hideBoard = types.ReplyKeyboardRemove()
admin = 891705090
token = '5136783035:AAFxDeRpBQhLBsKBHfg0DoYhgQIKeTarQzo'
bot = telebot.TeleBot(token)

while 1 == 1:
    time.sleep(30)
    connector = sqlite3.connect('nft_toned_ape.db')
    cursor = connector.cursor()
    cursor.execute("SELECT number_in_collection,price FROM list_NFT_APE  GROUP BY number_in_collection having MAX(date) and price<>'not' and CAST(price AS INT)  < '301'")
    a = cursor.fetchall()
    cursor.execute("SELECT count(*) FROM (SELECT number_in_collection,price FROM list_NFT_APE  GROUP BY number_in_collection having MAX(date) and price<>'not' and CAST(price AS INT)  < '301')")
    b = cursor.fetchone()


    for i in range(int(b[0])):
        cursor.execute(f"SELECT count(*) FROM options_ape WHERE Name_Nft = {str(a[i][0])} and CAST(rating AS INT)  < '201'")
        d = cursor.fetchone()
        if int(d[0]) > 0:
             cursor.execute(f"SELECT Name_Nft FROM options_ape WHERE Name_Nft= {str(a[i][0])} and CAST(rating AS INT)  < '201'")
             e = cursor.fetchall()
             for i in range(int(d[0])):

                  bot.send_message(admin, f"{e[i]} Стоит меньше 301 тон и она в топ 200 рейтинга")
                  bot.send_message(397448482, f"{e[i]} Стоит меньше 301 тон и она в топ 200 рейтинга")
                  print("1")
