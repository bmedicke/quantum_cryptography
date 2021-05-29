// read values from light dependant resistors
// and send them over the serial port:

int const BAUD = 9600;
int const LDR_PIN_HOR = A1;
int const LRD_PIN_VER = A3;
int const DELAY = 100; // in milliseconds.

int resistance_horizontal = 0;
int resistance_vertical = 0;

void setup() {
  Serial.begin(BAUD);
}

void loop() {  
  resistance_horizontal = analogRead(LDR_PIN_HOR);
  resistance_vertical = analogRead(LRD_PIN_VER);
  
  Serial.println(String(resistance_horizontal) + ",\t" + String(resistance_vertical));
  
  delay(DELAY);
}
