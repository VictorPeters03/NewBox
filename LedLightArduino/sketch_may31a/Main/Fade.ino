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


void fade() {
    idleChristmas();
    delay(10);
}
