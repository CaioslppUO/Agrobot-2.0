**Soluções para a placa do hover andando sozinha ao ligar**

-> Verificar/Resolver os problemas na ordem indicada abaixo. As soluções estão ordenadas da mais simples para a mais complexa.

---

-> **No raspberry:**

    * Verifique se o código do robô está rodando. Ao utilizar o comando 'rostopic echo /control_robot' deverá aparecer na tela os comandos de controle que estão sendo enviados para o robô.

    * Verificar a permissão dos conversores TTL.

    * Verificar se os conversores TTL estão conectados nas portas corretas do raspberry.

    * Verificar o nome dado aos conversores TTL.

---

-> **No conversor TTL:**
    
    * Verificar se os conversores piscam ao enviar comandos para o robô pelo app.

    * Verificar os cabos que vão do TTL para o arduino.

---

-> **No arduino:**

    * Verificar se o arduino pisca ao enviar comandos para o robô pelo app.

    * Verificar se os cabos que vão do arduino para a placa do hover.
    
    * Verificar se os arduinos não estão reiniciando por falta de energia.



    
