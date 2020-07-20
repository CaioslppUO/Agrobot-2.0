import { AsyncStorage } from "react-native";

//Variáveis de controle globais.
global.speed = 0;
global.steer = 0;
global.limit = 50;

//Variáveis de energia(liga/desliga).
global.power = 0;
global.uv = 0;

//Variáveis de comunicação.
global.serverIp = "192.168.1.2";
global.portManual = "8080";
global.comunicationDelay = 50;
global.comunicationInterval = 0;

//Variáveis de controle automático.
global.speedAuto = -26;
global.steerAuto = -2;
global.limitAuto = 50;
global.correctionMovements = 5;
global.correctionFactor = 15;

global.serverIpAuto = "192.168.1.121";
global.portAuto = "8082";
global.moveTimeAuto = 0;
global.stopTimeAuto = 0;
global.detectDistance = 1.5;

//Variáveis de informação.
global.version = "0.6.3";

async function setValue(name, defaultValue) {
  result = await AsyncStorage.getItem(name);
  if (result != null) {
    return result;
  }
  return defaultValue;
}

// Recupera as variáveis.
retrieveData = async () => {
  try {
    // Manual
    global.serverIp = await setValue("serverIp", "192.168.1.2");
    global.portManual = await setValue("portManual", "8080");
    global.comunicationDelay = parseInt(
      await setValue("comunicationDelay", "50")
    );

    // Automático
    global.speedAuto = await setValue("speedAuto", "-26");
    global.steerAuto = await setValue("steerAuto", "-2");
    global.limitAuto = await setValue("limitAuto", "50");
    global.correctionMovements = await setValue("correctionMovements", "5");
    global.correctionFactor = await setValue("correctionFactor", "15");
    global.moveTimeAuto = await setValue("moveTimeAuto", "0");
    global.stopTimeAuto = await setValue("stopTimeAuto", "0");
    global.detectDistance = await setValue("detectDistance", "1.5");
  } catch (error) {}
};

// Recuperando as variáveis previamente guardadas.
retrieveData();
