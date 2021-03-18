import emoji
def from_vk_to_tg(first_name, last_name, user_message):
    return_text = f'{first_name} {last_name} \(Vk\)\n' \
                  f'\-{user_message}'
    return return_text

def from_tg_to_vk(first_name, last_name, user_message):
    return_text = f'{first_name} {last_name} (Tg)\n' \
                  f'-{user_message}'
    return return_text

def from_vk_to_tg_with_photo(first_name, last_name, user_message, url):
    if user_message == '':
        return_text = f'{first_name} {last_name} \(Vk\)\n' \
                      f'[Фоточка]({url})'
    else:
        return_text = f'{first_name} {last_name} \(Vk\)\n' \
                      f'\-{user_message} \n' \
                      f'[Фоточка]({url})'
    return return_text
