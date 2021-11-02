#include "MLX90615.h"
#include <I2cMaster.h>
#include <SoftwareSerial.h>

#define SDA_PIN 3 
#define SCL_PIN 2
#define trigPin 4
#define echoPin 7
#define BT_RXD 0
#define BT_TXD 1

SoftI2cMaster i2c(SDA_PIN, SCL_PIN);
MLX90615 mlx90615(DEVICE_ADDR, &i2c);

#include <Wire.h>
#include <LiquidCrystal.h>
LiquidCrystal lcd(4,6,10,11,12,13);

SoftwareSerial bluetooth(BT_RXD, BT_TXD);

void setup()
{
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  delay(100);
  bluetooth.begin(9600);
  delay(100);
  lcd.begin(16,2);
}

long microsecondsToCentimeters(long microseconds){
  return microseconds /29 /2;
}

void loop()
{
  
  long duration, cm;
  float tem;

  digitalWrite(trigPin, LOW);
  delayMicroseconds(15);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(15);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);

  cm = microsecondsToCentimeters(duration);
  
  lcd.setCursor(0, 0);
  lcd.print("Your temperature: ");
  lcd.setCursor(0, 1);
  tem = mlx90615.getTemperature(MLX90615_OBJECT_TEMPERATURE)+3;
  lcd.print(tem);
  delay(1000);

  if((tem > 36) && (cm >3000 || cm <10) && cm != 0){
    Serial.println(tem);
  }
  
}
