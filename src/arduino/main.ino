#include <Wire.h>
#include <math.h>

/*Standard x and y
 * These are the values that keep the robot stationary
 * They range from 30 to 230, where 30 is go Back and 230 is go Ahead for y. For x, 30 is go Left and 230 is go Right
*/
#define STD_X 130
#define STD_Y 123

//Global variables
int x,y; //Values sent to the main board
int Speed,Steer,Limit; //Values used to convert string -> int, recieved through UART
String information=""; //String recieved through UART
bool stringComplete; //Flag to check if the message is complete

//Vector send through I2C
uint8_t vector[6] = {218, 130, 0, 1, 0, 1};

void setup(){
  Serial.begin(9600);
    
  //i2c
  Wire.begin(0x52);                
  Wire.onRequest(requestEvent);  
}

//Function that checks if speed and steer are correct, transform them according to the limit, and set the global x and y
void control(float _speed, float _steer, float _limit){
  float  coefficient_speed, coefficient_steer;  
  coefficient_speed = (_speed/100) * abs(_limit);
  coefficient_steer = (_steer/100) * abs(_limit);
  y = STD_Y +  coefficient_speed;
  if(y < 35) y = 35; if(y > 230) y = 230; 
  x = STD_X +  coefficient_steer;
  if(x < 35) x = 35; if(x > 230) x = 230;
 
}

void loop(){ 
  //read menssages and call control funtion
  readUart();
}

//Send information to the main board, when requested
void requestEvent() {
  int i;
  vector[0] = x;
  vector[1] = y;
  for(i = 0; i < 6; i++){
    Wire.write(vector,6);
  }
}

//Auxiliary funtion to uart communication
void readinfo(){
      information = "";
      stringComplete = false;  
}

//Convert the uart menssage and call control
void readUart() {
  String temp;
  char sinal;
  EventSerial();
  if(stringComplete){
    Serial.print("Info = {");
    Serial.print(information);
    Serial.println("}");
    temp="";
    sinal = information[0] - 48; //1 if sinal = '1' and 0 if sinal = '0'
    temp += information[1];
    temp += information[2];
    temp += information[3];
    Speed = temp.toInt();
    if(!sinal) Speed *= -1;
    
    temp="";
    sinal = information[5] - 48;
    temp += information[6];
    temp += information[7];
    temp += information[8];
    Steer = temp.toInt();
    if(!sinal) Steer *= -1;
    
    temp="";
    sinal = information[10] - 48;
    temp += information[11];
    temp += information[12];
    temp += information[13];
    Limit = temp.toInt();
    if(!sinal) Limit *= -1;
    
    control(Speed,Steer,Limit);
    readinfo(); //reset the flags for the next reading
  }
}

//Receive uart sinal, and save it
void EventSerial() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    information += inChar;
    if (inChar == ';') {
      stringComplete = true;
    }
  }
}
