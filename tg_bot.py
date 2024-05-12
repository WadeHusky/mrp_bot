import telebot
from requests import get
from config import tg_token
bot = telebot.TeleBot(tg_token)

@bot.message_handler(commands=["mrp_online"])
def get_online(message):
	try:
		response = get("https://l.mordor-rp.com/launcher/monitoring/online.php").json()
		rponl = 0; obsonl = 0; funonl = 0
		text = ""
		for element in response:
			text = text + f'[{element["name"]}]:  {element["min"]}\n'
			obsonl = obsonl + int(element["min"])
			if element["tag"] == "roleplay": rponl = rponl + int(element["min"])
			if element["tag"] == "fun": funonl = funonl + int(element["min"])
		text = text + \
                     	f"========================\n" \
                     	f"ROLEPLAY ONLINE: {rponl}\n" \
                     	f"FUN ONLINE: {funonl}\n" \
                     	f"========================\n" \
                     	f"FULL ONLINE: {obsonl}"
		if obsonl > 0: bot.reply_to(message, text)
		else: bot.reply_to(message, "[Mordor RP] Мордор или сайт умер.")
	except Exception as e: bot.reply_to(message, "Ошибка.")

@bot.message_handler(commands=['start', 'help'])
def process_start_command(message):
    bot.reply_to(message, f"Команды:\n- /my_id - получение уникального идентификатора пользователя.\n- /mrp_online - получение онлайна на проекте Mordor Role Play") #{message}")

@bot.message_handler(commands=["my_id"])
def user_id(message):
    bot.reply_to(message, f"Your telegram ID: {message.from_user.id}")

if __name__ == '__main__':
	while True:
		try: bot.polling()
		except KeyboardInterrupt: exit()
		except: pass
