#include <ArduinoJson.h>
#include <string>
#include <Adafruit_NeoPixel.h>
String rValue;
String gValue;
String bValue;
// Parameter 1 = number of pixels in strip
// Parameter 2 = pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_RGB     Pixels are wired for RGB bitstream
//   NEO_GRB     Pixels are wired for GRB bitstream
//   NEO_KHZ400  400 KHz bitstream (e.g. FLORA pixels)
//   NEO_KHZ800  800 KHz bitstream (e.g. High Density LED strip)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(60, 6, NEO_GRB + NEO_KHZ800);

StaticJsonDocument<200> doc;

void setup() {
  // Initialize serial port
  Serial.begin(300);
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
}

void loop() {
  // not used in this example
while (!Serial) continue;
//    char json[] =
//       "{\"status\": \"off\", \"color\": \"(21, 30, 87)\"}";
     String json = Serial.readStringUntil('#');
  
  while(Serial.available() > 0) {Serial.read();}
//    Serial.print("I got: @");
//    Serial.print(json);
//    Serial.println("@");
  // Deserialize the JSON document
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
  const char*  color = doc["color"];
 
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