# mrp_bot
Бот парсер онлайна проекта Mordor Role Play.
VK, TG
## Установка зависимостей:
```bash
pip install -r requirements.txt
```
## Что требуется для запуска ботов?
Создать файл .env:
```bash
touch .env
```
Заполнить следующие переменные любым текстовым редактором:
* tg_token = "API токен телеграм бота"
* vk_token = "API токен вк бота"
* vk_group_id = 123 

ПРИМЕЧАНИЕ: вместо 123 впишите айди группы (тип - int)

---
Запустить ботов командами:
```bash
nohup python3 vk_bot.py &
nohup python3 tg_bot.py &
```
## Основная команда ботов
* /mrp_online - получение онлайна
