import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import config
import send_message_tg
import text_editor

vk_session = vk_api.VkApi(token=config.vk_api_token)
session_api = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, config.group_id)

while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.from_chat:
                    msg_event = event.message
                    user_message = msg_event.text
                    print('peer_id', msg_event.peer_id)
                    print(event.message)
                    user = session_api.users.get(user_ids=msg_event['from_id'])[0]
                    first_name, last_name = user['first_name'], user['last_name']
                    if msg_event['attachments'] != []:
                        url = 'https://rt.pornhub.com/'
                        if msg_event['attachments'][0]['type'] == 'photo':
                            max_size = 0
                            for size in msg_event['attachments'][0]['photo']['sizes']:
                                if size['height'] > max_size:
                                    max_size = size['height']
                                    url = size['url']
                            send_message_tg.send_tg((text_editor.from_vk_to_tg_with_photo(first_name,
                                                                                         last_name,
                                                                                         user_message,
                                                                                         url)))
                    else:
                        send_message_tg.send_tg(text_editor.from_vk_to_tg(first_name,
                                                                          last_name,
                                                                          user_message))
    except Exception as er:
        print(er)