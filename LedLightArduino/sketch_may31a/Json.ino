#include <ArduinoJson.h>
#include <string>
StaticJsonDocument<200> doc;

void setup() {
  // Initialize serial port
  Serial.begin(9600);
     
}

void loop() {
  // not used in this example
while (!Serial) continue;
//    char json[] =
//      "{\"status\": \"off\", \"color\": \"(21, 30, 87)\"}";
     char* json = Serial.readString();
  Serial.println(json);
  // Deserialize the JSON document
//  DeserializationError error = deserializeJson(doc, json);

  // Test if parsing succeeds.
//  if (error) {
//    Serial.print(F("deserializeJson() failed: "));
//    Serial.println(error.f_str());
//    return;
//  }

  // Fetch values.
  
  const char* stat = doc["status"];
  String color = doc["color"];


  // Print values.
  Serial.println(stat);
  Serial.println(color);


}