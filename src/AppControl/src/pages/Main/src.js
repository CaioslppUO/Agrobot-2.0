import WebServer from "../../utils/webServer"

export default class Src {
    /** Envia o sinal para o relé ligar ou desligar. */
    sendSignalToRelay(relayId) {
        if (relayId == "Power") {
          WebServer.sendToRoscoreServer(0, 0, 0, 1, global.uv);
        }
      }

    /** Pega os valores de x e y do JoyStick e os envia para o robô. */
    sendManualCommand(joystick_x, joystick_y, sliderSensibility) {
        global.speed = -Math.round(joystick_y * sliderSensibility);
        global.steer = Math.round(joystick_x * sliderSensibility);
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

    /** Desliga o modo automático. */
    stopAutoMode(){
        WebServer.sendToLidarServer(0, 0, 0, 0, 0, 0, 0);
    }

    /** Envia os valores corretos para ligar a placa do robô. */
    powerButtonPressed() {
        this.sendSignalToRelay("Power");
    }

    /** Envia os valores corretos para ligar a lâmpada UV. */
    uvButtonPressed() {
        global.uv = global.uv == 0 ? 1 : 0;
        WebServer.sendToRoscoreServer(0, 0, 0, 0, global.uv);
    }

    /** Liga/desliga o modo de controle automático. */
    automaticButtonPressed(autoMode) {
        if (autoMode === 0) {
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
          this.stopRobot()
          return null;
        }
      }

    /** Para o robô. */
    stopRobot() {
        global.uv = 0;
        WebServer.sendToRoscoreServer(0, 0, 0, 0, 0);
        WebServer.sendToLidarServer(0, 0, 0, 0, 0, -1, -1);
    }
}