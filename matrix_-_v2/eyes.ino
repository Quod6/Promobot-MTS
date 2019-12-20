byte default1[16] =
{
  0b00011111,
  0b00111111,
  0b01110000,
  0b11100000,
  0b11000111,
  0b11001111,
  0b11001111,
  0b11001110,
  0b11001110,
  0b11001111,
  0b11001111,
  0b11000111,
  0b11100000,
  0b01110000,
  0b00111111,
  0b00011111,
};

byte default2[16] =
{
  0b11111000,
  0b11111100,
  0b00001110,
  0b00000111,
  0b11100011,
  0b11110011,
  0b11110011,
  0b01110011,
  0b01110011,
  0b11110011,
  0b11110011,
  0b11100011,
  0b00000111,
  0b00001110,
  0b11111100,
  0b11111000,
};

byte blink1_1[16] =
{
  0b00000000,
  0b00000000,
  0b00000000,
  0b00000000,
  0b00111111,
  0b01111111,
  0b11001111,
  0b11001110,
  0b11001110,
  0b11001111,
  0b01111111,
  0b00111111,
  0b00000000,
  0b00000000,
  0b00000000,
  0b00000000,
};

byte blink1_2[16] =
{
  0b00000000,
  0b00000000,
  0b00000000,
  0b00000000,
  0b11111100,
  0b11111110,
  0b11110011,
  0b01110011,
  0b01110011,
  0b11110011,
  0b11111110,
  0b11111100,
  0b00000000,
  0b00000000,
  0b00000000,
  0b00000000,
};

byte blink2[16] =
{
  0b00000000,
  0b00000000,
  0b00000000,
  0b00000000,
  0b00000000,
  0b00000000,
  0b00000000,
  0b11111111,
  0b11111111,
  0b00000000,
  0b00000000,
  0b00000000,
  0b00000000,
  0b00000000,
  0b00000000,
  0b00000000,
};

//  0b00011111,
//  0b00111111,
//  0b01110000,
//  0b11100000,
//  0b11000000,
//  0b11000000,
//  0b11000000,
//  0b11000000,
//  0b11000000,
//  0b11000000,
//  0b11000000,
//  0b11000000,
//  0b11100000,
//  0b01110000,
//  0b00111111,
//  0b00011111,
//
//  0b11111000,
//  0b11111100,
//  0b00001110,
//  0b00000111,
//  0b00000011,
//  0b00000011,
//  0b00000011,
//  0b00000011,
//  0b00000011,
//  0b00000011,
//  0b00000011,
//  0b00000011,
//  0b00000111,
//  0b00001110,
//  0b11111100,
//  0b11111000,

void glaz(String num)
{
  if (num == "left")
  {
    matrix.fillScreen(LOW);
    matrix.drawBitmap(0, 0, default1, 8, 16, 1);
    matrix.drawBitmap(8, 0, default2, 8, 16, 1);
    matrix.write();
  }
  else if (num == "right")
  {
    matrix.fillScreen(LOW);
    matrix.drawBitmap(16, 0, default1, 8, 16, 1);
    matrix.drawBitmap(24, 0, default2, 8, 16, 1);
    matrix.write();
  }
  else
  {
    matrix.fillScreen(LOW);
    matrix.drawBitmap(0, 0, default1, 8, 16, 1);
    matrix.drawBitmap(8, 0, default2, 8, 16, 1);
    matrix.drawBitmap(16, 0, default1, 8, 16, 1);
    matrix.drawBitmap(24, 0, default2, 8, 16, 1);
    matrix.write();
  }
}

void glaza()
{
   matrix.fillScreen(LOW);
   matrix.drawBitmap(0, 0, default1, 8, 16, 1);
   matrix.drawBitmap(8, 0, default2, 8, 16, 1);
   matrix.drawBitmap(16, 0, default1, 8, 16, 1);
   matrix.drawBitmap(24, 0, default2, 8, 16, 1);
   matrix.write();
}

void blinking()
{
  glaza(); // рисуем глаза
  delay(500);
  matrix.fillScreen(LOW);
  matrix.drawBitmap(0, 0, blink1_1, 8, 16, 1);
  matrix.drawBitmap(8, 0, blink1_2, 8, 16, 1);
  matrix.drawBitmap(16, 0, blink1_1, 8, 16, 1);
  matrix.drawBitmap(24, 0, blink1_2, 8, 16, 1);
  matrix.write(); // первая стадия закрытия глаза
  delay(150);
  matrix.fillScreen(LOW);
  matrix.drawBitmap(0, 0, blink2, 8, 16, 1);
  matrix.drawBitmap(8, 0, blink2, 8, 16, 1);
  matrix.drawBitmap(16, 0, blink2, 8, 16, 1);
  matrix.drawBitmap(24, 0, blink2, 8, 16, 1);
  matrix.write(); // закрытый глаз
  delay(400);
  matrix.fillScreen(LOW);
  matrix.drawBitmap(0, 0, blink1_1, 8, 16, 1);
  matrix.drawBitmap(8, 0, blink1_2, 8, 16, 1);
  matrix.drawBitmap(16, 0, blink1_1, 8, 16, 1);
  matrix.drawBitmap(24, 0, blink1_2, 8, 16, 1);
  matrix.write(); // первая стадия закрытия глаза
  delay(150);
  glaza(); // риусем глаза
}

void winking()
{
  matrix.fillScreen(LOW);
  glaz("left");
  matrix.drawBitmap(16, 0, blink1_1, 8, 16, 1);
  matrix.drawBitmap(24, 0, blink1_2, 8, 16, 1);
  matrix.write(); // правый глаз чуть закрывается
  
  delay(50);
  
  matrix.fillScreen(LOW);
  glaz("left");
  matrix.drawBitmap(16, 0, blink2, 8, 16, 1);
  matrix.drawBitmap(24, 0, blink2, 8, 16, 1);
  matrix.write(); // левый глаз открыт а правый закрыт

  delay(170);

  matrix.fillScreen(LOW);
  glaz("left");
  matrix.drawBitmap(16, 0, blink1_1, 8, 16, 1);
  matrix.drawBitmap(24, 0, blink1_2, 8, 16, 1);
  matrix.write(); // левый глаз открыт а правый чуть приоткрыт

  delay(50);

  glaza();
}
