import { AsyncStorage } from "react-native";
import LocalData from "../utils/localData"
import DefaultConfig from "./default"

// Classe que gerencia o carregamento e a gravação das variáveis na memória.
const localData = new LocalData()

//Variáveis de controle globais.
global.speed = DefaultConfig.speed;
global.steer = DefaultConfig.steer;
global.limit = DefaultConfig.limit;

//Variáveis de energia(liga/desliga).
global.power = DefaultConfig.power;
global.uv = DefaultConfig.uv;

//Variáveis de comunicação.
global.serverIp = DefaultConfig.serverIp;
global.portManual = DefaultConfig.portManual;
global.comunicationDelay = DefaultConfig.comunicationDelay;
global.comunicationInterval = DefaultConfig.comunicationInterval;

//Variáveis de controle automático.
global.speedAuto = DefaultConfig.speedAuto;
global.steerAuto = DefaultConfig.steerAuto;
global.limitAuto = DefaultConfig.limitAuto;
global.correctionMovements = DefaultConfig.correctionMovements;
global.correctionFactor = DefaultConfig.correctionFactor;

global.serverIpAuto = DefaultConfig.serverIpAuto;
global.portAuto = DefaultConfig.portAuto;
global.moveTimeAuto = DefaultConfig.moveTimeAuto;
global.stopTimeAuto = DefaultConfig.stopTimeAuto;
global.detectDistance = DefaultConfig.detectDistance;

//Variáveis de informação.
global.version = "0.7.5";

// Recuperando as variáveis previamente guardadas.
localData.retrieveData();
