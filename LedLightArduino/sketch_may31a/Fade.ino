#include <Adafruit_NeoPixel.h>
#define PIXEL_COUNT 60
#define PIXEL_PIN 6

Adafruit_NeoPixel strip = Adafruit_NeoPixel(PIXEL_COUNT, PIXEL_PIN, NEO_GRB);


double lastColorUpdate = 0;     // Epoch of last color update (local or remote)
String colorFromID;             // String, Tracks who sent the color (for debug)
uint16_t colorRecieved;         // 0 - 255, Tracks the color received from another lamp
bool lampOn = 0;                // Tracks if the lamp is lit
uint8_t activeColor = 0;        // 0 - 255, Tracks what color is currently active (default to red)
uint8_t activeR = 255;          // 0 - 255, Red component of activeColor;
uint8_t activeG = 0;            // 0 - 255, Green component of activeColor;
uint8_t activeB = 0;            // 0 - 255, Blue component of activeColor;
uint32_t decayTime = 3600;      // Turn off light after elapsed seconds
uint32_t decayDelay = 5;        // Seconds between decay fade-out
uint32_t decayDelayCounter = 0; // Tracker for decayDelay
int16_t lampBrightness = 70;     // 0 - 255, Tracks current lamp brightness
byte activePixels = 0;          // Tracks Pixels active during various functions
uint32_t fadeColor = 0;

void setup() {
    strip.begin();
}

void loop() {
    idleChristmas();
    delay(20);
}

void idleChristmas() {
    uint16_t newR, newG, newB, startR, startG, startB, endR, endG, endB;
    uint32_t color = wheelColor(fadeColor, lampBrightness);
    endR = (uint16_t)((color >> 16) & 0xff); // Splits out new color into separate R, G, B
    endG = (uint16_t)((color >> 8) & 0xff);
    endB = (uint16_t)(color & 0xff);
    for (uint16_t j = 0; j < activePixels; j++) {
        long startRGB = strip.getPixelColor(j); // Get pixel's current color
        startR = (uint16_t)((startRGB >> 16) & 0xff); // Splits out current color into separate R, G, B
        startG = (uint16_t)((startRGB >> 8) & 0xff);
        startB = (uint16_t)(startRGB & 0xff);
        if ( startR > endR ) {
            newR = startR - 1;
        } else if ( startR < endR ) {
            newR = startR + 1;
        } else {
            newR = endR;
        }
        if ( startG > endG ) {
            newG = startG - 1;
        } else if ( startG < endG ) {
            newG = startG + 1;
        } else {
            newG = endG;
        }
        if ( startB > endB ) {
            newB = startB - 1;
        } else if ( startB < endB ) {
            newB = startB + 1;
        } else {
            newB = endB;
        }
        
        //Catch overflows
        newR %= 255;
        newG %= 255;
        newB %= 255;
        
        //newR = startR + (endR - startR) * fade / 255;// / strip.numPixels();// Color mixer
        //newG = startG + (endG - startG) * fade / 255;// / strip.numPixels();
        //newB = startB + (endB - startB) * fade / 255;// / strip.numPixels();
        strip.setPixelColor(j, newR, newG, newB);
        if ( j >= strip.numPixels() - 1 && endR == startR && endG == startG && endB == startB) {
            if ( fadeColor == 0 ) {
                fadeColor = 85;
            } else {
                fadeColor = 0;
            }
            activePixels = 0;
        }
    }
    strip.show();
    if ( activePixels < strip.numPixels() ) activePixels++;
}

uint32_t wheelColor(uint16_t WheelPos, uint16_t iBrightness) {
  float R, G, B;
  float brightness = iBrightness / 255.0;

  if (WheelPos < 85) {
    R = WheelPos * 3;
    G = 255 - WheelPos * 3;
    B = 0;
  } else if (WheelPos < 170) {
    WheelPos -= 85;
    R = 255 - WheelPos * 3;
    G = 0;
    B = WheelPos * 3;
  } else {
    WheelPos -= 170;
    R = 0;
    G = WheelPos * 3;
    B = 255 - WheelPos * 3;
  }
  activeR = R * brightness;// + .5;
  activeG = G * brightness;// + .5;
  activeB = B * brightness;// + .5;
  return strip.Color((byte) activeR,(byte) activeG,(byte) activeB);
}

void colorFade(uint8_t r, uint8_t g, uint8_t b, uint8_t wait) {
  for(uint16_t i = 0; i < strip.numPixels(); i++) {
      uint8_t startR, startG, startB;
      uint32_t startColor = strip.getPixelColor(i); // get the current colour
      startB = startColor & 0xFF;
      startG = (startColor >> 8) & 0xFF;
      startR = (startColor >> 16) & 0xFF;  // separate into RGB components

      if ((startR != r) || (startG != g) || (startB != b)){  // while the curr color is not yet the target color
        if (startR < r) startR++; else if (startR > r) startR--;  // increment or decrement the old color values
        if (startG < g) startG++; else if (startG > g) startG--;
        if (startB < b) startB++; else if (startB > b) startB--;
        strip.setPixelColor(i, startR, startG, startB);  // set the color
        strip.show();
        // delay(1);  // add a delay if its too fast
      }
      delay(1000);
  }
}