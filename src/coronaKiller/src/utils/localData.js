import { AsyncStorage } from 'react-native'

export default class LocalData{
    // Guarda as variáveis de configuração na memória.
    async storeData  (name, value){
        try {
          await AsyncStorage.setItem(name, value);
        } catch (error) {
          alert("Erro ao salvar a variável " + name + ". " + error);
        }
    }

    // Recupera informação da memória.
    async getValue(name, defaultValue){
        result = await AsyncStorage.getItem(name);
        if (result != null && result != undefined) {
        if(name == "comunicationDelay"){
        }
          return result;
        }
        return defaultValue;
      }

    // Recupera as variáveis de configuração da memória.
    async retrieveData(){
        try {
          // Manual
          global.serverIp = String(await this.getValue("serverIp", "192.168.1.2"));
          global.portManual = String(await this.getValue("portManual", "8080"));
          global.comunicationDelay = parseInt(await this.getValue("comunicationDelay", 50));
        
          // Automático
          global.speedAuto = parseInt(await this.getValue("speedAuto", -26));
          global.steerAuto = parseInt(await this.getValue("steerAuto", -2));
          global.limitAuto = parseInt(await this.getValue("limitAuto", 50));
          global.correctionMovements = parseInt(await this.getValue("correctionMovements", 5));
          global.correctionFactor = parseInt(await this.getValue("correctionFactor", 15));
          global.moveTimeAuto = parseInt(await this.getValue("moveTimeAuto", 0));
          global.stopTimeAuto = parseInt(await this.getValue("stopTimeAuto", 0));
          global.detectDistance = parseFloat(await this.getValue("detectDistance", 1.5));
        } catch (error) {
            alert("Erro ao carregar as variáveis da memória: " + error);
        }
    }
}