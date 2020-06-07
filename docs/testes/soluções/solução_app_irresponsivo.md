**Soluções para o app irresponsivo**
---

    -> Verificar/Resolver os problemas na ordem indicada abaixo. As soluções estão ordenadas da mais simples para a mais complexa.

-> **No app/celular:**
    
    * Verificar se está conectado na rede wifi gerada pelo robô. Após conectar na rede é necessário aguardar alguns segundos.
        
    * Verificar se o IP de conexão com o robô está correto. O padrão é 192.168.1.2.

    * Verificar se as variáveis de configuração do robô estão sendo salvas. Salve, volte para a página principal e volte à tela de configuração novamente. Caso esteja funcionando, o valor deverá ser o último que você alterou.

    * Verificar se a distância do celular para o raspberry não é superior a 30 metros. Acima dessa distância não é garantido que a conexão funcione. 

-> **No raspberry:**

    * O raspberry está desligado.

    * O programa do robô não está rodando. Verificar utilizando o comando rostopic list, deverá aparecer um tópico com nome web_server.

    * As variáveis de ambiente do ROS estão erradas.

    * Verificar o status do serviço que inicializa o programa, nele é possível ver um log de erros, caso ocorram. Comando: sudo systemctl status autoStartRobotCore.

    * Verificar o arquivo de logs do programa localizado na pasta: raspberry/logs/errors.log.
