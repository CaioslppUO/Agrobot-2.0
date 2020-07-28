/** Classe que controla a comunicação com os servidores no raspberry. */
export default WebServer = {
  /**  Envia a mensagem de controle para o servidor do roscore. */
  sendToRoscoreServer(speed, steer, limit, power, uv) {
    command =
      "http://" + global.roscoreServerIp + ":" + global.roscoreServerPort +
      "/" +
      "0*speed$" + speed + "*" +
      "steer$" + steer + "*" +
      "limit$" + limit + "*" +
      "powerA$" + power + "*" +
      "powerB$" + 0 + "*" +
      "pulverize$" + uv;
    new WebSocket(command);
  },
  /**  Envia a mensagem de controle para o servidor do lidar. */
  sendToLidarServer(
    limit,
    tickDefault,
    steerDefault,
    speedDefault,
    shiftDirection,
    moveTimeAuto,
    stopTimeAuto
  ) {
    command =
      "http://" + global.lidarServerIp + ":" + global.lidarServerPort +
      "/" +
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
