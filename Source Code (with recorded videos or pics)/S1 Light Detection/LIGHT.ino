#include <Wire.h>

#define ADDR 0b0100011

void setup() {
  Serial.begin(9600);   //设置波特率
  
  while (!Serial) {;}
  
  Wire.begin();
  Wire.beginTransmission(ADDR);
  Wire.write(0b00000001);
  Wire.endTransmission();
}
void loop() {
  int val = 0;    //初始化光照值

  Wire.beginTransmission(ADDR);
  Wire.write(0b00000111);
  Wire.endTransmission();
 
  Wire.beginTransmission(ADDR);
  Wire.write(0b00100000);
  Wire.endTransmission();
  delay(120);
  /*计算光照*/
  Wire.requestFrom(ADDR, 2);      //每次2byte
  for (val = 0; Wire.available() >= 1; ) {
    char c = Wire.read();
    val = (val << 8) + (c & 0xFF);
  }
  val = val / 1.2;
  /*输出光照数值*/
  Serial.print("当前光照值: ");
  Serial.println(val);
  delay(500);
}
