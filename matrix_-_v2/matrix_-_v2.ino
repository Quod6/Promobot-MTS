#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Max72xxPanel.h>

int pinCS = 10; // Attach CS to this pin, DIN to MOSI and CLK to SCK (cf http://arduino.cc/en/Reference/SPI )
int numberOfHorizontalDisplays = 4;
int numberOfVerticalDisplays = 2;

Max72xxPanel matrix = Max72xxPanel(pinCS, numberOfHorizontalDisplays, numberOfVerticalDisplays);



void setup() {
  Serial.begin(9600);
  
  matrix.setIntensity(15);

// Adjust to your own needs
//  matrix.setPosition(0, 0, 0); // The first display is at <0, 0>
//  matrix.setPosition(1, 1, 0); // The second display is at <1, 0>
//  matrix.setPosition(2, 2, 0); // The third display is at <2, 0>
//  matrix.setPosition(3, 3, 0); // And the last display is at <3, 0>


//настройка позиций экранов
matrix.setPosition(0, 0, 0);
matrix.setPosition(2, 1, 0);
matrix.setPosition(4, 2, 0);
matrix.setPosition(6, 3, 0);
matrix.setPosition(1, 0, 1);
matrix.setPosition(3, 1, 1);
matrix.setPosition(5, 2, 1);
matrix.setPosition(7, 3, 1);

//  ...
//matrix.setRotation(0, 1);    // The first display is position upside down


//настройка ориентации экранов
matrix.setRotation(0, 1);
matrix.setRotation(2, 1);
matrix.setRotation(4, 1);
matrix.setRotation(6, 1);
matrix.setRotation(1, 1);
matrix.setRotation(3, 1);
matrix.setRotation(5, 1);
matrix.setRotation(7, 1);

//очитска экрана и рисовыание глаз
matrix.fillScreen(LOW);
matrix.write();
glaza();
//за функцию отрисовки глаз отвечает функция glaza();

//  matrix.setRotation(3, 2);    // The same hold for the last display
}

int wait = 50;
int inc = -2;

void loop() {
  //подмигивание - winking();
  //моргание - blinking();

  //сейчас код считываеет символ с Serial монитора и выводит нужную картинку
  char cmd = Serial.read();
  while (1)
  {
    if (cmd == 'w')
    {
      winking();
    }
    else if (cmd == 'b')
    {
      blinking();
    }
    else if (cmd == 'd' || cmd == 'g')
    {
      glaza();
    }
    cmd = Serial.read();
  }


  
  /*for ( int x = 0; x < matrix.width() - 1; x++ ) {
    matrix.fillScreen(LOW);
    matrix.drawLine(x, 0, matrix.width() - 1 - x, matrix.height() - 1, HIGH);
    matrix.write(); // Send bitmap to display
    delay(wait);
  }
  for ( int y = 0; y < matrix.height() - 1; y++ ) {
    matrix.fillScreen(LOW);
    matrix.drawLine(matrix.width() - 1, y, 0, matrix.height() - 1 - y, HIGH);
    matrix.write(); // Send bitmap to display
    delay(wait);
  }
  wait = wait + inc;
  if ( wait == 0 ) inc = 2;
  if ( wait == 50 ) inc = -2;*/
}
