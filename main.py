import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import threading
import time
import client

# Authorization
vk_session = vk_api.VkApi(token='')
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def client_handle(event):
    request = event.text.lower()
    print(f"[MainHandle] New message {request}\n")
    client.handle(event.user_id, request)


def new_message():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            thread = threading.Thread(target=client_handle, args=(event,))
            thread.start()
            print(f"[MainHandle] {threading.active_count()} threads\n")

while True:
    try:
        new_message()
    except requests.exceptions.ReadTimeout:
        pass