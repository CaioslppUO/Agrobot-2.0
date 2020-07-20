export default class Src {
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
      }

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

    // Envia o sinal para o relé ligar ou desligar.
    sendSignalToRelay(relayId) {
        if (relayId == "Power") {
          this.sendToWebServerManual(0, 0, 0, 1, global.uv);
        }
      }

    // Função que pega os valores de x e y do JoyStick e os envia para o robô.
    sendManualCommand(joystick_x, joystick_y) {
        global.speed = -Math.round(joystick_y * 100);
        global.steer = Math.round(joystick_x * 100);
        setTimeout(() => {
          this.sendToWebServerManual(
            global.speed,
            global.steer,
            global.limit,
            0,
            global.uv
          );
        }, global.comunicationDelay);
      }

    // Função que envia os valores corretos para ligar a placa do robô.
    powerButtonPressed() {
        this.sendSignalToRelay("Power");
    }

    // Função que envia os valores corretos para ligar a lâmpada UV.
    uvButtonPressed() {
        global.uv = global.uv == 0 ? 1 : 0;
        this.sendToWebServerManual(0, 0, 0, 0, global.uv);
    }

    // Função que liga/desliga o modo de controle automático.
    automaticButtonPressed(autoMode) {
        if (autoMode == 0) {
          this.sendToParamServer(
            global.limitAuto,
            global.correctionMovements,
            global.steerAuto,
            global.speedAuto,
            global.correctionFactor,
            global.moveTimeAuto,
            global.stopTimeAuto
          );
          return null;
        } else {
          this.sendToParamServer(0, 0, 0, 0, 0, 0, 0);
          return null;
        }
      }

    // Função que para o robô.
    stopRobot() {
        global.uv = 0;
        this.sendToWebServerManual(0, 0, 0, 0, 0);
        this.sendToParamServer(0, 0, 0, 0, 0, -1, -1);
    }
}