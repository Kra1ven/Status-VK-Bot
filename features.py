import win32api
import time
import webbrowser
from PIL import ImageGrab
from win32gui import GetWindowText, GetForegroundWindow 
from simple_image_download import simple_image_download as simp

def getStatus():
	return (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000

def wake():
	webbrowser.open("https://www.youtube.com/watch?v=CNDI4WlJ8eo")

def makeScreenshot():
	snapshot = ImageGrab.grab()
	snapshot.save('random.jpg')

def getWindow():
	return GetWindowText(GetForegroundWindow())

def randomPic(text):
	response = simp
	response().download(text, 1)

