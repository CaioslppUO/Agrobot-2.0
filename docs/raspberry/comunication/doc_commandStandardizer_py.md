**Descrição**

 * Classe que padroniza os comandos recebidos pelo commandPriorityDecider para serem enviados internamente pelo ROS.

---


**Classes**

 * CommandStandardizer():

    * Classe que gerencia a padronização dos comandos.

    * *Métodos*

        * checkSpeed(self,speed):

            * Método que verifica se a velocidade está dentro dos limites aceitáveis.
            * Caso não esteja, corrige a variável e a retorna.

        * checkSteer(self,steer):

            * Método que verifica se a direção está dentro dos limites aceitáveis.
            * Caso não esteja, corrige a variável e a retorna.

        * checkLimit(self,limit):

            * Método que verifica se o limite está dentro dos limites aceitáveis.
            * Caso não esteja, corrige a variável e a retorna.

        * checkRelays(self,signal):

            * Método que verifica se o sinal está dentro dos limites aceitáveis.
            * Caso não esteja, corrige a variável e a retorna.

        * webServerMsgCheck(self,speed,steer,limit,powerA,powerB,pulverizer):

            * Método que executa todas as verificações e retorna todos os resultados.
        
        * webServerMsgSpliter(self,msg):

            * Método que recebe todas as variáveis e as separa.
            * Retorna as variáveis separadas ou 0 para todas as variáveis, caso alguma esteja errada.

        * webServerMsgHandler(self,msg):

            * Método que recebe as variáveis do commandPriorityDecider e os processa.
            * retorna as variáveis processadas ou "None", caso algum erro ocorra.