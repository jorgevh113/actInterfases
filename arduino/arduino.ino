String data;

void setup() {
Serial.begin(9600);
}

void loop() {
  if(Serial.available()){
    data = Serial.readString();
    delay(100);
    Serial.println("Mensaje recibido");
    
  }
}