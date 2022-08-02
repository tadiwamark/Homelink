import time
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop

bulb = 26
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(bulb, GPIO.OUT)
GPIO.output(bulb, 0) 

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Received: %s' % command)

    if 'on' in command:
        message = "Turned on the light"
        GPIO.output(bulb, 1)
        telegram_bot.sendMessage (chat_id, message)
    
    if 'off' in command:
        message = "Turned off the light"
        GPIO.output(bulb, 0)
        telegram_bot.sendMessage (chat_id, message)
    

telegram_bot = telepot.Bot('5533298158:AAF7AIk7rhMUSklYfx7caRdMKbxPrwuH7dU')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print ('Send the command to turn on or off the light...')

while 1:
    time.sleep(10)