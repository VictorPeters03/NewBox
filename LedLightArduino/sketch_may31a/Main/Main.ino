#include <Adafruit_NeoPixel.h>
#include <ArduinoJson.h>
#include <string>

#define PIXEL_COUNT 60
#define PIXEL_PIN 6

String rValue;
String gValue;
String bValue;

String stat;
String music;
StaticJsonDocument<200> doc;

Adafruit_NeoPixel strip = Adafruit_NeoPixel(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);
//Adafruit_NeoPixel strip = Adafruit_NeoPixel(PIXEL_COUNT, PIXEL_PIN, NEO_GRB);
void setup(){
  jsonsetup();
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
  
}

void loop(){
  while(Serial.available() > 0){
    json();
  }
    // Fetch values.
    const String stat = doc["status"];
    const String music = doc["music"];
    const String color = doc["color"];

    if(stat == "on" && music == "on"){
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
      return;
    }else if(stat == "on" && music == "off"){
      fade();
      return;
    }else if(stat == "off" && music == "off"){
      colorWipe(strip.Color(0, 0, 0), 50);
      return;
    }
}
