export default WebServer = {
    // Envia a mensagem de controle manual para o webServerManual.
    sendToWebServerManual(speed, steer, limit, power, uv) {
        command =
          "http://" + global.serverIp + ":" +global.portManual + "/" +
          "speed$" + speed + "*" +
          "steer$" + steer + "*" +
          "limit$" + limit + "*" +
          "powerA$" + power + "*" +
          "powerB$" + 0 + "*" +
          "pulverize$" + uv;
        new WebSocket(command);
      },
    // Envia a mensagem de controle automático para o webserver de parâmetros.
    sendToParamServer(
        limit,
        tickDefault,
        steerDefault,
        speedDefault,
        shiftDirection,
        moveTimeAuto,
        stopTimeAuto
      ) {
        command =
          "http://" + global.serverIpAuto + ":" + global.portAuto + "/" +
          "limit$" + limit + "*" +
          "tick$" + tickDefault + "*" +
          "steer$" + steerDefault + "*" +
          "speed$" + speedDefault + "*" +
          "shift$" + shiftDirection + "*" +
          "uv$" + global.uv + "*" +
          "detect$" + global.detectDistance + "*" +
          "move$" + moveTimeAuto + "*" +
          "stop$" + stopTimeAuto;
        new WebSocket(command);
      }
}