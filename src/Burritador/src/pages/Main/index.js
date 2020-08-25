import React, { useState, useEffect } from "react";
import { View, TouchableOpacity, Text, Slider, Dimensions } from "react-native";
import AxisPad from "react-native-axis-pad";
import Styles from "./styles";
import Icon from "react-native-vector-icons/FontAwesome";
import Footer from "../../footer";
import { globalStyles } from "../../styles";
import Src from "./src.js";

// Controla o código fonte.

export default function Main({ navigation }) {
  useEffect(() => {
    navigation.navigate("Connection");
  }, []);

  const src = new Src();
  console.disableYellowBox = true;
  const JoystickHandlerSize = parseInt(Dimensions.get("window").height * 0.15);
  const JoystickSize = parseInt(Dimensions.get("window").height * 0.25);
  const [colorLight, setColorLight] = useState("#000");
  const [colorPower, setColorPower] = useState("#f00");
  const [colorAuto, setColorAutomatic] = useState("#000");
  const [autoMode, setAutoMode] = useState(0);
  const [menuItem, setMenuItem] = useState(0);
  const [menuItemValue, setMenuItemValue] = useState(0);
  const [limitSliderValue, setLimitSliderValue] = useState(50);

  function handleSetColorLight() {
    colorLight == "#000" ? setColorLight("#993399") : setColorLight("#000");
  }
  function handleSetColorPower() {
    colorPower == "#f00" ? setColorPower("#0f0") : setColorPower("#f00");
  }
  function handleSetColorAutomatic() {
    colorAuto == "#000" ? setColorAutomatic("#0f0") : setColorAutomatic("#000");
  }

  function handlePowerButton() {
    handleSetColorPower();
    src.powerButtonPressed();
  }

  function handleLightButton() {
    handleSetColorLight();
    src.uvButtonPressed();
  }

  function handleAutomaticButton() {
    handleSetColorAutomatic();
    src.automaticButtonPressed(autoMode);
    setAutoMode(autoMode == 0 ? 1 : 0);
  }

  function handleStopButton() {
    setColorAutomatic("#000");
    setColorLight("#000");
    setAutoMode(0);
    src.stopRobot();
  }

  function handleIncrementSlider() {
    if (limitSliderValue > 0) {
      global.limit = limitSliderValue - 1;
      setLimitSliderValue(limitSliderValue - 1);
    }
  }
  function handleDecrementSlider() {
    if (limitSliderValue < 100) {
      global.limit = limitSliderValue + 1;
      setLimitSliderValue(limitSliderValue + 1);
    }
  }
  return (
    <>
      <View style={[globalStyles.mainContainer, Styles.mainContainer]}>
        <View style={Styles.joystickView}>
          <AxisPad
            size={JoystickSize}
            handlerSize={JoystickHandlerSize}
            handlerStyle={Styles.handlerView}
            wrapperStyle={Styles.wrapperView}
            autoCenter={false}
            resetOnRelease={true}
            onValue={({ x, y }) => {
              if (global.communicationInterval === 5) {
                src.sendManualCommand(x, y, global.sliderSensibility);
                global.communicationInterval = 0;
              } else {
                if (x === 0 && y === 0) {
                  src.sendManualCommand(0, 0, global.sliderSensibility);
                }
                global.communicationInterval = global.communicationInterval + 1;
              }
              if (autoMode != 0) {
                setColorAutomatic("#000");
                setAutoMode(0);
                src.stopAutoMode();
              }
            }}
          />
        </View>

        <View style={Styles.containerButtons}>
          <View style={Styles.secondaryButtonContainer}>
            <TouchableOpacity style={Styles.actionButton} onPress={handlePowerButton}>
              <Icon name="power-off" size={30} color={colorPower} />
            </TouchableOpacity>

            <TouchableOpacity style={Styles.actionButton} onPress={handleLightButton}>
              <Icon name="lightbulb-o" size={30} color={colorLight} />
            </TouchableOpacity>

            <TouchableOpacity style={Styles.actionButton} onPress={handleAutomaticButton}>
              <Icon name="car" size={30} color={colorAuto} />
            </TouchableOpacity>
          </View>

          <View style={Styles.secondaryButtonContainer}>
            <TouchableOpacity style={Styles.stopButton} onPress={handleStopButton}>
              <Text style={Styles.stopButtonText}>PARAR</Text>
            </TouchableOpacity>
          </View>
        </View>

        <View style={Styles.sliderContainer}>
          <View style={Styles.topBarSliderView}>
            <TouchableOpacity style={Styles.buttonContactArea} onPress={handleIncrementSlider}>
              <Text style={Styles.incDecText}>-</Text>
            </TouchableOpacity>

            <Text style={Styles.speedText}>Velocidade {limitSliderValue}% </Text>

            <TouchableOpacity style={Styles.buttonContactArea} onPress={handleDecrementSlider}>
              <Text style={Styles.incDecText}>+</Text>
            </TouchableOpacity>
          </View>

          <Slider
            maximumValue={100}
            minimumValue={0}
            value={limitSliderValue}
            onValueChange={(limitSliderValue) => {
              global.limit = limitSliderValue;
              setLimitSliderValue(limitSliderValue);
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
