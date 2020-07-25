export default class Src {
    /** Tenta a comunicação com o servidor do roscore para acender o LED. */
    tryConnection() {
        command =
          "http://" + global.roscoreServerIp + ":" + global.roscoreServerPort + "/" +
          "speed$0*steer$0*limit$0*powerA$0*powerB$0*pulverize$0";
        new WebSocket(command);
      }
}