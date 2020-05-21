**Descrição**

 * Programa que gerência qual comando será executado baseado na prioridade do emissor do comando.

 ---

 **Dependências**

  * rospy
  * String from std_msgs.msg
  * commandStandardizer from raspberry/modules/CommandStandardizer

---

**Classes**

 * priorities():

    * Classe que contém variáveis que definem as prioridades dos emissores de comando.

    * *Métodos*

        * __init__(self):

            * Construtor da classe.

 * Comunication():

    * Classe que gerencia a comunicação de diversos dispositivos emissores de comando com o ROS.

    * *Métodos*

        * __init__(self):

            * Construtor da classe.

        * execute(self):

            * Método que envia o comando selecionado para o robô.

        * listenXXX(self):

            * Método genérico, onde XXX é o nome do dispositivo ao qual deseja-se escutar
            * Conecta a classe Comunication ao tópico publicado pelo emissor

        * callback(self,data,priority):

            * Trata os dados recebidos pelo listenXXX e executa o comando caso ele tenha prioridade
        
        * listenCommands(self):

            * Método que executa todos os listeners declarados no código