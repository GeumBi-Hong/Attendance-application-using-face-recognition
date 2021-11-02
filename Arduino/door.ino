#include <SoftwareSerial.h>

SoftwareSerial hc06(2,3); //Tx, Rx

int led = 11;
char state;

void setup() {
  Serial.begin(9600);
  hc06.begin(9600);
  pinMode(led, OUTPUT);  
}

void loop() {
  state=NULL;
  digitalWrite(led,HIGH);
  if (hc06.available()) {
    Serial.write("bluetooth available\n");
    state = hc06.read();
//    Serial.write(state);
//    Serial.write("\n");
    if(state=='p'){
      //Serial.write(hc06.read());
      Serial.write("state=");
      Serial.write(state);
      Serial.write("\n");
      digitalWrite(led,LOW);  //여기서 도어락이 열림
    }
     delay(1000);
     digitalWrite(led,HIGH);

}
}
