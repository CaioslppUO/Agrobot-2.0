**Descrição**

 * Programa que roda no arduino, fazendo a comunicação entre o Raspberry e placa do Hover Board.

**Defines**

 * STD_X e STD_Y: Valores que significam 'parado' para a placa do hover board.

 ---

**Variáveis Globais**

 * x e y: Variáveis utilizadas para manipula qual será o x e y enviados para a placa do hover board. Um controla a velocidade no eixo x e outro no y.

 * Speed, Steer e Limit: Variáveis 'virtuais' para controlar qual será o comando enviado para a placa do hover board.

 * information: Variável para manipular a informação recebida pelo protocolo UART.

 * stringComplete: Variável utilizada para saber quando começa e quando termina uma mensagem enviada pelo UART.

 * vector: Variável utilizada para enviar as informações para a placa do hover board.
 ---

**Funções**

 * void setup(){}: 

    * Função que roda as configurações iniciais do programa
    * Roda somente uma vez durante toda a execução do programa
    * Configura o monitor serial e a biblioteca de comunicação I2C(Wire.h)

 * void control(float _speed, float _steer, float _limit){}: 

    * Função que define as variáveis x e y que serão enviadas para a placa do hover board.
    * Verifica e corrige os valores recebidos como parâmetros para os adequar às regras de funcionamento da placa do hover board.

 * void loop(){}:

    * Função que executa em Loop a leitura pelo protocolo UART(Raspberry->arduino) e a escrita pelo protocolo I2C(Arduino->hover board).

 * void requestEvent(){}:

    * Função que responde às chamadas da placa do hover board, utilizando o protocolo I2C.
    * Utiliza a variável global vector para enviar os valores.

 * void readinfo(){}:

    * Função que reseta os flags da leitura após receber a comunicação pelo protocolo UART. Indica que a leitura foi finalizada.

 * void readUart(){}:

    * Função que trata as mensagens recebidas pelo UART e chama a função control.

 * void EventSerial(){}:

    * Função que se comunica com o Raspberry pelo protocolo UART.