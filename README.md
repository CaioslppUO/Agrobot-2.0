# Agrobot
  * This is a project to make a agriculture robot, using raspberry pi 3 model B+ and hoverBoard.
  
![robo](https://github.com/CaioslppUO/Agrobot/blob/master/pictures/robot/robo1.jpg)

# Material needed to do:
   
   Here we put a list to assemble the circuit in the simplest way, 
     with only 2 wheels and a main board(it also can be done with only 1 wheel):
     
     * 1 raspberry pi 3 model B+ (With linux installed)
     * 1 memory card for the raspberry.
     * 1 arduino(We have tested with nano and uno r3.You need 1 arduino to each mainBoard, 
       if want to have more than 1 in the project).
     * 1 ft232r USB -> UART, for each arduino you are using.
     * 1 mainBoard, removed from the hoverBoard.
     * 2 Or 1 wheel(s), depending on what you want, removed from the hoverBoard.
     * A couple of wires to connect the circuit.

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
   
   # References:
   
    On the part of hacking the main board and submitting the codes for it, 
    we rely on this github: https://github.com/NiklasFauth/hoverboard-firmware-hack.
