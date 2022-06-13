#include <ArduinoJson.h>
#include <ArduinoJson.h>
#include <string>

#define PIXEL_COUNT 60
#define PIXEL_PIN 6

String rValue;
String gValue;
String bValue;

Adafruit_NeoPixel strip = Adafruit_NeoPixel(60, 6, NEO_GRB + NEO_KHZ800);