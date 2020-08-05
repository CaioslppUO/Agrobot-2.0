import React, { Component } from "react";
import {
  View,
  TextInput,
  TouchableOpacity,
  Text,
  BackHandler,
  Slider
} from "react-native";
import Styles from "./styles";
import Footer from "../../footer";
import LocalData from "../../utils/localData";
import Src from "./src";
import { globalStyles } from "../../styles";

// Controla o carregamento e a gravação das variáveis na memória.
const localData = new LocalData();

export default class Config extends Component {
  state = {
    serverIp: global.roscoreServerIp,
    port: global.roscoreServerPort,
    delay: global.communicationDelay,
    serverIpTemp: global.roscoreServerIp,
    portTemp: global.roscoreServerPort,
    delayTemp: global.communicationDelay,
    sliderValue: global.sliderSensibility
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
        <View style={globalStyles.mainContainer}>
          <View />

          <Text style={globalStyles.title}>Comunicação</Text>

          {/*View dos campos de preenchimento de comunicação*/}
          <View style={Styles.textInputContainer}>
            <TextInput
              style={globalStyles.inputText}
              placeholder={"IP do robô: " + this.state.serverIp}
              onEndEditing={text => {
                this.setState({ serverIp: text.nativeEvent.text });
              }}
              onChangeText={text => {
                this.setState({ serverIpTemp: text });
              }}
            />
            <TextInput
              style={globalStyles.inputText}
              placeholder={"Porta: " + this.state.port}
              onEndEditing={text => {
                this.setState({ port: text.nativeEvent.text });
              }}
              onChangeText={text => {
                this.setState({ portTemp: text });
              }}
            />
            <TextInput
              style={globalStyles.inputText}
              placeholder={"Tempo de resposta(ms): " + this.state.delay}
              onEndEditing={text => {
                this.setState({ delay: text.nativeEvent.text });
              }}
              onChangeText={text => {
                this.setState({ delayTemp: text });
              }}
            />
          </View>

          <View style={Styles.sliderContainer}>
            <Slider
              maximumValue={100}
              minimumValue={0}
              value={this.state.sliderValue}
              onValueChange={sliderValue => {
                this.setState({ sliderValue });
              }}
              style={Styles.slider}
              step={1}
            />
            <View>
              <Text style={Styles.textSlider}>
                Sensibilidade joystick {this.state.sliderValue}%{" "}
              </Text>
            </View>
          </View>

          <View style={Styles.containerButtons}>
            <TouchableOpacity
              style={globalStyles.button}
              onPress={() => {
                try {
                  Src.checkIp(this.state.serverIpTemp);
                  Src.checkPort(this.state.portTemp);
                  Src.checkDelay(this.state.delayTemp);

                  global.roscoreServerIp = String(this.state.serverIpTemp);
                  global.roscoreServerPort = String(this.state.portTemp);
                  global.communicationDelay = parseFloat(this.state.delayTemp);
                  global.sliderSensibility = parseInt(this.state.sliderValue);

                  localData.storeData(
                    "roscoreServerIp",
                    String(this.state.serverIpTemp)
                  );
                  localData.storeData(
                    "roscoreServerPort",
                    String(this.state.portTemp)
                  );
                  localData.storeData(
                    "communicationDelay",
                    String(this.state.delayTemp)
                  );
                  localData.storeData(
                    "sliderSensibility",
                    String(this.state.sliderValue)
                  );
                  this.props.navigation.navigate("Main");
                } catch (err) {
                  alert(err);
                }
              }}
            >
              <Text style={globalStyles.textButtons}>Salvar</Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={globalStyles.button}
              onPress={() => {
                Src.buttonResetPressed();
                this.props.navigation.navigate("Main");
              }}
            >
              <Text style={globalStyles.textButtons}>Redefinir</Text>
            </TouchableOpacity>
          </View>

          <Footer />
        </View>
      </>
    );
  }
}
