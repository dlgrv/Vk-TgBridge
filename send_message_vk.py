import vk_api
from vk_api.utils import get_random_id
import config

vk_session = vk_api.VkApi(token=config.vk_api_token)
session_api = vk_session.get_api()

def send_vk(user_message):
    vk_session.method('messages.send', {'peer_id': config.vk_chat_id, 'message': user_message, 'random_id': get_random_id()})