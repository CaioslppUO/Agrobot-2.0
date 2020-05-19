**Descrição**

 * Programa que gerência as variáveis de inicialização do robô.

 ---

**Funções**

 * checkVariables(serverIp,enableUart,enableRelay,uartAmount,enableFaceDetect,rootPath):

    * Recebe as variáveis de inicialização, verifica se todas estão corretas e retorna uma mensagem.
    * A mensagem indica se alguma variável está incorreta ou se todas estão corretas.

---

**Classes**
  
  * LauncherVariables():

    * Classe que gerencia as variáveis.

  * *Métodos*

    * variableSeparator(self,variables):

        * Separa as variáveis recebidas em de um array.
        * Se todas estiverem corretas continua a execução do programa. Caso contrário, finaliza o programa e mostra a mensagem de erro.