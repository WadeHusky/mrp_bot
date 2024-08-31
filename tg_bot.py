# -*- coding: utf-8 -*-
import telebot
from os import getenv
from requests import get
from dotenv import load_dotenv
from pathlib import Path
dotenv_path = f"{Path(__file__).parent.resolve()}/.env"
load_dotenv(dotenv_path=dotenv_path)
bot = telebot.TeleBot(getenv("tg_token"))

@bot.message_handler(commands=["mrp_online"])
def get_online(message):
	try:
		response = get("https://l.mordor-rp.com/launcher/monitoring/online.php").json()
		rponl = 0; obsonl = 0; funonl = 0; text = ""
		for element in response:
			text += f'[{element["name"]}]:  {element["min"]}\n'
			obsonl += int(element["min"])
			if element["tag"] == "roleplay": rponl += int(element["min"])
			if element["tag"] == "fun": funonl += int(element["min"])
		text +=	f"========================\n" \
				f"ROLEPLAY ONLINE: {rponl}\n" \
				f"FUN ONLINE: {funonl}\n" \
				f"========================\n" \
				f"FULL ONLINE: {obsonl}"
		bot.reply_to(message, text)
	except Exception:
		bot.reply_to(message, "Ошибка.")

@bot.message_handler(commands=['start', 'help'])
def process_start_command(message):
    bot.reply_to(
		message, 
		f"Команды:\n"\
		f"- /my_id - получение уникального идентификатора пользователя.\n"\
		f"- /mrp_online - получение онлайна на проекте Mordor Role Play"
	)

@bot.message_handler(commands=["my_id"])
def user_id(message):
    uid = message.from_user.id
    bot.reply_to(
		message, 
		f"<a href='tg://user?id={uid}'>Пользователь</a>, "\
		f"твой уникальный идентификатор (ID):\n\n"\
		f"<code>{uid}</code>",
		parse_mode="HTML"
	)

if __name__ == '__main__':
	while True:
		try: bot.polling()
		except KeyboardInterrupt: exit()
		except: pass
