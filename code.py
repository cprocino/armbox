#include <Arduino.h>

#include <Servo.h>

Servo Myservo1;

Servo Myservo2;

int SERVO_PIN1 = 3;

int SERVO_PIN2 = 5;

int ServoButton = 4;

int dropTime = 2000;

void setup() {

Serial.begin(9600);

Myservo1.attach(SERVO_PIN1);

Myservo2.attach(SERVO_PIN2);
}

void loop() {

Serial.println(digitalRead(ServoButton));

if (digitalRead(ServoButton) == 1) {

  Myservo1.write(180);

  delay(1000);

  Myservo2.write(180);

   delay(dropTime);

  Myservo2.write(0);

  delay(1000);

  Myservo1.write(0);
}

else{

  Serial.println("No");

}

delay(500);
}
