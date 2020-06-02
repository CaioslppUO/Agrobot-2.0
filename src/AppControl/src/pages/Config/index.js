import React, { Component } from "react";
import {
  View,
  TextInput,
  TouchableOpacity,
  Text,
  BackHandler
} from "react-native";
import styles from "./styles";

export default class Config extends Component {
  //Variáveis da classe
  state = {
    serverIp: global.serverIp,
    port: global.port_manual,
    minPSpeed: global.minPulverizeSpeed,
    delay: global.comunication_delay,
    serverIp_temp: global.serverIp,
    port_temp: global.port_manual,
    minPSpeed_temp: global.minPulverizeSpeed,
    delay_temp: global.comunication_delay
  };

  //Opções do controlador de navegação de páginas
  static navigationOptions = {
    title: "Configuração",
    headerTitleStyle: {
      flexGrow: 1,
      marginLeft: "25%"
    }
  };

  componentWillMount() {
    BackHandler.addEventListener("hardwareBackPress", () => {});
  }

  componentWillUnmount() {
    BackHandler.removeEventListener("hardwareBackPress", this.backPressed);
  }

  render() {
    return (
      <>
        {/*View principal*/}
        <View style={styles.mainContainer}>
          <View style={styles.espassamento} />
          <View style={styles.containerCommunication}>
            <Text style={styles.comunication}>Comunicação</Text>
          </View>

          {/*View dos campos de preenchimento de comunicação*/}
          <View style={styles.textInputContainer}>
            <TextInput
              style={styles.textDefault}
              placeholder={"IP do robô: " + this.state.serverIp}
              onEndEditing={text => {
                this.setState({ serverIp: text.nativeEvent.text });
              }}
              onChangeText={text => {
                this.setState({ serverIp_temp: text })
              }}
            />

            <TextInput
              style={styles.textDefault}
              placeholder={"Porta: " + this.state.port}
              onEndEditing={text => {
                this.setState({ port: text.nativeEvent.text });
              }}
              onChangeText={text => {
                this.setState({ port_temp: text })
              }}
            />

            <TextInput
              style={styles.textDefault}
              placeholder={"Tempo de resposta(ms): " + this.state.delay}
              onEndEditing={text => {
                this.setState({ delay: text.nativeEvent.text });
              }}
              onChangeText={text => {
                this.setState({ delay_temp: text })
              }}
            />

            <TextInput
              style={styles.textDefault}
              placeholder={"Vel. mínima para pulv.: " + this.state.minPSpeed}
              onEndEditing={text => {
                this.setState({ minPSpeed: text.nativeEvent.text });
              }}
              onChangeText={text => {
                this.setState({ minPSpeed_temp: text })
              }}
            />
          </View>
          {/*View do botão de salvar*/}
          <View style={styles.saveContainer}>
            <TouchableOpacity
              onPress={() => {
                let lastIp = global.serverIp;
                let lastMPS = global.minPulverizeSpeed;
                global.minPulverizeSpeed = this.state.minPSpeed_temp;
                global.serverIp = this.state.serverIp_temp;
                global.port_manual = this.state.port_temp;
                global.comunication_delay = parseFloat(this.state.delay_temp);

                if (global.serverIp.split(".").length != 4) {
                  alert("Invalid IP");
                  global.serverIp = lastIp;
                }

                if (
                  global.minPulverizeSpeed < 0 ||
                  global.minPulverizeSpeed > 100
                ) {
                  alert("Invalid Min Pulverize speed");
                  global.minPulverizeSpeed = lastMPS;
                }

                this.props.navigation.navigate("Main");
              }}
            >
              <Text style={styles.saveText}>Salvar</Text>
            </TouchableOpacity>
          </View>

          {/*View da versão*/}
          <View style={styles.versionContainer}>
            <Text style={styles.versionText}>V {global.version}</Text>
          </View>
        </View>
      </>
    );
  }
}
