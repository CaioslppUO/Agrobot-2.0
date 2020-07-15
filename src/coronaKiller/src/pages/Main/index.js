import React, { Component, useState } from "react";
import { View,TouchableOpacity,Text,Slider,Image,Picker,Dimensions
} from "react-native";

import AxisPad from "react-native-axis-pad";
import NavigationActions from "react-navigation/src/NavigationActions";
import Styles from "./styles";
import Icon from "react-native-vector-icons/FontAwesome";

/**
 * Constantes de imagens
 */

const constLabiotImg = require("../../resources/labiot.png");
const constPtiImg = require("../../resources/pti.png");
const constUnioesteImg = require("../../resources/unioeste.png");
const constItaipuImg = require("../../resources/Itaipu.png");

/*
 * Página principal
 */
export default class Main extends Component {
  //Variáveis globais da classe
  state = {
    limitSliderValue: 50,
    buttonPowerColor: "#f00",
    buttonUvColor: "#000",
    buttonAutoColor: "#000",
    autoMode: 0,
    menuItem: 0,
    menuItemValue: 0
  };

  //Opções do controlador de navegação de páginas
  static navigationOptions = {
    title: "Controle",
    headerTitleStyle: {
      textAlign: "center",
      alignSelf: "center",
      flexGrow: 1
    }
  };

  componentWillMount(){
    this.props.navigation.navigate("Connection");
  }

  //Renderização do componente
  render() {
    console.disableYellowBox = true;

    //Envia a mensagem de controle manual para o webServerManual
    function sendToWebServerManual(speed, steer, limit, power) {
      command =
        "http://" +
        global.serverIp +
        ":" +
        global.portManual +
        "/" +
        0 +
        "*" +
        "speed$" +
        speed +
        "*" +
        "steer$" +
        steer +
        "*" +
        "limit$" +
        limit +
        "*" +
        "powerA$" +
        power +
        "*" +
        "powerB$" +
        0 +
        "*" +
        "pulverize$" +
        global.uv;
      new WebSocket(command);
    }

    //Envia a mensagem de controle automático para o webserver de parâmetros
    function sendToParamServer(
      limit,tickDefault,steerDefault,speedDefault,shiftDirection,moveTimeAuto,stopTimeAuto
    ){
      command =
        "http://" +
        global.serverIpAuto +
        ":" +
        global.portAuto +
        "/" +
        "limit$" +
        limit +
        "*" +
        "tick$" +
        tickDefault +
        "*" +
        "steer$" +
        steerDefault +
        "*" +
        "speed$" +
        speedDefault +
        "*" +
        "shift$" +
        shiftDirection +
        "*" +
        "uv$" +
        global.uv +
        "*" +
        "detect$" +
        global.detectDistance +
        "*" +
        "move$" +
        moveTimeAuto +
        "*" +
        "stop$" +
        stopTimeAuto;
      new WebSocket(command);
    }

    //Envia o sinal para o relé ligar ou desligar
    function sendSignalToRelay(relayId) {
      if (relayId == "Power") {
        sendToWebServerManual(0, 0, 0, 1, global.uv);
      }
    }

    //Função que pega os valores de x e y do JoyStick e os envia para o robô
    function sendManualCommand(joystick_x, joystick_y, uv) {
      global.speed = -Math.round(joystick_y * 100);
      global.steer = Math.round(joystick_x * 100);
      setTimeout(() => {
        sendToWebServerManual(
          global.speed,
          global.steer,
          global.limit,
          0,
          global.uv
        );
      }, global.comunicationDelay);
    }

    //Função que envia os valores corretos para ligar a placa do robô
    function powerButtonPressed() {
      sendSignalToRelay("Power");
    }

    //Função que envia os valores corretos para ligar a lâmpada UV
    function uvButtonPressed() {
      global.uv = global.uv == 0 ? 1 : 0;
      sendToWebServerManual(0, 0, 0, 0, global.uv);
    }

    //Função que liga/desliga o modo de controle automático
    function automaticButtonPressed(autoMode) {
      if (autoMode == 0) {
        sendToParamServer(
          global.limitAuto,
          global.correctionMovements,
          global.steerAuto,
          global.speedAuto,
          global.correctionFactor,
          global.moveTimeAuto,
          global.stopTimeAuto
        );
        return null;
      } else {
        sendToParamServer(0, 0, 0, 0, 0, 0, 0);
        return null;
      }
    }

    //Função que para o robô
    function stopRobot() {
      global.uv = 0;
      sendToWebServerManual(0, 0, 0, 0, 0, 0);
      sendToParamServer(0, 0, 0, 0, 0, -1, -1);
    }

    const JoystickHandlerSize = parseInt(Dimensions.get("window").height * 0.15);
    const JoystickSize = parseInt(Dimensions.get("window").height * 0.25);

    return (
      <>
        {/*View principal*/}
        <View style={Styles.mainContainer}>

          {/*View do botão do menu*/}
          <View style={Styles.menuButton}>

            {/*Botão do menu*/}
            <Picker
              style={{ height: 30, width: 150 }}
              selectedValue={this.state.menuItem}
              onValueChange={(itemValue, itemPosition) => {
                this.setState({
                  menuItemValue: itemValue,
                  menuItem: itemPosition
                });
                this.props.navigation.navigate(itemValue);
              }}
            >
              <Picker.Item label="Controlar" value="Main" />
              <Picker.Item label="Configuração Manual" value="Config" />
              <Picker.Item label="Configuração Automática" value="Automatic" />
            </Picker>

          </View>

          {/* View do joystick */}
          <View style={Styles.joystickView}>

            <AxisPad
              size={JoystickSize}
              handlerSize={JoystickHandlerSize}
              handlerStyle={Styles.handlerView}
              wrapperStyle={Styles.wrapperView}
              autoCenter={false}
              resetOnRelease={true}
              onValue={({ joystick_x, joystick_y }) => {
                if (global.comunicationInterval === 5) {
                  sendManualCommand(joystick_x, joystick_y);
                  global.comunicationInterval = 0;
                } else {
                  if (joystick_x == 0 && joystick_y == 0) {
                    sendManualCommand(0, 0);
                  }
                  global.comunicationInterval =
                    global.comunicationInterval + 1;
                }
                if (this.state.autoMode != 0) {
                  this.setState({ buttonAutoColor: "#000" });
                  this.setState({ autoMode: 0 });
                  sendToParamServer(0, 0, 0, 0, 0, 0, 0);
                }
              }}
            />

          </View>

          {/* View dos botoes*/}
          <View style={Styles.containerButtons}>

            <View style={Styles.powerButtonsContainer}>

              {/*Botão da placa A*/}
              <TouchableOpacity
                style={Styles.actionButton}
                onPress={() => {
                  this.setState({ buttonPowerColor: this.state.buttonPowerColor == "#f00" ? "#0f0" : "#f00" });
                  powerButtonPressed();
                }}
              >
                <Icon
                  name="power-off"
                  size={30}
                  color={this.state.buttonPowerColor}
                />
              </TouchableOpacity>

              {/*Botão da lâmpada UV*/}
              <TouchableOpacity
                style={Styles.actionButton}
                onPress={() => {
                  this.setState({ buttonUvColor: this.state.buttonUvColor == "#000" ? "#993399" : "#000" });
                  uvButtonPressed();
                }}
              >
                <Icon
                  name="lightbulb-o"
                  size={30}
                  color={this.state.buttonUvColor}
                />
              </TouchableOpacity>

              {/*Botão ligar modo automático*/}
              <TouchableOpacity
                style={Styles.actionButton}
                onPress={() => {
                  this.setState({ buttonAutoColor: this.state.buttonAutoColor == "#000" ? "#0f0" : "#000" });
                  automaticButtonPressed(this.state.autoMode);
                  this.setState({ autoMode: this.state.autoMode == 0 ? 1 : 0 });
                }}
              >
                <Icon name="car" size={30} color={this.state.buttonAutoColor} />
              </TouchableOpacity>

            </View>

            {/*Botão parar robô*/}
            <View style={Styles.powerButtonsContainer}>
              <TouchableOpacity
                style={{
                  borderColor: "#c90000",
                  borderRadius: 115,
                  height: 62,
                  width: 200,
                  borderWidth: 3,
                  alignItems: "center",
                  justifyContent: "center"
                }}
                onPress={() => {
                  this.setState({ buttonAutoColor: "#000" });
                  this.setState({ buttonUvColor: "#000" });
                  stopRobot();
                  this.setState({ autoMode: 0 });
                }}
              >
                <Text style={Styles.stopButtonText}>PARAR</Text>
              </TouchableOpacity>

            </View>

          </View>

          {/* View do slider*/}
          <View style={Styles.sliderContainer}>

            {/* View dos botoes + e - e do valor de speed */}
            <View style={Styles.topBarSliderView}>

              {/* Botão de - para diminuir o valor do slider */}
              <TouchableOpacity
                style={Styles.incDecArea}
                onPress={() => {
                  if (this.state.limitSliderValue > 0) {
                    global.limit = this.state.limitSliderValue - 1;
                    this.setState({
                      limitSliderValue: this.state.limitSliderValue - 1
                    });
                  }
                }}
              >
                <Text style={Styles.incDecText}>-</Text>
              </TouchableOpacity>

              <Text style={Styles.speedText}>
                Velocidade {this.state.limitSliderValue}%{" "}
              </Text>

              {/* Botão de + para aumentar o valor do slider */}
              <TouchableOpacity
                style={Styles.incDecArea}
                onPress={() => {
                  if (this.state.limitSliderValue < 100) {
                    global.limit = this.state.limitSliderValue + 1;
                    this.setState({
                      limitSliderValue: this.state.limitSliderValue + 1
                    });
                  }
                }}
              >
                <Text style={Styles.incDecText}>+</Text>
              </TouchableOpacity>
              
            </View>

            {/*Slider*/}
            <Slider
              maximumValue={100}
              minimumValue={0}
              value={this.state.limitSliderValue}
              onValueChange={limitSliderValue => {
                global.limit = limitSliderValue;
                this.setState({ limitSliderValue });
              }}
              style={Styles.slider}
              step={1}
            />

          </View>

          {/* View de logo e versão */}
          <View style={Styles.containerLogoVersion}>

            {/* View das logos */}
            <View style={Styles.logosView}>

              <Image style={Styles.logoUnioeste} source={constUnioesteImg} />
              <Image style={Styles.logoLabiot} source={constLabiotImg} />
              <Image style={Styles.logoPti} source={constPtiImg} />
              <Image style={Styles.logoItaipu} source={constItaipuImg} />

            </View>

            {/*View da versão*/}
            <View>

              <Text style={Styles.versionText}>V {global.version}</Text>

            </View>

          </View>

        </View>
      </>
    );
  }
}
