import { Alert } from "react-native"

import LocalData from "../../utils/localData"

// Classe que gerencia o carregamento e a gravação das variáveis na memória.
const localData = new LocalData()

export default Src = {
    checkLimitAuto: function(limit){
        if(typeof parseInt(limit) != "number" || Number.isNaN(parseInt(limit))){
            throw new Error("Limite inválido.")
        }
        if(parseInt(limit) > 100 || parseInt(limit) < 0){
            throw new Error("Limite inválido.")
        }
    },
    checkCorrectionMovements: function(corrections){
        if(typeof parseInt(corrections) != "number" || Number.isNaN(parseInt(corrections))){
            throw new Error("N° de movimentos de correção inválido.")
        }
        if(parseInt(corrections) < 0){
            throw new Error("N° de movimentos de correção inválido.")
        }
    },
    checkSteerAuto: function(steer){
        if(typeof parseInt(steer) != "number" || Number.isNaN(parseInt(steer))){
            throw new Error("Direção inválida.")
        }

        if(parseInt(steer) > 100 || parseInt(steer) < -100){
            throw new Error("Direção inválida.")
        }
    },
    checkSpeedAuto: function(speed){
        if(typeof parseInt(speed) != "number" || Number.isNaN(parseInt(speed))){
            throw new Error("Velocidade inválida.")
        }

        if(parseInt(speed) > 100 | parseInt(speed) < -100){
            throw new Error("Velocidade inválida.")
        }
    },
    checkCorrectionFactor: function(correctionFactor){
        if(typeof parseFloat(correctionFactor) != "number" || Number.isNaN(parseInt(correctionFactor))){
            throw new Error("Fator de correção inválido.")
        }

        if(parseFloat(correctionFactor) < 0){
            throw new Error("Fator de correção inválido.")
        }
    },
    checkMoveTimeAuto: function(moveTime){
        if(typeof parseInt(moveTime) != "number" || Number.isNaN(parseInt(moveTime))){
            throw new Error("Andar por inválido.")
        }
        if(parseInt(moveTime) < 0 || parseInt(moveTime) > 10800){ //Evita números negativos ou superiores a 3 horas.
            throw new Error("Andar por inválido.")
        }
    },
    checkStopTimeAuto: function(stopTime){
        if(typeof parseInt(stopTime) != "number" || Number.isNaN(parseInt(stopTime))){
            throw new Error("Parar por inválido.")
        }

        if(parseInt(stopTime) < 0 || parseInt(stopTime) > 10800){ //Evita números negativos ou superiores a 3 horas.
            throw new Error("Parar por inválido.")
        }
    },
    checkDetectDistance: function(detectDistance){
        if(typeof parseFloat(detectDistance) != "number" || Number.isNaN(parseInt(detectDistance))){
            throw new Error("Distância de colisão inválida.")
        }

        if(parseFloat(detectDistance) < 0 || parseFloat(detectDistance) > 11.9){
            throw new Error("Distância de colisão inválida.")
        }
    },
    buttonResetPressed: function(){
        const title = "Resetar configurações"
        const message = "Tem certeza que deseja resetar as configurações?"
        const buttons = [
            { text:"Sim", onPress: () => {
                global.lidarServerIp = DefaultConfig.lidarServerIp();
                global.lidarServerPort = DefaultConfig.lidarServerPort();

                global.speedAuto = DefaultConfig.speedAuto();
                global.steerAuto = DefaultConfig.steerAuto();
                global.limitAuto = DefaultConfig.limitAuto();

                global.correctionMovements = DefaultConfig.correctionMovements();
                global.correctionFactor = DefaultConfig.correctionFactor();

                global.moveTime = DefaultConfig.moveTime();
                global.stopTime = DefaultConfig.stopTime();
                global.detectDistance = DefaultConfig.detectDistance();

                localData.storeData("limitAuto", String(limitAuto));
                localData.storeData(
                  "correctionMovements",
                  String(correctionMovements)
                );
                localData.storeData("steerAuto", String(steerAuto));
                localData.storeData("speedAuto", String(speedAuto));
                localData.storeData(
                  "correctionFactor",
                  String(correctionFactor)
                );
                localData.storeData("moveTime", String(moveTime));
                localData.storeData("stopTime", String(stopTime));
                localData.storeData("detectDistance", String(detectDistance));
                alert("Redefinição concluída.")
            } },
            { text:"Não", onPress: () => alert("Redefinição cancelada.") }
        ]
        Alert.alert(title,message,buttons)
    }
}