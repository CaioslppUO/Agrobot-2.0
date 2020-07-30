import React, { Component, useState } from "react";
import {
  View,
  TouchableOpacity,
  Text,
  Slider,
  Image,
  Picker,
  Dimensions,
} from "react-native";
import AxisPad from "react-native-axis-pad";
import NavigationActions from "react-navigation/src/NavigationActions";
import styles from "./styles";
import Icon from "react-native-vector-icons/FontAwesome";
import Icon2 from "react-native-vector-icons/MaterialCommunityIcons";

/**
 * Constantes de imagens
 */
const LabiotImg = require("../../resources/labiot.png");
const ptiImg = require("../../resources/pti.png");
const unioesteImg = require("../../resources/unioeste.png");
const itaipuImg = require("../../resources/Itaipu.png");

/*
 * Página principal
 */
export default class Main extends Component {
  //Variáveis globais da classe
  state = {
    speedSliderValue: 50,
    buttonPowerA: "#000",
    buttonPowerB: "#000",
    buttonPulverizador: "#000",
    buttonAuto: "#000",
    autoMode: 0,
    pickerItem: 0,
    pickerValue: 0,
  };

  //Opções do controlador de navegação de páginas
  static navigationOptions = {
    title: "Controle",
    headerTitleStyle: {
      textAlign: "center",
      alignSelf: "center",
      flexGrow: 1,
    },
  };

  //Renderização do componente
  render() {
    console.disableYellowBox = true;

    //Envia a mensagem de controle manual para o webServerManual
    function sendToWebServerManual(
      speed,
      steer,
      limit,
      powerA,
      powerB,
      pulverize
    ) {
      new WebSocket(
        "http://" +
          global.serverIp +
          ":" +
          global.port_manual +
          "/" +
          0 +
          "*" +
          "speed$" +
          speed +
          "*steer$" +
          steer +
          "*limit$" +
          limit +
          "*powerA$" +
          powerA +
          "*powerB$" +
          powerB +
          "*pulverize$" +
          pulverize
      );
    }

    //Envia a mensagem de controle automático para o webserver de parâmetros
    function sendToParamServer(
      limit,
      tickDefault,
      steerDefault,
      speedDefault,
      shiftDirection,
      move_time_auto,
      stop_time_auto
    ) {
      new WebSocket(
        "http://" +
          global.serverIp_auto +
          ":" +
          global.port_auto +
          "/" +
          limit +
          "$" +
          tickDefault +
          "$" +
          steerDefault +
          "$" +
          speedDefault +
          "$" +
          shiftDirection +
          "$" +
          global.pulverize +
          "$" +
          global.detect_distance +
          "$" +
          move_time_auto +
          "$" +
          stop_time_auto
      );
    }

    //Envia o sinal para o relé ligar ou desligar
    function sendSignalToRelay(relay_id) {
      if (relay_id === "PowerA") {
        sendToWebServerManual(0, 0, 0, 1, 0, 0);
      } else if (relay_id === "PowerB") {
        sendToWebServerManual(0, 0, 0, 0, 1, 0);
      }
    }

    //Função que pega os valores de x e y do JoyStick e os envia para o robô
    function sendManualCommand(x, y) {
      global.speed = -Math.round(y * 100);
      global.steer = Math.round(x * 100);
      if (global.speed >= global.minPulverizeSpeed) {
        setTimeout(() => {
          sendToWebServerManual(
            global.speed,
            global.steer,
            global.limit,
            0,
            0,
            global.pulverize
          );
        }, global.comunication_delay);
      } else {
        setTimeout(() => {
          sendToWebServerManual(
            global.speed,
            global.steer,
            global.limit,
            0,
            0,
            0
          );
        }, global.comunication_delay);
      }
    }

    //Função que envia os valores corretos para ligar a placa A do robô
    function powerAButtonPressed() {
      sendSignalToRelay("PowerA");
    }

    //Função que envia os valores corretos para ligar a placa B do robô
    function powerBButtonPressed() {
      sendSignalToRelay("PowerB");
    }

    //Função que envia os valores corretos para ligar o pulverizador
    function pulverizeButtonPressed() {
      global.pulverize = global.pulverize == 0 ? 1 : 0;
      sendManualCommand(0, 0);
    }

    //Função que liga/desliga o modo de controle automático
    function automaticButtonPressed(autoMode) {
      if (autoMode == 0) {
        sendToParamServer(
          global.limit_auto,
          global.correction_movements,
          global.steer_auto,
          global.speed_auto,
          global.correction_factor,
          global.move_time_auto,
          global.stop_time_auto
        );
        return null;
      } else {
        sendToParamServer(0, 0, 0, 0, 0, 0, 0);
        return null;
      }
    }

    //Função que para o robô
    function stopRobot() {
      global.pulverize = 0;
      sendToWebServerManual(0, 0, 0, 0, 0, 0);
      sendToParamServer(0, 0, 0, 0, 0, 0, 0);
    }
    const handlerSizeJoystick = parseInt(
      Dimensions.get("window").height * 0.15
    );
    const sizeJoystick = parseInt(Dimensions.get("window").height * 0.25);
    return (
      <>
        {/*View principal*/}
        <View style={styles.mainContainer}>
          {/*View do botão do menu*/}
          <View style={styles.menuButton}>
            {/*Botão do menu*/}
            <Picker
              style={{ height: 30, width: 150 }}
              selectedValue={this.state.pickerItem}
              onValueChange={(itemValue, itemPosition) => {
                this.setState({
                  pickerValue: itemValue,
                  pickerItem: itemPosition,
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
          <View style={styles.joystickView}>
            <AxisPad
              size={sizeJoystick}
              handlerSize={handlerSizeJoystick}
              handlerStyle={styles.handlerView}
              wrapperStyle={styles.wrapperView}
              autoCenter={false}
              resetOnRelease={true}
              onValue={({ x, y }) => {
                if (global.comunication_interval === 5) {
                  sendManualCommand(x, y);
                  global.comunication_interval = 0;
                } else {
                  if (x == 0 && y == 0) {
                    sendManualCommand(0, 0);
                  }
                  global.comunication_interval =
                    global.comunication_interval + 1;
                }
                if (this.state.autoMode != 0) {
                  this.setState({ buttonAuto: buttonAutoOff });
                  this.setState({ autoMode: 0 });
                }
              }}
            />
          </View>

          {/* View dos botoes*/}
          <View style={styles.containerButtons}>
            <View style={styles.powerButtonsContainer}>
              {/*Botão da placa A*/}
              <TouchableOpacity
                style={{
                  borderRadius: 200,
                  height: 70,
                  borderWidth: 1,
                  width: 70,
                  alignItems: "center",
                  justifyContent: "center",
                }}
                onPress={() => {
                  this.setState({
                    buttonPowerA:
                      this.state.buttonPowerA == "#000" ? "#0f0" : "#000",
                  });
                  powerAButtonPressed();
                }}
              >
                <Icon
                  name="power-off"
                  size={30}
                  color={this.state.buttonPowerA}
                />
              </TouchableOpacity>

              {/*Botão da placa B*/}
              <TouchableOpacity
                style={{
                  borderRadius: 200,
                  height: 70,
                  borderWidth: 1,
                  width: 70,
                  alignItems: "center",
                  justifyContent: "center",
                }}
                onPress={() => {
                  this.setState({
                    buttonPowerB:
                      this.state.buttonPowerB == "#000" ? "#0f0" : "#000",
                  });
                  powerBButtonPressed();
                }}
              >
                <Icon
                  name="power-off"
                  size={30}
                  color={this.state.buttonPowerB}
                />
              </TouchableOpacity>

              {/*Botão do pulverizador*/}
              <TouchableOpacity
                style={{
                  borderRadius: 200,
                  height: 70,
                  borderWidth: 1,
                  width: 70,
                  alignItems: "center",
                  justifyContent: "center",
                }}
                onPress={() => {
                  this.setState({
                    buttonPulverizador:
                      this.state.buttonPulverizador == "#000" ? "#0f0" : "#000",
                  });
                  pulverizeButtonPressed();
                }}
              >
                <Icon2
                  name="spray"
                  size={35}
                  color={this.state.buttonPulverizador}
                />
              </TouchableOpacity>

              {/*Botão ligar modo automático*/}
              <TouchableOpacity
                style={{
                  borderRadius: 200,
                  height: 70,
                  borderWidth: 1,
                  width: 70,
                  alignItems: "center",
                  justifyContent: "center",
                }}
                onPress={() => {
                  this.setState({
                    buttonAuto:
                      this.state.buttonAuto == "#000" ? "#0f0" : "#000",
                  });
                  automaticButtonPressed(this.state.autoMode);
                  this.setState({ autoMode: this.state.autoMode == 0 ? 1 : 0 });
                }}
              >
                <Icon name="car" size={30} color={this.state.buttonAuto} />
              </TouchableOpacity>
            </View>

            {/*Botão parar robô*/}
            <View style={styles.powerButtonsContainer}>
              <TouchableOpacity
                style={{
                  borderColor: "#c90000",
                  borderRadius: 115,
                  height: 62,
                  width: 200,
                  borderWidth: 3,
                  alignItems: "center",
                  justifyContent: "center",
                }}
                onPress={() => {
                  this.setState({ buttonAuto: "#000" });
                  this.setState({ buttonPulverizador: "#000" });
                  stopRobot();
                  this.setState({ autoMode: 0 });
                }}
              >
                <Text style={styles.ButtonText}>PARAR</Text>
              </TouchableOpacity>
            </View>
          </View>

          {/* View do slider*/}
          <View style={styles.sliderContainer}>
            {/* View dos botoes + e - e do valor de speed */}
            <View style={styles.topBarSliderView}>
              {/* Botão de - para diminuir o valor do slider */}
              <TouchableOpacity
                style={styles.area}
                onPress={() => {
                  if (this.state.speedSliderValue > 0) {
                    global.limit = this.state.speedSliderValue - 1;
                    this.setState({
                      speedSliderValue: this.state.speedSliderValue - 1,
                    });
                  }
                }}
              >
                <Text style={styles.sinalText}>-</Text>
              </TouchableOpacity>

              <Text style={styles.speedText}>
                Velocidade {this.state.speedSliderValue}%{" "}
              </Text>

              {/* Botão de + para aumentar o valor do slider */}
              <TouchableOpacity
                style={styles.area}
                onPress={() => {
                  if (this.state.speedSliderValue < 100) {
                    global.limit = this.state.speedSliderValue + 1;
                    this.setState({
                      speedSliderValue: this.state.speedSliderValue + 1,
                    });
                  }
                }}
              >
                <Text style={styles.sinalText}>+</Text>
              </TouchableOpacity>
            </View>

            {/*Slider*/}
            <Slider
              maximumValue={100}
              minimumValue={0}
              value={this.state.speedSliderValue}
              onValueChange={(speedSliderValue) => {
                global.limit = speedSliderValue;
                this.setState({ speedSliderValue });
              }}
              style={styles.slider}
              step={1}
            />
          </View>

          {/* View de logo e versão */}
          <View style={styles.containerLogoVersion}>
            {/* View das logos */}
            <View style={styles.logosView}>
              <Image style={styles.logoUnioeste} source={unioesteImg} />
              <Image style={styles.logoLabiot} source={LabiotImg} />
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
