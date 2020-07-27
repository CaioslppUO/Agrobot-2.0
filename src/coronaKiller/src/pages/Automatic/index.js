import React, { Component } from "react";
import {
  View,
  TextInput,
  TouchableOpacity,
  Text,
  ScrollView
} from "react-native";
import Styles from "./styles";
import Footer from "../../footer";
import LocalData from '../../utils/localData'
import Src from "./src"

// Classe que gerencia o carregamento e a gravação das variáveis na memória.
const localData = new LocalData()

export default class Automatic extends Component {
  state = {
    sliderValue: 100
  }
  //Opções do controlador de navegação de páginas
  static navigationOptions = {
    title: "Configuração do Modo Automático",
    alignContent: "center",
    headerTitleStyle: {
      flexGrow: 1,
      fontSize: 15
    }
  };

  //Variáveis da classe
  state = {
    limitAuto: global.limitAuto,
    tickDefaultAuto: global.correctionMovements,
    steerDefaultAuto: global.steerAuto,
    speedDefaultAuto: global.speedAuto,
    shiftDirectionAuto: global.correctionFactor,
    moveTimeAuto: global.moveTime,
    stopTimeAuto: global.stopTime,
    detectDistance: global.detectDistance,
    limitAutoTemp: global.limitAuto,
    tickDefaultAutoTemp: global.correctionMovements,
    steerDefaultAutoTemp: global.steerAuto,
    speedDefaultAutoTemp: global.speedAuto,
    shiftDirectionAutoTemp: global.correctionFactor,
    moveTimeAutoTemp: global.moveTime,
    stopTimeAutoTemp: global.stopTime,
    detectDistanceTemp: global.detectDistance
  };

  render() {
    return (
      <>
        <ScrollView showsVerticalScrollIndicator={false}>
          {/*View principal*/}
          <View style={Styles.mainContainer}>
            <Text style={Styles.parameters}>Parâmetros</Text>

            {/*View dos campos de preenchimento de comunicação*/}
            <View style={Styles.boxesContainer}>
              <TextInput
                style={Styles.boxText}
                placeholder={"Limite: " + this.state.limitAuto}
                onEndEditing={text => {
                  this.setState({ limitAuto: parseInt(text.nativeEvent.text) });
                }}
                onChangeText={text => {
                  this.setState({ limitAutoTemp: parseInt(text) });
                }}
              />

              <TextInput
                style={Styles.boxText}
                placeholder={"Direção: " + this.state.steerDefaultAuto}
                onSubmitEditing={text => {
                  this.setState({ steerDefaultAuto: parseInt(text.nativeEvent.text) });
                }}
                onChangeText={text => {
                  this.setState({ steerDefaultAutoTemp: parseInt(text) });
                }}
              />

              <TextInput
                style={Styles.boxText}
                placeholder={"Velocidade: " + this.state.speedDefaultAuto}
                onSubmitEditing={text => {
                  this.setState({ speedDefaultAuto: parseInt(text.nativeEvent.text) });
                }}
                onChangeText={text => {
                  this.setState({ speedDefaultAutoTemp: parseInt(text) });
                }}
              />

              <TextInput
                style={Styles.boxText}
                placeholder={
                  "Nº de Movimentos de correção: " + this.state.tickDefaultAuto
                }
                onSubmitEditing={text => {
                  this.setState({ tickDefaultAuto: parseInt(text.nativeEvent.text) });
                }}
                onChangeText={text => {
                  this.setState({ tickDefaultAutoTemp: parseInt(text) });
                }}
              />

              <TextInput
                style={Styles.boxText}
                placeholder={
                  "Fator de Correção: " + this.state.shiftDirectionAuto
                }
                onSubmitEditing={text => {
                  this.setState({ shiftDirectionAuto: parseFloat(text.nativeEvent.text) });
                }}
                onChangeText={text => {
                  this.setState({ shiftDirectionAutoTemp: parseFloat(text) });
                }}
              />

              <TextInput
                style={Styles.boxText}
                placeholder={
                  "Distância de Colisão(m): " + this.state.detectDistance
                }
                onSubmitEditing={text => {
                  this.setState({ detectDistance: parseFloat(text.nativeEvent.text) });
                }}
                onChangeText={text => {
                  this.setState({ detectDistanceTemp: parseFloat(text) });
                }}
              />

              <TextInput
                style={Styles.boxText}
                placeholder={"Andar por(seg): " + this.state.moveTimeAuto}
                onSubmitEditing={text => {
                  this.setState({ moveTimeAuto: parseInt(text.nativeEvent.text) });
                }}
                onChangeText={text => {
                  this.setState({ moveTimeAutoTemp: parseInt(text) });
                }}
              />

              <TextInput
                style={Styles.boxText}
                placeholder={"Parar por(seg): " + this.state.stopTimeAuto}
                onSubmitEditing={text => {
                  this.setState({ stopTimeAuto: parseInt(text.nativeEvent.text) });
                }}
                onChangeText={text => {
                  this.setState({ stopTimeAutoTemp: parseInt(text) });
                }}
              />
            </View>
            {/*View do botão de salvar*/}
            <View style={Styles.containerButtons}>
              <TouchableOpacity
                style={Styles.button}
                onPress={() => {
                  try {
                    Src.checkLimitAuto(this.state.limitAutoTemp)
                    Src.checkCorrectionMovements(this.state.tickDefaultAutoTemp)
                    Src.checkCorrectionFactor(this.state.shiftDirectionAutoTemp)
                    Src.checkSteerAuto(this.state.steerDefaultAutoTemp)
                    Src.checkSpeedAuto(this.state.speedDefaultAutoTemp)
                    Src.checkMoveTimeAuto(this.state.moveTimeAutoTemp)
                    Src.checkStopTimeAuto(this.state.stopTimeAutoTemp)
                    Src.checkDetectDistance(this.state.detectDistanceTemp)

                    global.limitAuto = parseInt(this.state.limitAutoTemp);
                    global.correctionMovements = parseInt(this.state.tickDefaultAutoTemp);
                    global.steerAuto = parseInt(this.state.steerDefaultAutoTemp);
                    global.speedAuto = parseInt(this.state.speedDefaultAutoTemp);
                    global.correctionFactor = parseFloat(this.state.shiftDirectionAutoTemp);
                    global.moveTime = parseInt(this.state.moveTimeAutoTemp);
                    global.stopTime = parseInt(this.state.stopTimeAutoTemp);
                    global.detectDistance = parseFloat(this.state.detectDistanceTemp);

                    localData.storeData("limitAuto", String(this.state.limitAutoTemp));
                    localData.storeData(
                      "correctionMovements",
                      String(this.state.tickDefaultAutoTemp)
                    );
                    localData.storeData("steerAuto", String(this.state.steerDefaultAutoTemp));
                    localData.storeData("speedAuto", String(this.state.speedDefaultAutoTemp));
                    localData.storeData(
                      "correctionFactor",
                      String(this.state.shiftDirectionAutoTemp)
                    );
                    localData.storeData("moveTime", String(this.state.moveTimeAutoTemp));
                    localData.storeData("stopTime", String(this.state.stopTimeAutoTemp));
                    localData.storeData("detectDistance", String(this.state.detectDistanceTemp));

                    this.props.navigation.navigate("Main");
                  } catch (err) {
                    alert(err)
                  }
                }}
              >
                <Text style={Styles.textButtons}>Salvar</Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={Styles.button}
              >
                <Text style={Styles.textButtons}>Redefinir</Text>
              </TouchableOpacity>
            </View>

            <Footer />
          </View>
        </ScrollView>
      </>
    );
  }
}
