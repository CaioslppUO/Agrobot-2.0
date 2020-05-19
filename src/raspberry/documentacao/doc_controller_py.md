**Descrição**

* Programa que gerência o launch do ROS e de todos os módulos que serão utilizados

---

**Dependências**
 
 * os
 * sys
 * rospy
 * time
 * String from std_msgs.msg
 * launcherVariables from raspberry/LauncherVariables

---

**Parâmetros de execução do arquivo**

 * serverIp: Ip do WebServer no qual irá rodar o roscore(ROS_MASTER_URI)
 * enableUart: Boolean para definir se a comunicação UART vai ou não estar habilitada
 * enableSensor: Boolean para definir se os sensores vão ou não estar habilitados
 * enableRelay: Boolean para definir se os relés vão ou não estar habilitados
 * uartAmount: Quantidade de UART's que serão utilizados(Nº de placas de hover boards)
 * enableFaceDetect: Boolean para definir se o controle automático por meio de câmeras será ou não habilitado
 * rootPath: Caminho completo até a raiz do código fonte. Ex: /home/USER/Agrobor-2.0/src/raspberry/

---

 **Variáveis Globais**

 * pubController: Variável que controla o publisher no Tópico 'Controller' do ROS

 ---

**Funções**

 * mainLoop():

    * Função que Recebe todos os parâmetros passados com a execução do arquivo, os processa e ajusta quais módulos serão e quais não serão executados.