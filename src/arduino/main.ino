#include <Wire.h>
#include <math.h>

//X e Y padrões
#define STD_X 130
#define STD_Y 123

//Variáveis globais
int x,y;
int Speed,Steer,Limit; 
String information="";
bool stringComplete;

//Vetor enviado pela comunicação I2C
uint8_t vector[6] = {218, 130, 0, 1, 0, 1};

//Configurações iniciais
void setup(){
  Serial.begin(9600);
    
  //i2c
  Wire.begin(0x52);                
  Wire.onRequest(requestEvent);  
}

//Função que verifica se a velocidade, a direção e o limite estão corretos, e depois define as variáveis globais x e y
void control(float _speed, float _steer, float _limit){
  float  coefficient_speed, coefficient_steer;  
  coefficient_speed = (_speed/100) * abs(_limit);
  coefficient_steer = (_steer/100) * abs(_limit);
  y = STD_Y +  coefficient_speed;
  if(y < 35) y = 35; if(y > 230) y = 230; 
  x = STD_X +  coefficient_steer;
  if(x < 35) x = 35; if(x > 230) x = 230;
 
}

//Lê o canal de comunicação UART e executa o tratamento para os dados recebidos
void loop(){ 
  readUart();
}

//Envia informação para a placa do hover board quando requisitado
void requestEvent() {
  int i;
  vector[0] = x;
  vector[1] = y;
  for(i = 0; i < 6; i++){
    Wire.write(vector,6);
  }
}

//Função auxiliar para tratar a comunicação UART
void readinfo(){
      information = "";
      stringComplete = false;  
}

//Traduz a mensagem recebida pelo UART e as envia para a placa do hover board
void readUart() {
  String temp;
  char sinal;
  EventSerial();
  if(stringComplete){
    Serial.print("Info = {");
    Serial.print(information);
    Serial.println("}");
    temp="";
    sinal = information[0] - 48; //1 se o sinal for igual a '1' e 0 se o sinal for igual a '0'
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
    readinfo(); //Reseta os flags para a próxima leitura
  }
}

//recebe o sinal pelo UART e o salva
void EventSerial() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    information += inChar;
    if (inChar == ';') {
      stringComplete = true;
    }
  }
}
