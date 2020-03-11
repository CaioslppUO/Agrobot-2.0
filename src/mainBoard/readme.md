# Arquivos para destravar e dar o flash da placa do Hover Board, para poder controlar a placa e os motores

---

# Comandos para destravar e dar flash na placa:
---
 * 1 - Downloads:
 
    * 1.1 - (Linux) Para destravar ou dar flash na placa, é necessários instalar o St - Link v2 e a biblioteca libusb no seu computador.
    * 1.2 - (Windows) Baixe a ferramenta ST - Link utility
---

 * 2 - Destravar e dar flash na placa:
 
    * 2.1 - Se for a primeira vez que está dando flash na placa, utilize o seguinte comando para destrava-la:
    
         Comando: openocd -f interface/stlink-v2.cfg -f target/stm32f1x.cfg -c init -c "reset halt" -c "stm32f1x unlock 0"

         Se este comando não funcionar, utilize este:

         Comando: openocd -f interface/stlink-v2.cfg -f target/stm32f1x.cfg -c init -c "reset halt" -c "mww 0x40022004 0x45670123" -c "mww 0x40022004 0xCDEF89AB" -c "mww 0x40022008 0x45670123" -c "mww 0x40022008 0xCDEF89AB" -c "mww 0x40022010 0x220" -c "mww 0x40022010 0x260" -c "sleep 100" -c "mww 0x40022010 0x230" -c "mwh 0x1ffff800 0x5AA5" -c "sleep 1000" -c "mww 0x40022010 0x2220" -c "sleep 100" -c "mdw 0x40022010" -c "mdw 0x4002201c" -c "mdw 0x1ffff800" -c targets -c "halt" -c "stm32f1x unlock 0"

         Se este comando também não funcionar, utilize este:

         Comando: openocd -f interface/stlink-v2.cfg -f target/stm32f1x.cfg -c init -c "reset halt" -c "mww 0x40022004 0x45670123" -c "mww 0x40022004 0xCDEF89AB" -c "mww 0x40022008 0x45670123" -c "mww 0x40022008 0xCDEF89AB" -c targets -c "halt" -c "stm32f1x unlock 0"


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
