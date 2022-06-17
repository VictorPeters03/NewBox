// Fill the dots one after the other with a color
void colorWipe(uint32_t c, uint8_t wait) {
  for(uint16_t i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, c);
      strip.show();
      delay(wait);
  }
}

String getValue(String data, char separator, int index){
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
