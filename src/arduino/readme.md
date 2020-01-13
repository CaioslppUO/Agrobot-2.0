# Arduino code to control the agrobot:

  * This code allows arduino to receive information (Uart Communication) and transmit to Hover MainBoard (I2C Communication).
  
# Protocol to send uart to the arduino:

 * You need to send to arduino via UART(RX,TX pins), the three variables in the order: speed;steer;limit.
 * If using python3, you can send it through serial libs from raspberry to arduino.
   * Our code under src/raspberry/ use it.

 * There are three varaibles that control the mainBoard(hoverBoard):
     * Speed.
     * Steer.
     * Limit.
     
  * Speed accept values from -100 to 100.
     *    0 means stopped.
     *  100 means all power to front.
     * -100 means all power to back.
  
   * Steer accept values from -100 to 100.
     *    0 means front.
     *  100 means turn right.
     * -100 means turn left.
     
   * Limit accept values from 0 to 100.
     *   0 means no power to the wheels.
     * 100 means full power to the wheels.
 
 # Receiving values via Uart:
  
  * The procotol implemented is: ABCD;ABCD;ABCD;
 
  * Where ABCD are numbers:
    * the number A is the signal, if setted to 1 the singnal is +(Positive), else if setted 0 the signal is -(Negative).
    * BCD are the numbers that define the speed, steer and limit values, from 0 to 100.
    * Example:
         To send 80 in speed and turn full right, with limit on 100% of power: 1080;1100;1100;
