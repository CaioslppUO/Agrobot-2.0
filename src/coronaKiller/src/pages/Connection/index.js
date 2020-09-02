import React, { Component } from "react";
import { View, TouchableOpacity, Text, Image } from "react-native";

import NavigationActions from "react-navigation/src/NavigationActions";
import styles from "./styles";

const LabiotImg = require("../../resources/labiot.png");
const ptiImg = require("../../resources/pti.png");
const unioesteImg = require("../../resources/unioeste.png");
const itaipuImg = require("../../resources/Itaipu.png");
const hmcc = require("../../resources/hmcc.jpeg");
const municipal = require("../../resources/municipal.png");
const receitaFederal = require("../../resources/receitaFederal.png");

export default class Connection extends Component {
  state = {
    speed: 0
  };
  static navigationOptions = {
    title: "Teste de conexão",
    // alignContent: "center",
    headerTitleStyle: {
      flexGrow: 1,
      // fontSize: 18,
      textAlign: "center",
      alignSelf: "center"
    }
  };

  render() {
    //Envia a mensagem de controle manual para o webServerManual
    function sendToWebServerManual() {
      speed = 0
      for(i = 0; i<10; i++){
        if(speed === 0){
          speed = 1
        }else{
          speed = 0
        }
        command =
        "http://" +
        global.serverIp +
        ":" +
        global.port_manual +
        "/0*speed$" +
        speed +
        "*steer$0*limit$0*powerA$0*powerB$0*pulverize$0";
        new WebSocket(command);
      }
    }
    return (
      <>
        <View style={styles.container}>
          <View style={styles.buttonTryConnectionn} />
          <View style={styles.containerTutorial}>
            <Text style={styles.textTutorial}>
              1 - Após ligar o robô, aguarde 2 minutos.
            </Text>
            <Text style={styles.textTutorial}>
              2 - Clique em estabelecer conexão.
            </Text>
            <Text style={styles.textTutorial}>
              3 - Caso o led não se acenda, aguarde 5 segundos, clique novamente
              em estabelecer conexão. Repita esse processo ate o led acender.
            </Text>
            <Text style={styles.textTutorial}>
              4 - Com o led aceso clique em ok.
            </Text>
          </View>

          <View style={styles.containerButtons}>
            <TouchableOpacity
              style={styles.buttonTryConnection}
              onPress={() => {
                sendToWebServerManual();
              }}
            >
              <Text style={styles.buttonTryText}>Estabelecer Conexão</Text>
            </TouchableOpacity>
            <View style={styles.buttonTryConnectionn} />

            <TouchableOpacity
              style={styles.buttonTryConnection}
              onPress={() => {
                this.props.navigation.navigate("Main");
              }}
            >
              <Text style={styles.buttonTryText}>OK</Text>
            </TouchableOpacity>
          </View>

          {/* View de logo e versão */}
          <View style={styles.containerLogoVersion}>
            {/* View das logos */}
            <View style={styles.logosView}>
              <Image style={styles.logoReceita} source={receitaFederal} />
              <Image style={styles.logoMunicipal} source={municipal} />
              <Image style={styles.logoHmcc} source={hmcc} />
            </View>
            <View style={styles.logosView}>
              <Image style={styles.logoLabiot} source={LabiotImg} />
              <Image style={styles.logoUnioeste} source={unioesteImg} />
              <Image style={styles.logoPti} source={ptiImg} />
              <Image style={styles.logoItaipu} source={itaipuImg} />
            </View>
            {/*View da versão*/}
            <View>
              <Text style={styles.versionText}>V {global.version}</Text>
            </View>
          </View>
        </View>
      </>
    );
  }
}
