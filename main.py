import pyautogui as pg
import time

message = pg.prompt('What message you wanna send ?','Automate messaging','Type message here')
message_count =  pg.prompt('How many messages you wanna send ?', 'Automate messaging','')
for i in range(int(message_count)):
	pg.typewrite(message)
	pg.press('enter')
	print(message, i)