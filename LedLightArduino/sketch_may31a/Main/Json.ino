const unsigned int MAX_LENGTH = 70;


void jsonsetup() {
  Serial.setTimeout(3000);
  // Initialize serial port
  Serial.begin(1200);
}

void json() {
    static char message[MAX_LENGTH];
    static unsigned int message_pos = 0;

    char inByte = Serial.read();

    if (inByte != '\n' && message_pos < MAX_LENGTH -1){
      message[message_pos] = inByte;
      message_pos++;
    }else {
      message[message_pos] = '\0';
      message_pos = 0;

      String json = message;
      DeserializationError error = deserializeJson(doc, json);
      
      // Test if parsing succeeds.
      if (error) {
        Serial.print(F("deserializeJson() failed: "));
        Serial.println(error.f_str());
        return;
      }
    }
}
