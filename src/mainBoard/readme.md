# Arquivos para destravar e dar o flash da placa do Hover Board, para poder controlar a placa e os motores

---

# Comandos para destravar e dar flash na placa:
---
 * 1 - Downloads:
 
    * 1.1 - (Linux) Para destravar ou dar flash na placa, é necessários instalar o St - Link v2 e a biblioteca libusb no seu computador.
    * 1.2 - (Windows) Baixe a ferramenta ST - Link utility
---

 * 2 - Destravar e dar flash na placa: (Linux)
 
    * 2.1 - Abra um terminal e entre na pasta mainBoard.
 
    * 2.2 - Se for a primeira vez que está dando flash na placa, utilize o seguinte comando para destrava-la:
    
         Comando: openocd -f interface/stlink-v2.cfg -f target/stm32f1x.cfg -c init -c "reset halt" -c "stm32f1x unlock 0"

         Se este comando não funcionar, utilize este:

         Comando: openocd -f interface/stlink-v2.cfg -f target/stm32f1x.cfg -c init -c "reset halt" -c "mww 0x40022004 0x45670123" -c "mww 0x40022004 0xCDEF89AB" -c "mww 0x40022008 0x45670123" -c "mww 0x40022008 0xCDEF89AB" -c "mww 0x40022010 0x220" -c "mww 0x40022010 0x260" -c "sleep 100" -c "mww 0x40022010 0x230" -c "mwh 0x1ffff800 0x5AA5" -c "sleep 1000" -c "mww 0x40022010 0x2220" -c "sleep 100" -c "mdw 0x40022010" -c "mdw 0x4002201c" -c "mdw 0x1ffff800" -c targets -c "halt" -c "stm32f1x unlock 0"

         Se este comando também não funcionar, utilize este:

         Comando: openocd -f interface/stlink-v2.cfg -f target/stm32f1x.cfg -c init -c "reset halt" -c "mww 0x40022004 0x45670123" -c "mww 0x40022004 0xCDEF89AB" -c "mww 0x40022008 0x45670123" -c "mww 0x40022008 0xCDEF89AB" -c targets -c "halt" -c "stm32f1x unlock 0"

    * 2.3 - Dar flash na placa:
         
         Comando: st-flash --reset write build/hover.bin 0x8000000

         Se este comando não funcionar, utilize este:

         Comando: openocd -f interface/stlink-v2.cfg -f target/stm32f1x.cfg -c flash "write_image erase build/hover.bin 0x8000000"

---

# Observações
 
 * Para configurar o tipo de entrada(Para controlar os motores) que a placa irá receber, altere o arquivo inv/config.h. Apenas comente o input atual (CONTROL_NUNCHUCK) e descomente o input que você irá utilizar.

   * Exemplo: 
     * Se quiser utilizar UART, é necessário descomentar a seguinte linha:
     
       //#define CONTROL_SERIAL_USART2       // left sensor board cable, disable if ADC or PPM is used!
       
     * E comentar a seguinte linha:
     
       #define CONTROL_NUNCHUCK            // use nunchuck as input. disable DEBUG_SERIAL_USART3!
