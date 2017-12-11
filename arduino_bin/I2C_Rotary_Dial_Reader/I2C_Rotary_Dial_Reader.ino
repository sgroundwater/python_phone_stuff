/*  ORIGINAL SOURCE CREDIT GOES TO: */
/*  Rotary Read Dial Code - See http://www.instructables.com/id/Interface-a-rotary-phone-dial-to-an-Arduino/ */
/*  Send I2C to Python Code - See  https://oscarliang.com/raspberry-pi-arduino-connected-i2c/ */
/*  Telephone Exchange System Code - See https://gluebox.com/telephone_stuff */

#include <Wire.h>
#define SLAVE_ADDRESS 0x04
int number = 0;
int state = 0;
int send_to_pi = 0;

// Rotary Dial Stuff
int needToPrint = 0;
int count;
int digit_payload;
int in = 2; //Arduino Pin to read
int lastState = LOW;
int trueState = LOW;
long lastStateChangeTime = 0;
int cleared = 0;
// Rotary Dial Constants
int dialHasFinishedRotatingAfterMs = 100;
int debounceDelay = 10;
//
const int offHookPin = 3;     // OFF THE HOOK BUTTON PIN
int offHookState = 0;
int offHook = 3;
bool executed = false;
bool hooked = false;

void setup(){
pinMode(13, OUTPUT);
Serial.begin(9600);
//pinMode(in, INPUT);
pinMode(offHookPin, INPUT);
// initialize i2c as slave
Wire.begin(SLAVE_ADDRESS);
// define callbacks for i2c communication
Wire.onReceive(receiveData);
Wire.onRequest(sendData);
// WELCOME
Serial.println("Insert Dime Here!");

}

void loop() {
// read OFF HOOK state of switch
offHookState = digitalRead(offHookPin);

int currentState = 1;
int hookedState =1;

if (offHookState == HIGH) {  // Off The Hook  
    // turn LED on:
    hooked = false;
    delay (1000);
    offHook = 6;
    
if (hookedState == 1 && hooked == false) {
        hooked = true;
        stopTone();
}    
    executed = false;
    delay (1000);
    offHook = 8;
  } 
  
if (offHookState == LOW) { // Off The Hook
if (currentState == 1 && executed == false) { // Play Tone Only OneTime
        executed = true;
        playTone();
} 
    
// Read Rotary Dial Stuff ...
int reading = digitalRead(in);
if ((millis() - lastStateChangeTime) > dialHasFinishedRotatingAfterMs) {
// the dial isn't being dialed, or has just finished being dialed.
if (needToPrint) {
// if it's only just finished being dialed, we need to send the number down the serial
// line and reset the count. We mod the count by 10 because '0' will send 10 pulses.
Serial.print(count % 10, DEC);
digit_payload = (count % 10);
executed = true;
hooked = true;
send_to_pi = 1;
needToPrint = 0;
count = 0;
cleared = 0;
offHook = 0;
} 
}

if (reading != lastState) {
lastStateChangeTime = millis();
}
if ((millis() - lastStateChangeTime) > debounceDelay) {
// debounce - this happens once it's stablized
if (reading != trueState) {
// this means that the switch has either just gone from closed->open or vice versa.
trueState = reading;
if (trueState == HIGH) {
// increment the count of pulses if it's gone high.
count++;
needToPrint = 1; // we'll need to print this number (once the dial has finished rotating)
}
}
}

lastState = reading;
}
}

// callback for received data
void receiveData(int byteCount){
while(Wire.available()) {
number = Wire.read();
Serial.print("data received: ");
Serial.println(number);
if (number == 1){
if (state == 0){
state = 1;
}
else{
state = 0;
}
}
}

}

// Callback for dialtone
void playTone() {
    Serial.println("\nPlay Dialtone Here\n");
    delay (100);
    offHook = 5;
}

void stopTone() {
    Serial.println("\nStop Dialtone Now\n");
    delay (100);
    offHook = 6;
}

// callback for sending data
void sendData(){
if (send_to_pi == 1){
Wire.write(digit_payload);
send_to_pi = 0;
} else if (offHook == 5) {
Wire.write(55);
offHook = 4;
} else if (offHook == 6) {
Wire.write(56);
}
}
