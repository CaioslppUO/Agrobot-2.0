# Files To unlock flash and flash the mainBoard for use the hoverboard hardware and control the motors:

# Commands to unlock flash and flash the mainBoard

 * To unlock or flash the MainBoard you need to install the St-Link v2  and libusb in your linux machine. 
   If you are in a windows machine use the Windows ST-Link utility. Open the terminal in the mainboard code folder (in this 
   project it's located here: https://github.com/CaioslppUO/Agrobot/tree/master/src/mainBoard) and use the following commands:

 * A) If you never flashed the mainboard before use this to unlock the flash:

   Command 1: openocd -f interface/stlink-v2.cfg -f target/stm32f1x.cfg -c init -c "reset halt" -c "stm32f1x unlock 0"

   or (if that does not work):

   Command 2: openocd -f interface/stlink-v2.cfg -f target/stm32f1x.cfg -c init -c "reset halt" -c "mww 0x40022004 0x45670123" -c "mww 0x40022004 0xCDEF89AB" -c "mww 0x40022008 0x45670123" -c "mww 0x40022008 0xCDEF89AB" -c "mww 0x40022010 0x220" -c "mww 0x40022010 0x260" -c "sleep 100" -c "mww 0x40022010 0x230" -c "mwh 0x1ffff800 0x5AA5" -c "sleep 1000" -c "mww 0x40022010 0x2220" -c "sleep 100" -c "mdw 0x40022010" -c "mdw 0x4002201c" -c "mdw 0x1ffff800" -c targets -c "halt" -c "stm32f1x unlock 0"

   or:

   Command 3: openocd -f interface/stlink-v2.cfg -f target/stm32f1x.cfg -c init -c "reset halt" -c "mww 0x40022004 0x45670123" -c "mww 0x40022004 0xCDEF89AB" -c "mww 0x40022008 0x45670123" -c "mww 0x40022008 0xCDEF89AB" -c targets -c "halt" -c "stm32f1x unlock 0"


 * B)Now you can flash the mainboard, use:

   Command 1: st-flash --reset write build/hover.bin 0x8000000

   or:

   Command 2: openocd -f interface/stlink-v2.cfg -f target/stm32f1x.cfg -c flash "write_image erase build/hover.bin 0x8000000"


# NOTE
 * To configure the input of the MainBoard you need to modify the inc/config.h.
   Just comments the current input (CONTROL_NUNCHUCK) and uncomment the input that you want.

   * Example: 
     * if you want the UART input, you need to uncomment the following line:
     
       //#define CONTROL_SERIAL_USART2       // left sensor board cable, disable if ADC or PPM is used!
       
     * and comment the follwing line:
     
       #define CONTROL_NUNCHUCK            // use nunchuck as input. disable DEBUG_SERIAL_USART3!
