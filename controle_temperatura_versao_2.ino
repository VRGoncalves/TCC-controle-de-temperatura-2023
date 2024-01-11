//Bibliotecas
#include <PID_v1.h>

//Constantes PWM e PID
#define MIN_PWM 10
#define MAX_PWM 230
#define KP 32.0
#define KI 10.0
#define KD 1.0

//Declaração de pinos
#define pSENSOR		A0
#define pCONTROLE1	10
#define pCONTROLE2	11

//Definindo as variáveis que vamos utilizar
double Setpoint = 22.0;
double currentPWM;
float valor_analog_lm35 = 0;
float tensao;
double currentTemp;
double erro;
float samples[10];
int i;

//Especificando os parâmetros do construtor
PID myPID(&currentTemp, &currentPWM, &Setpoint, KP, KI, KD, REVERSE);


void setup(void){

  	Serial.begin(9600);
    
    pinMode(pSENSOR, INPUT);
  	pinMode(pCONTROLE1, OUTPUT);
    pinMode(pCONTROLE2, OUTPUT);

   //Inserindo os limites do PWM
   myPID.SetOutputLimits(MIN_PWM, MAX_PWM);

   //Ligando o PID e deixando-o em modo Automático
   myPID.SetMode(AUTOMATIC);
  
}


void loop(void){
  
  //Calcula a temperatura com base na média das amostras 
  readTemp();

  //Chama a função do algoritmo PID
  myPID.Compute();
   
  //Saída do Controle
  analogWrite(pCONTROLE1, currentPWM);
  analogWrite(pCONTROLE2, currentPWM);
  

  //Print Temperatura
  Serial.print("Temp: ");
  Serial.print(currentTemp);//4  
  Serial.print(", ");
 

  //Print PWM
  if (currentPWM < 100){
    Serial.print("PWM: ");
    Serial.print(currentPWM);//4  
    Serial.print(" , ");
  }
  else {
    Serial.print("PWM: ");
    Serial.print(currentPWM);//4  
    Serial.print(", ");
  }

  //Print Erro Temperatura
  Serial.print("Erro: ");
  error(currentTemp);
  Serial.print(", ");
  
  //Print Tempo
  if(millis()/1000 < 10){
    Serial.print("Tempo:  ");
    Serial.print(millis()/1000);
    Serial.println(",");
  }
  
  else{
    Serial.print("Tempo: ");
    Serial.print(millis()/1000);
    Serial.println(",");
  }  
  
  delay(3000);

}  


void readTemp(){
  
  //Faz amostragem de 10 leituras de temperatura e tira a média
  valor_analog_lm35 = 0;
  for(i = 0; i <= 9; i++){
    samples[i] = analogRead(pSENSOR);
    valor_analog_lm35 = valor_analog_lm35 + samples[i];
    delay(100);
  }
  valor_analog_lm35 = valor_analog_lm35 / 10.0; // dividimos pelo número de amostras
  tensao = ((valor_analog_lm35 * 5.0) / 1024.0); // Vamos converter esse valor para tensão elétrica
  currentTemp = tensao * 100.0; // dividimos a tensão por 0.010 que representa os 10 mV
}

void error(double CurrentTemp){

  erro = CurrentTemp - Setpoint;
  Serial.print(erro);
}


