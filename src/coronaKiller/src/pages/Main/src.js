import WebServer from "../../utils/webServer"

export default class Src {
    // Envia o sinal para o relé ligar ou desligar.
    sendSignalToRelay(relayId) {
        if (relayId == "Power") {
          WebServer.sendToRoscoreServer(0, 0, 0, 1, global.uv);
        }
      }

    // Função que pega os valores de x e y do JoyStick e os envia para o robô.
    sendManualCommand(joystick_x, joystick_y) {
        global.speed = -Math.round(joystick_y * 100);
        global.steer = Math.round(joystick_x * 100);
        setTimeout(() => {
          WebServer.sendToRoscoreServer(
            global.speed,
            global.steer,
            global.limit,
            0,
            global.uv
          );
        }, global.communicationDelay);
      }

    // Função que desliga o modo automático.
    stopAutoMode(){
        WebServer.sendToLidarServer(0, 0, 0, 0, 0, 0, 0);
    }

    // Função que envia os valores corretos para ligar a placa do robô.
    powerButtonPressed() {
        this.sendSignalToRelay("Power");
    }

    // Função que envia os valores corretos para ligar a lâmpada UV.
    uvButtonPressed() {
        global.uv = global.uv == 0 ? 1 : 0;
        WebServer.sendToRoscoreServer(0, 0, 0, 0, global.uv);
    }

    // Função que liga/desliga o modo de controle automático.
    automaticButtonPressed(autoMode) {
        if (autoMode == 0) {
          WebServer.sendToLidarServer(
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
          WebServer.sendToLidarServer(0, 0, 0, 0, 0, 0, 0);
          return null;
        }
      }

    // Função que para o robô.
    stopRobot() {
        global.uv = 0;
        WebServer.sendToRoscoreServer(0, 0, 0, 0, 0);
        WebServer.sendToLidarServer(0, 0, 0, 0, 0, -1, -1);
    }
}