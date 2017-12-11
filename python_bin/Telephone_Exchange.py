#!/usr/bin/python
import smbus, time, sys, pygame, datetime
from pygame import mixer

# Get ready for some i2c stuff
bus = smbus.SMBus(1)
# Arduino i2c address
address = 0x04

def writeNumber(value):
    bus.write_byte(address, int(value))
    return -1

def readNumber():
    number = bus.read_byte(address)
    return number

pygame.init()
pygame.mixer.init()
#tone  = pygame.mixer.Sound("../FUN_sounds/Kenney_Sounds/1.ogg")

while True:
    # Rotary Digit  - MIGHT NOT NEED - TRY REMOVING AT SOME POINT
    #r_digit = "99"
    #writeNumber(r_digit)
    time.sleep(1)
    number = readNumber()
    if number == 1:
        pygame.mixer.stop()
        print("Dialed 1 Received")
        number == 99;
        r_digit = "11"
        writeNumber(r_digit)
        tone = pygame.mixer.Sound("../FUN_sounds/Kenney_Sounds/1.ogg")
        tone.play()
        # time.sleep (20)
    if number == 55:
        print("off hook")
        number == 99;
        r_digit = "11"
        writeNumber(r_digit)
        tone = pygame.mixer.Sound("../FUN_sounds/dial_tone.ogg")
        tone.play()
        # time.sleep (20)
    if number == 2:
        print("Dialed 2 Received")
        number == 99;
        r_digit = "22"
        writeNumber(r_digit)
        tone = pygame.mixer.Sound("../FUN_sounds/Kenney_Sounds/2.ogg")
        tone.play()
    if number == 3:
        print("Dialed 3 Received")
        number == 99;
        r_digit = "33"
        writeNumber(r_digit)
        tone = pygame.mixer.Sound("../FUN_sounds/Kenney_Sounds/3.ogg")
        tone.play()
    if number == 4:
        print("Dialed 4 Received")
        number == 99;
        r_digit = "44"
        writeNumber(r_digit)
        # Dial Festival for Date
        mylist = []
        phone_time = datetime.datetime.now().strftime('%I Hours:%M Minutes: %p')
        mylist.append(phone_time)
        import subprocess
        at_tone = '"At the tone the time will be: "'
        #text = str(datetime.datetime.now().time())
        phone_time = str(mylist[0])
        filename = 'hello'
        file=open(filename,'w')
        file.write(at_tone)
        file.write(phone_time)
        file.close()
        subprocess.call('festival --tts '+filename, shell=True)

    if number == 5:
        print("Dialed 5 Received")
        number == 99;
        r_digit = "55"
        writeNumber(r_digit)
    #if number == 0:
    #    print("Dialed 0 Received")
    #    number == 99;
    #    r_digit = "55"
    #    writeNumber(r_digit)

    #print(number)
