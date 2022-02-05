import random, vk_api, vk, time, random
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
vk_session = vk_api.VkApi(token='f19b1fa0b2a0820c2a41098c2846d6f2a5ac6dc415917d92951f353badeac556550b74f209e53c7b8f567')
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
longpoll = VkBotLongPoll(vk_session, 210517440)
vk = vk_session.get_api()
from vk_api.longpoll import VkLongPoll, VkEventType
Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()

keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Привет', color=VkKeyboardColor.NEGATIVE)
keyboard.add_button('Клавиатура', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_location_button()
keyboard.add_line()
keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=210517440")

Prime = ['вы все гандоны', 'секс за танк', 'чуваки, вы слиты', 'мой гендер PANZERKAMPFVAGEN IV', 'сосать блять!!!', 'я бешенный пидорас бегите', 'огузок соси хуй', 'вы тоже мечтали выебать Айнуру из кухни', 'хозяин бота пидор', 'ебать все в рот', 'простите за ругательство хуесосы', 'го гулять все', 'пиздец', 'лол', 'анальный дебошир', 'заебали сука', 'я чурка', 'залейте жижки', 'ругаюсь по кд']
d = 0

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if 'бред' in str(event):
            if event.from_chat:
                while True:
                    d = random.randint(0, 18)
                    time.sleep(3600)
                    vk.messages.send(
                        key = ('bacb2905825498030380bbf683256a610e074aa8'),          #ВСТАВИТЬ ПАРАМЕТРЫ
                        server = ('https://lp.vk.com/wh210517440'),
                        ts=('46'),
                        random_id = get_random_id(),
                        message=Prime[d],
                        chat_id = event.chat_id
                        )
