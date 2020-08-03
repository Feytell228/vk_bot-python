#импорт либ
import requests
import datetime, time
import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


vk_session=vk_api.VkApi(token="30b1235ef7a47f25146523bb6fd174e8f63438e7169860e5caf7e0505083a320da07b84e6629392c355d3") 

text=["Кек","Лол","Ну ты и лох","bot by Xachapury","Бтс топ","порно асманской империи "," Чукча","водка плоха","Привет","Здорова", "хеллоу", "хелло","хай","зиг хаиль","как дела","че каво","пошол нахуй","как тебя зовут", "ты че пидр",]

running=True

longpoll=VkLongPoll(vk_session)
vk=vk_session.get_api()
#листание лонга
for event in longpoll.listen():
  
  if event.type==VkEventType.MESSAGE_NEW and event.to_me and event.text:
    if event.text=="!даун":
      if event.from_chat:
        vk.messages.send(
        chat_id=event.chat_id,
        random_id=random.randomint(64),
        message=random.choice(text))
    elif event.text=="!хелп",or event.text=="!помощь":
      elif event.from_chat:
        vk.messages.send(
          chat_id=event.chat_id,
          random_id=random.randomint(64),
          message="Команды: !даун"
          )
        