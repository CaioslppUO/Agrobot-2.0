# Código do Arduino para controlar o robô:
 
  * Este código permite que o Arduino receba informações a partir da comunicação UART com o Raspberry e as evie para a placa do Hover Board através da comunicação I2C.

# Protocolo utilizado para a comunicação do Raspberry com o Arduino através do UART:

 * É necessário enviar para o Arduino através do UART três variáveis, seguindo o padrão: speed;steer;limit
       * O formato é exatamente o descrito acima, com as três variáveis e dois ponto e vírgulas separando-as
 * São necessárias três variáveis para controlar o robô:
       * Speed.
       * Steer.
       * Limit.
     
  * Speed aceita valores entre -100 e +100.
     *    0 significa parado.
     *  +100 significa potência total para frente.
     *  -100 significa potência total para trás.
  
   * Steer aceita valores entre -100 e +100.
     *    0 significa ir para frente.
     *  +100 significa ir para a direita.
     *  -100 significa ir para a esquerda.
     
   * Limit aceita valores entre 0 e +100.
     *   0 significa sem potência para as rodas.
     * +100 Significa potência total para as rodas.
 
 # Receiving values via Uart:
  
  * The procotol implemented is: ABCD;ABCD;ABCD;
 
  * Where ABCD are numbers:
    * the number A is the signal, if setted to 1 the singnal is +(Positive), else if setted 0 the signal is -(Negative).
    * BCD are the numbers that define the speed, steer and limit values, from 0 to 100.
    * Example:
         To send 80 in speed and turn full right, with limit on 100% of power: 1080;1100;1100;
