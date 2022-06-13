#include <ArduinoJson.h>
#include <string>
#include <Adafruit_NeoPixel.h>
String rValue;
String gValue;
String bValue;

Adafruit_NeoPixel strip = Adafruit_NeoPixel(60, 6, NEO_GRB + NEO_KHZ800);

StaticJsonDocument<200> doc;
const unsigned int MAX_LENGTH = 60;
void setup() {
  Serial.setTimeout(3000);
  // Initialize serial port
  Serial.begin(1200);
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'

}

void loop() {
  while (!Serial) continue;
  while(Serial.available() > 0){
    static char message[MAX_LENGTH];
    static unsigned int message_pos = 0;

    char inByte = Serial.read();

    if (inByte != '\n' && message_pos < MAX_LENGTH -1){
      message[message_pos] = inByte;
      message_pos++;
    }else {
      message[message_pos] = '\0';
      Serial.println(message);
      message_pos = 0;

      String json = message;
      Serial.println(json);
      DeserializationError error = deserializeJson(doc, json);
      Serial.println("Works");
      // Test if parsing succeeds.
      if (error) {
        Serial.print(F("deserializeJson() failed: "));
        Serial.println(error.f_str());
        return;
      }
      // Fetch values.
      const char* stat = doc["status"];
      const char* color = doc["color"];

      //trim off unnecessary characters
      String rValue = getValue(color, ',', 0);
      rValue.remove(0, 1);
      String gValue = getValue(color, ',', 1);
      gValue.remove(0, 1);
      String bValue = getValue(color, ',', 2);
      bValue.remove(0, 1);
      int lastIndex = bValue.length()-1;
      bValue.remove(lastIndex, -1); 

      
      colorWipe(strip.Color(bValue.toInt(), rValue.toInt(), gValue.toInt()), 50);
    }
  }
}

String getValue(String data, char separator, int index)
{
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length()-1;

  for(int i=0; i<=maxIndex && found<=index; i++){
    if(data.charAt(i)==separator || i==maxIndex){
        found++;
        strIndex[0] = strIndex[1]+1;
        strIndex[1] = (i == maxIndex) ? i+1 : i;
    }
  }
  return found>index ? data.substring(strIndex[0], strIndex[1]) : "";
}


// Fill the dots one after the other with a color
void colorWipe(uint32_t c, uint8_t wait) {
  for(uint16_t i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, c);
      strip.show();
      delay(wait);
  }
}