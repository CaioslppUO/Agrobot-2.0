import React, { Component } from "react";
import {
  View,
  TextInput,
  TouchableOpacity,
  Text,
  BackHandler
} from "react-native";
import Styles from "./styles";
import Footer from "../../footer";
import LocalData from '../../utils/localData'

// Classe que gerencia o carregamento e a gravação das variáveis na memória.
const localData = new LocalData()

export default class Config extends Component {
  //Variáveis da classe
  state = {
    serverIp: global.serverIp,
    port: global.portManual,
    minPSpeed: global.minPulverizeSpeed,
    delay: global.comunicationDelay,
    serverIpTemp: global.serverIp,
    portTemp: global.portManual,
    minPSpeedTemp: global.minPulverizeSpeed,
    delayTemp: global.comunicationDelay
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
        <View style={Styles.mainContainer}>
          <View />

          <View style={Styles.containerCommunication}>
            <Text style={Styles.comunication}>Comunicação</Text>
          </View>

          {/*View dos campos de preenchimento de comunicação*/}
          <View style={Styles.textInputContainer}>
            <TextInput
              style={Styles.inputText}
              placeholder={"IP do robô: " + this.state.serverIp}
              onEndEditing={text => {
                this.setState({ serverIp: text.nativeEvent.text });
              }}
              onChangeText={text => {
                this.setState({ serverIpTemp: text });
              }}
            />

            <TextInput
              style={Styles.inputText}
              placeholder={"Porta: " + this.state.port}
              onEndEditing={text => {
                this.setState({ port: text.nativeEvent.text });
              }}
              onChangeText={text => {
                this.setState({ portTemp: text });
              }}
            />

            <TextInput
              style={Styles.inputText}
              placeholder={"Tempo de resposta(ms): " + this.state.delay}
              onEndEditing={text => {
                this.setState({ delay: text.nativeEvent.text });
              }}
              onChangeText={text => {
                this.setState({ delayTemp: text });
              }}
            />
          </View>

          {/*View do botão de salvar*/}
          <View style={Styles.saveContainer}>
            <TouchableOpacity
              onPress={() => {
                global.serverIp = String(this.state.serverIpTemp);
                global.portManual = String(this.state.portTemp);
                global.comunicationDelay = parseFloat(this.state.delayTemp);

                localData.storeData("serverIp", String(this.state.serverIpTemp));
                localData.storeData("portManual", String(this.state.portTemp));
                localData.storeData("comunicationDelay", String(this.state.delayTemp));
                this.props.navigation.navigate("Main");
              }}
            >
              <Text style={Styles.saveText}>Salvar</Text>
            </TouchableOpacity>
          </View>

          <Footer />
        </View>
      </>
    );
  }
}
