import React, { Component } from "react";
import { View, TouchableOpacity, Text } from "react-native";

import Styles from "./styles";
import Footer from "../../footer";

export default class Connection extends Component {
  state = {
    speed: 0
  };

  static navigationOptions = {
    title: "Teste de conexão",
    headerTitleStyle: {
      flexGrow: 1,
      textAlign: "center",
      alignSelf: "center"
    }
  };

  render() {
    //Envia a mensagem de controle manual para o webServerManual
    function sendToWebServerManual() {
      command =
        "http://" +
        global.serverIp +
        ":" +
        global.portManual +
        "/0*speed$" +
        0 +
        "*steer$0*limit$0*powerA$0*powerB$0*pulverize$0";
      new WebSocket(command);
    }

    return (
      <>
        <View style={Styles.container}>
          <View style={Styles.buttonTryConnectionn} />

          <View style={Styles.containerTutorial}>
            <Text style={Styles.tutorialText}>
              1 - Após ligar o robô, aguarde 2 minutos.
            </Text>
            <Text style={Styles.tutorialText}>
              2 - Clique em estabelecer conexão.
            </Text>
            <Text style={Styles.tutorialText}>
              3 - Caso o led não se acenda, aguarde 5 segundos, clique novamente
              em estabelecer conexão. Repita esse processo ate o led acender.
            </Text>
            <Text style={Styles.tutorialText}>
              4 - Com o led aceso clique em ok.
            </Text>
          </View>

          <View style={Styles.containerButtons}>
            <TouchableOpacity
              style={Styles.buttonTryConnection}
              onPress={() => {
                sendToWebServerManual();
              }}
            >
              <Text style={Styles.buttonTryText}>Estabelecer Conexão</Text>
            </TouchableOpacity>
            <View style={Styles.buttonTryConnectionn} />

            <TouchableOpacity
              style={Styles.buttonTryConnection}
              onPress={() => {
                this.props.navigation.navigate("Main");
              }}
            >
              <Text style={Styles.buttonTryText}>OK</Text>
            </TouchableOpacity>
          </View>

          <Footer />
        </View>
      </>
    );
  }
}
