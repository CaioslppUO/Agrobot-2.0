export default class Src {
    //Envia a mensagem de controle manual para o webServerManual
    sendToWebServerManual() {
        command =
          "http://" + global.serverIp + ":" + global.portManual + "/" +
          "speed$0*steer$0*limit$0*powerA$0*powerB$0*pulverize$0";
        new WebSocket(command);
      }
}