# Agrobot
  * Projeto para criar um robô de multiplos propósitos baseado em Raspberry Pi 3 model B+ e Hover Boards.
  
![robo](https://github.com/CaioslppUO/Agrobot/blob/master/pictures/robot/robo1.jpg)

# Tutorial:
   
   * 1 - Setup the main Hover Board.
   
      * Follow instructions under src/mainBoard/.
      
   * 2 - Upload the code to the arduino board.
   
      * Follow instructions under src/arduino/.
   
   * 3 - Download and setup the code into raspberry pi 3 B+ (Already need to have linux. We are using Linux Mate on it
        , if you want, you can download it here: https://ubuntu-mate.org/download/).
        
        * Follow instructions under src/raspberry/.
        
   * 4 - Donwload the application to use it on your smartphone(Only tested on Android).
   
      * Follow instructions under src/AppControl/.
      * Also, you can edit the python3 script used to control the robot, and change the way to send commads.
      * If you have a nunchuck controller, you can use it to control the robot too.
      
   * 5 - Setup all the circuits needed to make it work.
   
      * Follow instructions under pictures/circuits/mainBoard , pictures/circuits/mainCircuit and
        pictures/circuits/whells/.

   * 6 - Turn arduino and raspberry on, sync raspberry and the smartphone application by typing the ip of raspberry pi in it.
   
   * 7 - Control the robot.
   
   # Referência:
   
    Git utilizado como base para o projeto: https://github.com/NiklasFauth/hoverboard-firmware-hack.
