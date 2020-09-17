import { AsyncStorage } from "react-native";

//Variáveis de controle globais
global.speed = 0;
global.steer = 0;
global.limit = 50;

//Variáveis de energia(liga/desliga)
global.power = 0;
global.uv = 0;

//Variáveis de comunicação
global.serverIp = "192.168.1.2";
global.port_manual = "8080";
global.comunication_delay = 50;
global.comunication_interval = 0;

global.props = 0;

//Variáveis de controle automático
global.speed_auto = -26;
global.steer_auto = -2;
global.limit_auto = 50;
global.correction_movements = 5;
global.correction_factor = 15;

global.serverIp_auto = "192.168.1.125";
global.port_auto = "8082";
global.move_time_auto = 0;
global.stop_time_auto = 0;
global.detect_distance = 1.5;

//Variáveis de informação
global.version = "0.6.2";

async function setValue(name, default_value) {
  res = await AsyncStorage.getItem(name);
  if (res != null) {
    return res;
  }
  return default_value;
}

// Recupera as variáveis
retrieveData = async () => {
  try {
    // Manual
    global.serverIp = await setValue("serverIp", "192.168.1.2");
    global.port_manual = await setValue("port_manual", "8080");
    global.comunication_delay = parseInt(
      await setValue("comunication_delay", "50")
    );

    // Automático
    global.speed_auto = await setValue("speed_auto", "-26");
    global.steer_auto = await setValue("steer_auto", "-2");
    global.limit_auto = await setValue("limit_auto", "50");
    global.correction_movements = await setValue("correction_movements", "5");
    global.correction_factor = await setValue("correction_factor", "15");
    global.move_time_auto = await setValue("move_time_auto", "0");
    global.stop_time_auto = await setValue("stop_time_auto", "0");
    global.detect_distance = await setValue("detect_distance", "1.5");
  } catch (error) {}
};

// Recuperando as variáveis
retrieveData();
