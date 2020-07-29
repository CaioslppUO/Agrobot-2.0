export default class Src {
  /** Tenta a comunicação com o servidor do roscore para acender o LED. */
  tryConnection() {
    for (let i = 0; i < 10; i++) {
      command =
        "http://" + global.roscoreServerIp + ":" + global.roscoreServerPort + "/" +
        "0*speed$" + (i % 2 === 0 ? 0 : 1) +
        "*steer$0*limit$0*powerA$0*powerB$0*pulverize$0";
      new WebSocket(command);
    }
  }
}
