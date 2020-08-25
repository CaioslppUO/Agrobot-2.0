import React, { useEffect, useState } from "react";
import { View, TextInput, TouchableOpacity, Text, BackHandler, Slider } from "react-native";
import Styles from "./styles";
import Footer from "../../footer";
import { storeData } from "../../utils/localData";
import Src from "./src";
import { globalStyles } from "../../styles";

// Controla o carregamento e a gravação das variáveis na memória.
// const localData = new LocalData();

export default function Config({ navigation }) {
  const [serverIp, setServerIp] = useState(global.roscoreServerIp);
  const [port, setPort] = useState(global.roscoreServerPort);
  const [delay, setDelay] = useState(global.communicationDelay);
  const [serverIpTemp, setServerIpTemp] = useState(global.roscoreServerIp);
  const [portTemp, setPortTemp] = useState(global.roscoreServerPort);
  const [delayTemp, setDelayTemp] = useState(global.communicationDelay);
  const [sliderValue, setSliderValue] = useState(global.sliderSensibility);

  useEffect(() => {
    BackHandler.addEventListener("hardwareBackPress", () => {});
  }, []);

  // componentWillUnmount() {
  // BackHandler.removeEventListener('hardwareBackPress', this.backPressed);
  // }

  return (
    <>
      {/*View principal*/}
      <View style={globalStyles.mainContainer}>
        <View />

        <Text style={globalStyles.title}>Comunicação</Text>

        <View style={Styles.textInputContainer}>
          <TextInput
            style={globalStyles.inputText}
            placeholder={"IP do robô: " + serverIp}
            onEndEditing={(text) => {
              setServerIp(text.nativeEvent.text);
            }}
            onChangeText={(text) => {
              setServerIpTemp(text);
            }}
          />
          <TextInput
            style={globalStyles.inputText}
            placeholder={"Porta: " + port}
            onEndEditing={(text) => {
              setPort(text.nativeEvent.text);
            }}
            onChangeText={(text) => {
              setPortTemp(text);
            }}
          />
          <TextInput
            style={globalStyles.inputText}
            placeholder={"Tempo de resposta(ms): " + delay}
            onEndEditing={(text) => {
              setDelay(text.nativeEvent.text);
            }}
            onChangeText={(text) => {
              setDelayTemp(text);
            }}
          />
        </View>

        <View style={Styles.sliderContainer}>
          <Slider
            maximumValue={100}
            minimumValue={0}
            value={sliderValue}
            onValueChange={(sliderValue) => {
              setSliderValue(sliderValue);
            }}
            style={Styles.slider}
            step={1}
          />
          <View>
            <Text style={Styles.textSlider}>Sensibilidade joystick {sliderValue}% </Text>
          </View>
        </View>

        <View style={Styles.containerButtons}>
          <TouchableOpacity
            style={globalStyles.button}
            onPress={() => {
              try {
                Src.checkIp(serverIpTemp);
                Src.checkPort(portTemp);
                Src.checkDelay(delayTemp);

                global.roscoreServerIp = String(serverIpTemp);
                global.roscoreServerPort = String(portTemp);
                global.communicationDelay = parseFloat(delayTemp);
                global.sliderSensibility = parseInt(sliderValue);

                storeData("roscoreServerIp", String(serverIpTemp));
                storeData("roscoreServerPort", String(portTemp));
                storeData("communicationDelay", String(delayTemp));
                storeData("sliderSensibility", String(sliderValue));
                navigation.navigate("Home");
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
              navigation.navigate("Home");
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
