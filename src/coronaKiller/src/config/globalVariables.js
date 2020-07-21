import { AsyncStorage } from "react-native";
import LocalData from "../utils/localData"

// Classe que gerencia o carregamento e a gravação das variáveis na memória.
const localData = new LocalData()

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
global.version = "0.7.0";

// Recuperando as variáveis previamente guardadas.
localData.retrieveData();
