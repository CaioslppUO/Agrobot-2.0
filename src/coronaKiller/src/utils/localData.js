import { AsyncStorage } from 'react-native'
import DefaultConfig from "../config/default"

/** Classe que controla o write e read de parâmetros de configuração permanentes
  . */
export default class LocalData{
    /** Guarda as variáveis de configuração na memória. */
    async storeData  (name, value){
        try {
          await AsyncStorage.setItem(name, value);
        } catch (error) {
          alert("Erro ao salvar a variável " + name + ". " + error);
        }
    }

    /** Recupera informação da memória. */
    async getValue(name, defaultValue){
        result = await AsyncStorage.getItem(name);
        if (result != null && result != undefined) {
        if(name == "communicationDelay"){
        }
          return result;
        }
        return defaultValue;
      }

    /** Recupera as variáveis de configuração da memória. */
    async retrieveData(){
        try {
          // Manual
          global.roscoreServerIp = String(await this.getValue("roscoreServerIp",
            DefaultConfig.roscoreServerIp()));
          global.roscoreServerPort = String(await this.getValue("roscoreServerPort",
            DefaultConfig.roscoreServerPort()));
          global.communicationDelay = parseInt(
            await this.getValue("communicationDelay",
            DefaultConfig.communicationDelay()));
        
          // Automático
          global.speedAuto = parseInt(await this.getValue("speedAuto",
           DefaultConfig.speedAuto()));
          global.steerAuto = parseInt(await this.getValue("steerAuto",
           DefaultConfig.steerAuto()));
          global.limitAuto = parseInt(await this.getValue("limitAuto",
           DefaultConfig.limitAuto()));
          global.correctionMovements = parseInt(
            await this.getValue("correctionMovements",
             DefaultConfig.correctionMovements()));
          global.correctionFactor = parseInt(
            await this.getValue("correctionFactor",
             DefaultConfig.correctionFactor()));
          global.moveTime = parseInt(await this.getValue("moveTime",
           DefaultConfig.moveTime()));
          global.stopTime = parseInt(await this.getValue("stopTime",
           DefaultConfig.stopTime()));
          global.detectDistance = parseFloat(
            await this.getValue("detectDistance",
             DefaultConfig.detectDistance()));
        } catch (error) {
            alert("Erro ao carregar as variáveis da memória: " + error);
        }
    }
}