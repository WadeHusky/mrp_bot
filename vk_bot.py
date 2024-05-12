# -*- coding: utf-8 -*-
from requests import get
import vk_api
from random import randint
from config import vk_token, headers, vk_group_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
vk_session = vk_api.VkApi(token=vk_token)
vk_session._auth_token()
vk_api = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, vk_group_id)

commands = ["/mrp", "/mrp_online", "/pomoidor", "/mordor", "/мордор", "/мрп", "/мрп_онлайн", "/помойдор"]

def get_online():
	try:
		response = get("https://l.mordor-rp.com/launcher/monitoring/online.php", headers=headers).json()
		rponl = 0; obsonl = 0; funonl = 0
		text = "--====[ Mordor RP ]====--\n\n"
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
		if obsonl > 0: return(text)
		else: return("[Mordor RP] Мордор или сайт умер.")
	except: return("Ошибка.")


def send(pid, msg):
	rid = randint(1, 2147483647)
	vk_api.messages.send(peer_id=pid, message=msg, random_id=rid)


def main():
	while True:
		try:
			for event in longpoll.listen():
				if event.type == VkBotEventType.MESSAGE_NEW:
					peer_id = event.object.message["peer_id"]
					text = event.object.message["text"]
					if text.lower() in commands:
						send(peer_id, f"{get_online()}")
					elif text.lower() in ["/help", "/хелп", "/помощь"]:
						send(peer_id, "Команды:\nПолучение онлайна Mordor RP:\n- /mrp\n- /mrp_online\n- /pomoidor\n- /mordor\n- /мрп\n- /мрп_онлайн\n- /помойдор\n- /мордор")
		except Exception as e:
			with open("log_vk_bot.txt", "a") as file:
				file.write(e+"\n")


if __name__ == "__main__": main()
