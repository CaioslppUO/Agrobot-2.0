import { AsyncStorage } from "react-native";
import DefaultConfig from "../config/default";

// Classe que controla o write e read de parâmetros de configuração permanentes

// Guarda as variáveis de configuração na memória.
export async function storeData(name, value) {
  try {
    await AsyncStorage.setItem(name, value);
  } catch (error) {
    alert("Erro ao salvar a variável " + name + ". " + error);
  }
}

// Recupera informação da memória.
export async function getValue(name, defaultValue) {
  result = await AsyncStorage.getItem(name);
  if (result != null && result != undefined) {
    if (name == "communicationDelay") {
    }
    return result;
  }
  return defaultValue;
}

// Recupera as variáveis de configuração da memória.
export default async function retrieveData() {
  try {
    // Manual
    global.roscoreServerIp = String(
      await getValue("roscoreServerIp", DefaultConfig.roscoreServerIp())
    );
    global.roscoreServerPort = String(
      await getValue("roscoreServerPort", DefaultConfig.roscoreServerPort())
    );
    global.communicationDelay = parseInt(
      await getValue("communicationDelay", DefaultConfig.communicationDelay())
    );

    // Automático
    global.speedAuto = parseInt(await getValue("speedAuto", DefaultConfig.speedAuto()));
    global.steerAuto = parseInt(await getValue("steerAuto", DefaultConfig.steerAuto()));
    global.limitAuto = parseInt(await getValue("limitAuto", DefaultConfig.limitAuto()));
    global.correctionMovements = parseInt(
      await getValue("correctionMovements", DefaultConfig.correctionMovements())
    );
    global.correctionFactor = parseInt(
      await getValue("correctionFactor", DefaultConfig.correctionFactor())
    );
    global.moveTime = parseInt(await getValue("moveTime", DefaultConfig.moveTime()));
    global.stopTime = parseInt(await getValue("stopTime", DefaultConfig.stopTime()));
    global.detectDistance = parseFloat(
      await getValue("detectDistance", DefaultConfig.detectDistance())
    );
    global.sliderSensibility = parseInt(
      await getValue("sliderSensibility", DefaultConfig.sliderSensibility())
    );
  } catch (error) {
    alert("Erro ao carregar as variáveis da memória: " + error);
  }
}
