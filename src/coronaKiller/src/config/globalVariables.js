import LocalData from "../utils/localData"
import DefaultConfig from "./default"

// Controla o carregamento e a gravação das variáveis na memória.
const localData = new LocalData()

// Variáveis de controle globais.
global.speed = DefaultConfig.speed();
global.steer = DefaultConfig.steer();
global.limit = DefaultConfig.limit();

// Variáveis de energia(liga/desliga).
global.power = DefaultConfig.power();
global.uv = DefaultConfig.uv();

// Variáveis de conexão.
global.roscoreServerIp = DefaultConfig.roscoreServerIp();
global.lidarServerIp = DefaultConfig.lidarServerIp();
global.roscoreServerPort = DefaultConfig.roscoreServerPort();
global.lidarServerPort = DefaultConfig.lidarServerPort();

// Variáveis de controle de comunicação.
global.communicationDelay = DefaultConfig.communicationDelay();
global.communicationInterval = DefaultConfig.communicationInterval();

//Variáveis de controle automático.
global.speedAuto = DefaultConfig.speedAuto();
global.steerAuto = DefaultConfig.steerAuto();
global.limitAuto = DefaultConfig.limitAuto();

global.correctionMovements = DefaultConfig.correctionMovements();
global.correctionFactor = DefaultConfig.correctionFactor();

global.moveTime = DefaultConfig.moveTime();
global.stopTime = DefaultConfig.stopTime();
global.detectDistance = DefaultConfig.detectDistance();

//Variáveis de informação.
global.version = "0.7.9";

// Recuperando as variáveis previamente guardadas.
localData.retrieveData();
