# Código do Arduino para controlar o robô:
 
  * Este código permite que o Arduino receba informações a partir da comunicação UART com o Raspberry e as evie para a placa do Hover Board através da comunicação I2C.

---

# Protocolo utilizado para a comunicação do Raspberry com o Arduino através do UART:

 * É necessário enviar para o Arduino através do UART três variáveis, seguindo o padrão: speed;steer;limit;
       * O formato é exatamente o descrito acima, com as três variáveis e três ponto e vírgulas separando-as
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
 
 ---
 
 # Recebendo os valores por UART:
  
  * O protocolo implementado é: ABCD;ABCD;ABCD onde ABCD são números com os seguintes significados:
  
       * O número A é o sinal, com duas opções possíveis. 1 significa que o número é positivo(+). 0 significa que o númeor é negativo(-). BCD são números que definem a velocidade, a direção e o limite. É necessário que todas as letras(ABCD) sejam preenchidas, mesmo que com o valor 0.


  * Exêmplo de uso:
       * Para enviar 80% de velocidade, virando 100% para a esquerda, com 50% da potência máxima, é necessário enviar o seguinte comando: 1080;0100;1100;
