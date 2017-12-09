#!/usr/bin/python
import smbus
import time
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value):
    bus.write_byte(address, int(value))
    return -1

def readNumber():
    number = bus.read_byte(address)
    return number

while True:
    #var = input("Enter 1 - 9: ")
    foo = "99"
    #if not var:
    #    continue
    writeNumber(foo)
    #writeNumber(var)
    #print("Nothing sent - RPI - Hi Arduino, I sent you ", var)
    #print("RPI - Hi Arduino, I sent you also", foo)
    #sleep one second
    time.sleep(1)
    number = readNumber()
    if number == 1:
        print("Dialed 1 Received")
        number == 0;
        foo = "11"
        writeNumber(foo)
    if number == 2:
        print("Dialed 2 Received")
        number == 0;
        foo = "22"
        writeNumber(foo)
    if number == 3:
        print("Dialed 3 Received")
        number == 0;
        foo = "33"
        writeNumber(foo)
    if number == 4:
        print("Dialed 4 Received")
        number == 0;
        foo = "44"
        writeNumber(foo)
    if number == 5:
        print("Dialed 5 Received")
        number == 0;
        foo = "55"
        writeNumber(foo)
    print(number)
