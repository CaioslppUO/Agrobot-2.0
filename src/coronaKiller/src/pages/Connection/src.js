export default class Src {
    /** Envia a mensagem de controle manual para o webServerManual */
    tryConnection() {
        command =
          "http://" + global.roscoreServerIp + ":" + global.roscoreServerPort + "/" +
          "speed$0*steer$0*limit$0*powerA$0*powerB$0*pulverize$0";
        new WebSocket(command);
      }
}