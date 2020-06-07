**Soluções para a placa do robô apitando**

-> Verificar/Resolver os problemas na ordem indicada abaixo. As soluções estão ordenadas da mais simples para a mais complexa.

---

-> **No celular:**

    * Verifique se está conectado na rede wifi do robô por pelo menos 30 segundos.

    * Verifique se o IP de conexão com o robô está correto. O padrão é 192.168.1.2.

    * Tente enviar algum comando, por exêmplo o botão de parar, e depois tente ligar novamente a placa do robô.

---

-> **No raspberry:**

    * Verifique se o raspberry está ligado.

    * Verifique se o código do robô está rodando:

        * ao utilizar o comando 'rostopic list', o tópico control_robot deverá aparecer.

        * ao utilizar o comando 'rostopic echo /control_robot', deverão ser impressos na tela os comandos que estão sendo enviados ao robô.

    * Verifique a permissão das portas utilizadas pelos conversores TTL.

    * Verifique se os conversores TTL estão conectados nas portas corretas do raspberry. Ao conectar na porta correta, ao utilizar o comando 'ls /dev | grep tty' , o(s) nome(s) ttyUSB_conversor_0 e/ou ttyUSB_conversor_1 deverá(ão) aparecer.

    * Verifique se ao enviar comandos, os conversores TTL piscam.

    * Verifique os cabos de conexão do raspberry com os conversores TTL. Tanto se eles funcionam como se estão conectados corretamente.

---

-> **No arduino:**

    * Verifique se os arduinos piscam ao enviar comandos.

    * Resete o arduino e tente novamente.

    * Verifique se os cabos que conectam o arduino com a placa do hover board estão funcionando/conectados corretamente.

    * Conecte o arduino a um computador e utilize a IDE do arduino para visualizar o que ele está recebendo nas portas seriais ao enviar comandos pelo app.

---

-> **Na placa do hover:**

    * Verifique se as baterias possuem 39V ou mais.

    * Verifique se as baterias estão conectadas.

    * Verifique se os motores estão conectados à placa.

    * Verifique se os cabos que vêm do arduino estão conectados corretamente nos cabos dos sensores da placa.
