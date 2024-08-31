# -*- coding: utf-8 -*-
import vk_api
from requests import get
from os import getenv
from random import randint
from config import headers
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from dotenv import load_dotenv
from pathlib import Path
dotenv_path = f"{Path(__file__).parent.resolve()}/.env"
load_dotenv(dotenv_path=dotenv_path)
vk_session = vk_api.VkApi(token=getenv("vk_token"))
vk_session._auth_token()
vk_api = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, getenv("vk_group_id"))

commands = ["/mrp", "/mrp_online", "/pomoidor", "/mordor", "/мордор", "/мрп", "/мрп_онлайн", "/помойдор"]

def get_online():
	try:
		response = get("https://l.mordor-rp.com/launcher/monitoring/online.php", headers=headers).json()
		rponl = 0; obsonl = 0; funonl = 0; text = ""
		for element in response:
			text += f'[{element["name"]}]:  {element["min"]}\n'
			obsonl += int(element["min"])
			if element["tag"] == "roleplay": rponl += int(element["min"])
			if element["tag"] == "fun": funonl += int(element["min"])
		text += f"========================\n" \
            f"ROLEPLAY ONLINE: {rponl}\n" \
            f"FUN ONLINE: {funonl}\n" \
            f"========================\n" \
            f"FULL ONLINE: {obsonl}"
		return(text)
	except: 
		return("Ошибка.")


def send(pid, msg):
	rid = randint(1, 2147483647)
	vk_api.messages.send(peer_id=pid, message=msg, random_id=rid)


if __name__ == "__main__":
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
		except Exception:
			pass
