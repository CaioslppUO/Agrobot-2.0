#include <Wire.h>
#include <math.h>

/** Valor padrão de direção 0 do robô. */
#define STD_X 130
/** Valor padrão de velocidade 0 do robô. */
#define STD_Y 123
/** Pino utilizado para controlar o relé que liga e desliga o motor */
#define POWER 8
/** Pino utilizado para controlar o LED de teste de conexão */
#define LED 7

/** Variável utilizada para manipular qual será o x enviado para o robô. Significa a direção enviada. */
int x;
/** Variável utilizada para manipular qual será o u enviado para o robô. Significa a velocidade enviada. */
int y;

/** Variável 'virtual' que controla a velocidade do robô */
int Speed;
/** Variável 'virtual' que controla a direção do robô */
int Steer;
/** Variável 'virtual' que controla o limite do robô */
int Limit; 
/** Variável que controla o acionamento do relé */
int power;

/** Variável para manipular a informação recebida pelo protocolo UART. */
String information = "";

/** Variável utilizada para saber quando começa e quando termina uma mensagem
 enviada pelo UART. */
bool stringComplete;

/** Variável utilizada para enviar as informações para a placa do hover board. */
uint8_t vector[6] = {218, 130, 0, 1, 0, 1};

/** Função que roda as configurações iniciais do programa. \n
  Roda somente uma vez durante toda a execução do programa. \n
  Configura o monitor serial e a biblioteca de comunicação I2C(Wire.h). */
void setup(){
  Serial.begin(9600);
  Wire.begin(0x52);                
  Wire.onRequest(requestEvent);
  pinMode(LED,OUTPUT);
  pinMode(POWER,OUTPUT);
}

/** Função que define as variáveis x e y que serão enviadas para a placa do hover board. \n
  Verifica e corrige os valores recebidos como parâmetros para os adequar às regras de funcionamento
  placa do hover board. */
void control(float _speed, float _steer, float _limit, int power){
  float  coefficient_speed, coefficient_steer;  
  coefficient_speed = (_speed/100) * abs(_limit);
  coefficient_steer = (_steer/100) * abs(_limit);
  y = STD_Y +  coefficient_speed;
  if(y < 35) y = 35; if(y > 230) y = 230; 
  x = STD_X +  coefficient_steer;
  if(x < 35) x = 35; if(x > 230) x = 230;
  if(power == 1){
    digitalWrite(POWER, HIGH);
    digitalWrite(POWER, LOW);
  }else{
    digitalWrite(POWER, LOW);
  }
}

/** Função que executa em Loop a leitura pelo protocolo UART(Raspberry->arduino)
 e a escrita pelo protocolo I2C(Arduino->hover board). */
void loop(){ 
  readUart();
}

/** Função que responde às chamadas da placa do hover board, utilizando o
 protocolo I2C. \n
 Utiliza a variável global vector para enviar os valores. */
void requestEvent() {
  int i;
  vector[0] = x;
  vector[1] = y;
  for(i = 0; i < 6; i++){
    Wire.write(vector,6);
  }
}

/** Função que reseta os flags da leitura após receber a comunicação pelo protocolo
 UART. \n
 Indica que a leitura foi finalizada. */
void readinfo(){
      information = "";
      stringComplete = false;  
}

/** Função que trata as mensagens recebidas pelo UART e chama a função control. */
void readUart() {
  String temp;
  char sinal;
  EventSerial();
  if(stringComplete){
    digitalWrite(LED, HIGH);
    Serial.print("Info = {");
    Serial.print(information);
    Serial.println("}");
    
    temp="";
    sinal = information[0] - 48; // 1 se o sinal for igual a '1' e 0 se o sinal for igual a '0'
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

    temp="";
    temp += information[14];
    power = temp.toInt();
    
    control(Speed,Steer,Limit,power);
    readinfo(); // Reseta os flags para a próxima leitura
  }
}

/** Função que se comunica com o Raspberry pelo protocolo UART. */
void EventSerial() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    information += inChar;
    if (inChar == ';') {
      stringComplete = true;
    }
  }
}
