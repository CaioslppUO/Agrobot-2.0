import React, { useState } from "react";
import { View, TextInput, TouchableOpacity, Text, ScrollView, Button } from "react-native";
import Styles from "./styles";
import Footer from "../../footer";
import { storeData } from "../../utils/localData";
import Src from "./src";
import { globalStyles } from "../../styles";

// Controla o carregamento e a gravação das variáveis na memória.
// const localData = new LocalData();

export default function Automatic({ navigation }) {
  const [limitAuto, setLimitAuto] = useState(global.limitAuto);
  const [tickDefaultAuto, setTickDefaultAuto] = useState(global.correctionMovements);
  const [steerDefaultAuto, setSteerDefaultAuto] = useState(global.steerAuto);
  const [speedDefaultAuto, setSpeedDefaultAuto] = useState(global.speedAuto);
  const [shiftDirectionAuto, setShiftDirectionAuto] = useState(global.correctionFactor);
  const [moveTimeAuto, setMoveTimeAuto] = useState(global.moveTime);
  const [stopTimeAuto, setStopTimeAuto] = useState(global.stopTime);
  const [detectDistance, setDetectDistance] = useState(global.detectDistance);
  const [limitAutoTemp, setLimitAutoTemp] = useState(global.limitAuto);
  const [tickDefaultAutoTemp, setTickDefaultAutoTemp] = useState(global.correctionMovements);
  const [steerDefaultAutoTemp, setSteerDefaultAutoTemp] = useState(global.steerAuto);
  const [speedDefaultAutoTemp, setSpeedDefaultAutoTemp] = useState(global.speedAuto);
  const [shiftDirectionAutoTemp, setShiftDirectionAutoTemp] = useState(global.correctionFactor);
  const [moveTimeAutoTemp, setMoveTimeAutoTemp] = useState(global.moveTime);
  const [stopTimeAutoTemp, setStopTimeAutoTemp] = useState(global.stopTime);
  const [detectDistanceTemp, setDetectDistanceTemp] = useState(global.detectDistance);

  function handleSavePage() {
    try {
      Src.checkLimitAuto(limitAutoTemp);
      Src.checkCorrectionMovements(tickDefaultAutoTemp);
      Src.checkCorrectionFactor(shiftDirectionAutoTemp);
      Src.checkSteerAuto(steerDefaultAutoTemp);
      Src.checkSpeedAuto(speedDefaultAutoTemp);
      Src.checkMoveTimeAuto(moveTimeAutoTemp);
      Src.checkStopTimeAuto(stopTimeAutoTemp);
      Src.checkDetectDistance(detectDistanceTemp);

      global.limitAuto = parseInt(limitAutoTemp);
      global.correctionMovements = parseInt(tickDefaultAutoTemp);
      global.steerAuto = parseInt(steerDefaultAutoTemp);
      global.speedAuto = parseInt(speedDefaultAutoTemp);
      global.correctionFactor = parseFloat(shiftDirectionAutoTemp);
      global.moveTime = parseInt(moveTimeAutoTemp);
      global.stopTime = parseInt(stopTimeAutoTemp);
      global.detectDistance = parseFloat(detectDistanceTemp);

      storeData("limitAuto", String(limitAutoTemp));
      storeData("correctionMovements", String(tickDefaultAutoTemp));
      storeData("steerAuto", String(steerDefaultAutoTemp));
      storeData("speedAuto", String(speedDefaultAutoTemp));
      storeData("correctionFactor", String(shiftDirectionAutoTemp));
      storeData("moveTime", String(moveTimeAutoTemp));
      storeData("stopTime", String(stopTimeAutoTemp));
      storeData("detectDistance", String(detectDistanceTemp));

      navigation.navigate("Home");
    } catch (err) {
      alert(err);
    }
  }
  return (
    <>
      <ScrollView showsVerticalScrollIndicator={false}>
        <View style={globalStyles.mainContainer}>
          <Text style={globalStyles.title}>Parâmetros</Text>
          <View style={Styles.boxesContainer}>
            <TextInput
              style={globalStyles.inputText}
              placeholder={"Limite: " + limitAuto}
              onEndEditing={(text) => {
                setLimitAuto(parseInt(text.nativeEvent.text));
              }}
              onChangeText={(text) => {
                setLimitAutoTemp(parseInt(text));
              }}
            />

            <TextInput
              style={globalStyles.inputText}
              placeholder={"Direção: " + steerDefaultAuto}
              onSubmitEditing={(text) => {
                setSteerDefaultAuto(parseInt(text.nativeEvent.text));
              }}
              onChangeText={(text) => {
                setSteerDefaultAutoTemp(parseInt(text));
              }}
            />

            <TextInput
              style={globalStyles.inputText}
              placeholder={"Velocidade: " + speedDefaultAuto}
              onSubmitEditing={(text) => {
                setSpeedDefaultAuto(parseInt(text.nativeEvent.text));
              }}
              onChangeText={(text) => {
                setSpeedDefaultAutoTemp(parseInt(text));
              }}
            />

            <TextInput
              style={globalStyles.inputText}
              placeholder={"Nº de Movimentos de correção: " + tickDefaultAuto}
              onSubmitEditing={(text) => {
                setTickDefaultAuto(parseInt(text.nativeEvent.text));
              }}
              onChangeText={(text) => {
                setTickDefaultAutoTemp(parseInt(text));
              }}
            />

            <TextInput
              style={globalStyles.inputText}
              placeholder={"Fator de Correção: " + shiftDirectionAuto}
              onSubmitEditing={(text) => {
                setShiftDirectionAuto(parseFloat(text.nativeEvent.text));
              }}
              onChangeText={(text) => {
                setShiftDirectionAutoTemp(parseFloat(text));
              }}
            />

            <TextInput
              style={globalStyles.inputText}
              placeholder={"Distância de Colisão(m): " + detectDistance}
              onSubmitEditing={(text) => {
                setDetectDistance(parseFloat(text.nativeEvent.text));
              }}
              onChangeText={(text) => {
                setDetectDistanceTemp(parseFloat(text));
              }}
            />

            <TextInput
              style={globalStyles.inputText}
              placeholder={"Andar por(seg): " + moveTimeAuto}
              onSubmitEditing={(text) => {
                setMoveTimeAuto(parseInt(text.nativeEvent.text));
              }}
              onChangeText={(text) => {
                setMoveTimeAutoTemp(parseInt(text));
              }}
            />

            <TextInput
              style={globalStyles.inputText}
              placeholder={"Parar por(seg): " + stopTimeAuto}
              onSubmitEditing={(text) => {
                setStopTimeAuto(parseInt(text.nativeEvent.text));
              }}
              onChangeText={(text) => {
                setStopTimeAutoTemp(parseInt(text));
              }}
            />
          </View>
          {/*View do botão de salvar*/}
          <View style={Styles.containerButtons}>
            <TouchableOpacity style={globalStyles.button} onPress={handleSavePage}>
              <Text style={globalStyles.textButtons}>Salvar</Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={globalStyles.button}
              onPress={() => {
                Src.buttonResetPressed();
                navigation.navigate("Home");
              }}
              title="Redefinir"
            >
              <Text style={globalStyles.textButtons}>Redefinir</Text>
            </TouchableOpacity>
          </View>

          <Footer />
        </View>
      </ScrollView>
    </>
  );
}
