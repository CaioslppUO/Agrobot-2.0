import WebServer from '../../utils/webServer';

export default function Src() {
  /** Envia o sinal para o relé ligar ou desligar. */
  function sendSignalToRelay(relayId) {
    if (relayId == 'Power') {
      WebServer.sendToRoscoreServer(0, 0, 0, 1, global.uv);
    }
  }

  /** Pega os valores de x e y do JoyStick e os envia para o robô. */
  function sendManualCommand(joystick_x, joystick_y, sliderSensibility) {
    global.speed = -Math.round(joystick_y * sliderSensibility);
    global.steer = Math.round(joystick_x * sliderSensibility);
    setTimeout(() => {
      WebServer.sendToRoscoreServer(
        global.speed,
        global.steer,
        global.limit,
        0,
        global.uv,
      );
    }, global.communicationDelay);
  }

  /** Desliga o modo automático. */
  function stopAutoMode() {
    WebServer.sendToLidarServer(0, 0, 0, 0, 0, 0, 0);
  }

  /** Envia os valores corretos para ligar a placa do robô. */
  function powerButtonPressed() {
    this.sendSignalToRelay('Power');
  }

  /** Envia os valores corretos para ligar a lâmpada UV. */
  function uvButtonPressed() {
    global.uv = global.uv == 0 ? 1 : 0;
    WebServer.sendToRoscoreServer(0, 0, 0, 0, global.uv);
  }

  /** Liga/desliga o modo de controle automático. */
  function automaticButtonPressed(autoMode) {
    if (autoMode === 0) {
      WebServer.sendToLidarServer(
        global.limitAuto,
        global.correctionMovements,
        global.steerAuto,
        global.speedAuto,
        global.correctionFactor,
        global.moveTimeAuto,
        global.stopTimeAuto,
      );
      return null;
    } else {
      WebServer.sendToLidarServer(0, 0, 0, 0, 0, 0, 0);
      this.stopRobot();
      return null;
    }
  }

  /** Para o robô. */
  function stopRobot() {
    global.uv = 0;
    WebServer.sendToRoscoreServer(0, 0, 0, 0, 0);
    WebServer.sendToLidarServer(0, 0, 0, 0, 0, -1, -1);
  }
}
