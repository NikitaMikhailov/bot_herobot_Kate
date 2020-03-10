#!/usr/bin/env bash
#!/bin/bash
#!/bin/sh
#!/bin/sh -

from vk_api.utils import get_random_id
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests, vk_api, random

f = open('token.txt','r')
token = f.read()
f.close()

session = requests.Session()
vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, '183679552')
vk = vk_session.get_api()
upload = VkUpload(vk_session)  # Для загрузки изображений


def mainfunc():

    try:
        for event in longpoll.listen():

            if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text:

                fio = requests.get("https://api.vk.com/method/users.get?user_ids=" + str(
                    event.obj.from_id) + "&fields=bdate&access_token="+token+"&v=5.92")
                first_name = fio.text[14::].split(',')[1].split(':')[1][1:-1:]
                last_name = fio.text[14::].split(',')[2].split(':')[1][1:-1:]
#195310233  51556033

                slovar_Katya=["Ну Пееееть","Ну Пееетяяя","Опять ты тут пиздишь, Пётр","Дома тебя ждёт серьезный разговор!"]
                if event.from_chat and random.randint(0,10)==0 and event.obj.from_id==51556033 and len(event.obj.text.split(" "))>5:
                    vk.messages.send(
                        chat_id=event.chat_id,
                        random_id=get_random_id(),
                        message=slovar_Katya[random.randint(0,1)]
                    )

                if event.from_chat and random.randint(0,2)==0 and event.obj.text.find('ТОП') == -1 and event.obj.text.find("Катя")!=-1 or event.obj.text.find("Катю")!=-1 or event.obj.text.find("Катей")!=-1 or event.obj.text.find("Катюха")!=-1:
                    vk.messages.send(
                        chat_id=event.chat_id,
                        random_id=get_random_id(),
                        message="Я тут!"
                    )
                if event.from_chat and event.obj.text=='!Kate ping' and event.obj.from_id==195310233:
                    vk.messages.send(
                        chat_id=event.chat_id,
                        random_id=get_random_id(),
                        message="I'm Ok"
                    )

    except Exception as err:
        mainfunc()
        vk.messages.send(
            user_id=195310233,
            random_id=get_random_id(),
            message='Возникла ошибка ' + str(err) + ' в главном цикле bot_herobot_Kate'
        )
mainfunc()
