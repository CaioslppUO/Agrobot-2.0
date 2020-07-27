import React, { Component } from "react";
import {
  View,
  TouchableOpacity,
  Text,
  Slider,
  Picker,
  Dimensions
} from "react-native";

import AxisPad from "react-native-axis-pad";
import Styles from "./styles";
import Icon from "react-native-vector-icons/FontAwesome";
import Footer from "../../footer";
import Src from "./src.js";

// Classe que controla o código fonte.
const src = new Src();

export default class Main extends Component {
  state = {
    limitSliderValue: 50,
    buttonPowerColor: "#f00",
    buttonUvColor: "#000",
    buttonAutoColor: "#000",
    autoMode: 0,
    menuItem: 0,
    menuItemValue: 0
  };
  componentWillMount() {
    this.props.navigation.navigate("Connection");
    global.props = this.props;
  }
  // Opções do controlador de navegação de páginas.
  static navigationOptions = {
    title: "Controle",
    headerTitleStyle: {
      textAlign: "center",
      alignSelf: "center",
      flexGrow: 1
    },
    headerLeft: () => (
      <Picker
        style={{ height: 30, width: 150, color: "#ffffff" }}
        selectedValue={0}
        onValueChange={(itemValue, itemPosition) => {
          global.props.navigation.navigate(itemValue);
        }}
      >
        <Picker.Item label="Controlar" value="Main" />
        <Picker.Item label="Configuração Manual" value="Config" />
        <Picker.Item label="Configuração Automática" value="Automatic" />
      </Picker>
    )
  };

  // Carrega a tela de teste de conexão.
  componentWillMount() {
    this.props.navigation.navigate("Connection");
  }

  //Renderização do componente
  render() {
    console.disableYellowBox = true;
    const JoystickHandlerSize = parseInt(
      Dimensions.get("window").height * 0.15
    );
    const JoystickSize = parseInt(Dimensions.get("window").height * 0.25);

    return (
      <>
        {/*View principal*/}
        <View style={Styles.mainContainer}>


          {/* View do joystick */}
          <View style={Styles.joystickView}>
            <AxisPad
              size={JoystickSize}
              handlerSize={JoystickHandlerSize}
              handlerStyle={Styles.handlerView}
              wrapperStyle={Styles.wrapperView}
              autoCenter={false}
              resetOnRelease={true}
              onValue={({ x, y }) => {
                // Não alterar o nome x e y.
                joystick_x = x;
                joystick_y = y;
                if (global.communicationInterval === 5) {
                  src.sendManualCommand(joystick_x, joystick_y);
                  global.communicationInterval = 0;
                } else {
                  if (joystick_x == 0 && joystick_y == 0) {
                    src.sendManualCommand(0, 0);
                  }
                  global.communicationInterval =
                    global.communicationInterval + 1;
                }
                if (this.state.autoMode != 0) {
                  this.setState({ buttonAutoColor: "#000" });
                  this.setState({ autoMode: 0 });
                  src.stopAutoMode();
                }
              }}
            />
          </View>

          {/* View dos botões*/}
          <View style={Styles.containerButtons}>
            <View style={Styles.powerButtonsContainer}>
              {/*Botão da placa A*/}
              <TouchableOpacity
                style={Styles.actionButton}
                onPress={() => {
                  this.setState({
                    buttonPowerColor:
                      this.state.buttonPowerColor == "#f00" ? "#0f0" : "#f00"
                  });
                  src.powerButtonPressed();
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
                  this.setState({
                    buttonUvColor:
                      this.state.buttonUvColor == "#000" ? "#993399" : "#000"
                  });
                  src.uvButtonPressed();
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
                  this.setState({
                    buttonAutoColor:
                      this.state.buttonAutoColor == "#000" ? "#0f0" : "#000"
                  });
                  src.automaticButtonPressed(this.state.autoMode);
                  this.setState({ autoMode: this.state.autoMode == 0 ? 1 : 0 });
                }}
              >
                <Icon name="car" size={30} color={this.state.buttonAutoColor} />
              </TouchableOpacity>
            </View>

            {/*Botão parar robô*/}
            <View style={Styles.powerButtonsContainer}>
              <TouchableOpacity
                style={Styles.stopButton}
                onPress={() => {
                  this.setState({ buttonAutoColor: "#000" });
                  this.setState({ buttonUvColor: "#000" });
                  src.stopRobot();
                  this.setState({ autoMode: 0 });
                }}
              >
                <Text style={Styles.stopButtonText}>PARAR</Text>
              </TouchableOpacity>
            </View>
          </View>

          {/* View do slider*/}
          <View style={Styles.sliderContainer}>
            {/* View dos botões + e - e do valor de speed */}
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

          <Footer />
        </View>
      </>
    );
  }
}
