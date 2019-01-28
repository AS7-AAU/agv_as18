#include <PID_v1.h>
#include "TimerThree.h"

#define INPUT_SIZE 30 //TODO: Check if this could be smaller or needs to be larger
#define MAX_ANG_VEL 48.0 //TODO: This value with fully charged battery

const byte encoder1A = 2; // Encoder 1 interrupt pin
const byte encoder1B = 3; // Encoder 1 interrupt pin
const byte encoder2A = 20; // Encoder 2 interrupt pin
const byte encoder2B = 21; // Encoder 2 interrupt pin
const byte AIN1 = 30;
const byte AIN2 = 31;
const byte PWMA = 9;
const byte BIN1 = 32;
const byte BIN2 = 33;
const byte PWMB = 10;
const byte STBY = 24;

volatile unsigned int counter1 = 0;
volatile unsigned int counter2 = 0;

double rotation1 = 0.0;
double setpoint1 = 0.0;
double output1 = 0.0;
double rotation2 = 0.0;
double setpoint2 = 0.0;
double output2 = 0.0;

double cmd_1 = 0.0;
double cmd_2 = 0.0;

PID PID1(&rotation1, &output1, &setpoint1, 1, 0, 0, DIRECT); //TODO: Tune gains
PID PID2(&rotation2, &output2, &setpoint2, 1, 0, 0, DIRECT);

void ISR_count1() { counter1++; }
void ISR_count2() { counter2++; }

void timer() {
  Timer3.detachInterrupt();  // Stop the timer
  noInterrupts();
  rotation1 = counter1 * 0.6981317; // Motor 1 speed (cm/s)
  counter1 = 0;
  rotation2 = counter2 * 0.6981317; // Motor 2 speed (cm/s)
  counter2 = 0;
  interrupts();
  Timer3.attachInterrupt(timer);  // Enable the timer
}

float saturate(float signal) {
  if(signal > MAX_ANG_VEL) {
    return MAX_ANG_VEL;
  } else if (signal < 0) {
    return 0.0;
  } else {
    return signal;
  }
}

void recvSetpoints() {
  if(Serial.available()) {
    char input[INPUT_SIZE + 1];
    byte size = Serial.readBytes(input, INPUT_SIZE);
    input[size] = 0;
    bool first = true;
    
    char* command = strtok(input, "&");
    while(command != 0) {
      if(first) {
        setpoint1 = atof(command);
        if(setpoint1 < 0) {
          digitalWrite(AIN1, LOW);
          digitalWrite(AIN2, HIGH);
          setpoint1 *= -1;
        } else {
          digitalWrite(AIN1, HIGH);
          digitalWrite(AIN2, LOW);
        }
        first = false;
        command = strtok(0, "&");
      } else {
        setpoint2 = atof(command);
        if(setpoint2 < 0) {
          digitalWrite(BIN1, HIGH);
          digitalWrite(BIN2, LOW);
          setpoint2 *= -1;
        } else {
          digitalWrite(BIN1, LOW);
          digitalWrite(BIN2, HIGH);
        }
        first = true;
        command = 0;
      }
    }
  }
}
 
void setup() {
  Serial.begin(250000); //TODO: Try higher baudrate for faster transmission
  Serial.setTimeout(5);
  
  Timer3.initialize(10000); // 100Hz
  Timer3.attachInterrupt(timer); // Enable the timer
  
  attachInterrupt(digitalPinToInterrupt(encoder1A), ISR_count1, CHANGE);
  attachInterrupt(digitalPinToInterrupt(encoder1B), ISR_count1, CHANGE);
  attachInterrupt(digitalPinToInterrupt(encoder2A), ISR_count2, CHANGE);
  attachInterrupt(digitalPinToInterrupt(encoder2B), ISR_count2, CHANGE);
  
  digitalWrite(STBY, HIGH);
  digitalWrite(AIN1, HIGH);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, HIGH);

  PID1.SetMode(AUTOMATIC);
  PID1.SetSampleTime(50); //TODO: Try faster sample time, see how it behaves
  PID1.SetOutputLimits(-MAX_ANG_VEL,MAX_ANG_VEL);
  PID2.SetMode(AUTOMATIC);
  PID2.SetSampleTime(50);
  PID2.SetOutputLimits(-MAX_ANG_VEL,MAX_ANG_VEL);
}

void loop() {
  recvSetpoints(); //DONE - TODO: Check if it slows the loop too much
  
  if(PID1.Compute()) {
    cmd_1 += output1;
    analogWrite(PWMA, saturate(cmd_1) * 255 / MAX_ANG_VEL);
  }
  if(PID2.Compute()) {
    cmd_2 += output2;
    analogWrite(PWMB, saturate(cmd_2) * 255 / MAX_ANG_VEL);
  }
}
