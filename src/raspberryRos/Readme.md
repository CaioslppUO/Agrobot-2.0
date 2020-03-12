# Código fonte do Raspberry que faz a comunicação com os Arduinos e com o App:
 
  * Para rodar o código, utilize os scrips na pasta runnables.
 
---

# Lógica de funcionamento do código:
  
  * O código do Raspberry é baseado no ROS(Robot Operating System), e está dividido em camadas para facilitar a implementação de novos componentes, visando a total modularidade do código.
  
  * As camadas são 3: 
  
        1 - Recepção de comandos por quaisquer meios.
-
        2 - Montagem dos comandos de uma forma que o robô entenda.
-
        3 - Envio dos comandos recebidos para as devidas partes e dispositivos.
-
