export default defaultConfig = {
    //Variáveis de controle globais.
    speed: 0,
    steer: 0,
    limit: 50,

    //Variáveis de energia(liga/desliga).
    power: 0,
    uv: 0,

    //Variáveis de comunicação.
    serverIp: "192.168.1.2",
    portManual: "8080",
    comunicationDelay: 50,
    comunicationInterval: 0,

    //Variáveis de controle automático.
    speedAuto: -26,
    steerAuto: -2,
    limitAuto: 50,
    correctionMovements: 5,
    correctionFactor: 15,

    serverIpAuto: "192.168.1.121",
    portAuto: "8082",
    moveTimeAuto: 0,
    stopTimeAuto: 0,
    detectDistance: 1.5,
}