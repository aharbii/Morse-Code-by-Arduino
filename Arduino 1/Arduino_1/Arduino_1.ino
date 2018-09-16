// This Code written by Ahmed Harbi on August.2018

// Defined Laser & Buzzer
#define Laser 13
#define Buzzer 9

// Enter Morse Code Library
char* MorseCode[] = {
  ".-",     // A
  "-...",   // B
  "-.-.",   // C
  "-..",    // D
  ".",      // E
  "..-.",   // F
  "--.",    // G
  "....",   // H
  "..",     // I
  ".---",   // J
  "-.-",    // K
  ".-..",   // L
  "--",     // M
  "-.",     // N
  "---",    // O
  ".--.",   // P
  "--.-",   // Q
  ".-.",    // R
  "...",    // S
  "-",      // T
  "..-",    // U
  "...-",   // V
  ".--",    // W
  "-..-",   // X
  "-.--",   // Y
  "--.."    // Z
};

//Enter Numbers Library
char* Numbers[] = {
  "-----",   // 0
  ".----",   // 1
  "..---",   // 2
  "...--",   // 3
  "....-",   // 4
  ".....",   // 5
  "-....",   // 6
  "--...",   // 7
  "---..",   // 8
  "----."    // 9
};

//Define I/Os
void setup() {
  pinMode(Laser, OUTPUT);
  pinMode(Buzzer, OUTPUT);
  Serial.begin(9600);
}



void loop() {

  // Reset the readed data every loop
  char letter;
  

  // Check if bluetooth is connected
  if (Serial.available() > 0) {

    // Read data from bluetooth
    letter = Serial.read();


    // Lower case letters
    if (letter >= 'a' && letter <= 'z') {
      // Call the letter element then apply morse code decoder
      decoder(MorseCode[letter - 'a']);
    }

    // Capital case letters
    else if (letter >= 'A' && letter <= 'Z') {
      // Call the letter element then apply morse code decoder
      decoder(MorseCode[letter - 'A']);
    }

    // Numbers
    else if (letter >= '0' && letter <= '9') {
      // Call Number's Element then apply morse code decoder
      decoder(Numbers[letter - '0']);
    }

    // Space Case
    else if (letter == ' ') {
      delay(600);
    }
    
    // Print output back
    if (letter == '\0') {
      Serial.println("");
    } else {
      Serial.print(letter);
    }
  }
}

// Set the decoder [flash for each letter in received string]
void decoder (char* x) {

  // Counter
  int i = 0;

  //Decoder
  while (x[i] != '\0') {
    flashType(x[i]);
    i++;
  }
  
  // Delay between every letter
  delay(250);
}



// Dash or Dot 
void flashType (char data) {

  // Turn laser & Buzzer on
  digitalWrite(Laser, HIGH);
  tone(Buzzer, 1000);

  // DOT
  if (data == '.') {
    delay(200);
  }

  //Dash
  if (data == '-') {
    delay(600);
  }

  // Turn laser & Buzzer off
  digitalWrite(Laser, LOW);
  noTone(Buzzer);

  //Delay before the following dash/dot
  delay(200); 
}

/*Problems:
 *1.cann't control laser or buzzer itself
 */
