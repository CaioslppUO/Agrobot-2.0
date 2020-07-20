import React, { Component } from "react";
import {
  View,
  TextInput,
  TouchableOpacity,
  Text,
  ScrollView,
  AsyncStorage
} from "react-native";
import Styles from "./styles";
import Footer from "../../footer";
import Src from "./src"

// Classe que controla o código fonte.
const src = new Src()

export default class Automatic extends Component {
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
    moveTimeAuto: global.moveTimeAuto,
    stopTimeAuto: global.stopTimeAuto,
    detectDistance: global.detectDistance,
    limitAutoTemp: global.limitAuto,
    tickDefaultAutoTemp: global.correctionMovements,
    steerDefaultAutoTemp: global.steerAuto,
    speedDefaultAutoTemp: global.speedAuto,
    shiftDirectionAutoTemp: global.correctionFactor,
    moveTimeAutoTemp: global.moveTimeAuto,
    stopTimeAutoTemp: global.stopTimeAuto,
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
                  this.setState({ limitAuto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ limitAutoTemp: text });
                }}
              />

              <TextInput
                style={Styles.boxText}
                placeholder={"Direção: " + this.state.steerDefaultAuto}
                onSubmitEditing={text => {
                  this.setState({ steerDefaultAuto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ steerDefaultAutoTemp: text });
                }}
              />

              <TextInput
                style={Styles.boxText}
                placeholder={"Velocidade: " + this.state.speedDefaultAuto}
                onSubmitEditing={text => {
                  this.setState({ speedDefaultAuto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ speedDefaultAutoTemp: text });
                }}
              />

              <TextInput
                style={Styles.boxText}
                placeholder={
                  "Nº de Movimentos de correção: " + this.state.tickDefaultAuto
                }
                onSubmitEditing={text => {
                  this.setState({ tickDefaultAuto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ tickDefaultAutoTemp: text });
                }}
              />

              <TextInput
                style={Styles.boxText}
                placeholder={
                  "Fator de Correção: " + this.state.shiftDirectionAuto
                }
                onSubmitEditing={text => {
                  this.setState({ shiftDirectionAuto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ shiftDirectionAutoTemp: text });
                }}
              />

              <TextInput
                style={Styles.boxText}
                placeholder={
                  "Distância de Colisão(m): " + this.state.detectDistance
                }
                onSubmitEditing={text => {
                  this.setState({ detectDistance: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ detectDistanceTemp: text });
                }}
              />

              <TextInput
                style={Styles.boxText}
                placeholder={"Andar por(seg): " + this.state.moveTimeAuto}
                onSubmitEditing={text => {
                  this.setState({ moveTimeAuto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ moveTimeAutoTemp: text });
                }}
              />

              <TextInput
                style={Styles.boxText}
                placeholder={"Parar por(seg): " + this.state.stopTimeAuto}
                onSubmitEditing={text => {
                  this.setState({ stopTimeAuto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ stopTimeAutoTemp: text });
                }}
              />
            </View>

            {/*View do botão de salvar*/}
            <View style={Styles.saveButton}>
              <TouchableOpacity
                onPress={() => {
                  global.limitAuto = this.state.limitAutoTemp;
                  global.correctionMovements = this.state.tickDefaultAutoTemp;
                  global.steerAuto = this.state.steerDefaultAutoTemp;
                  global.speedAuto = this.state.speedDefaultAutoTemp;
                  global.correctionFactor = this.state.shiftDirectionAutoTemp;
                  global.moveTimeAuto = this.state.moveTimeAutoTemp;
                  global.stopTimeAuto = this.state.stopTimeAutoTemp;
                  global.detectDistance = this.state.detectDistanceTemp;

                  src.storeData("limitAuto", this.state.limitAutoTemp);
                  src.storeData(
                    "correctionMovements",
                    this.state.tickDefaultAutoTemp
                  );
                  src.storeData("steerAuto", this.state.steerDefaultAutoTemp);
                  src.storeData("speedAuto", this.state.speedDefaultAutoTemp);
                  src.storeData(
                    "correctionFactor",
                    this.state.shiftDirectionAutoTemp
                  );
                  src.storeData("moveTimeAuto", this.state.moveTimeAutoTemp);
                  src.storeData("stopTimeAuto", this.state.stopTimeAutoTemp);
                  src.storeData("detectDistance", this.state.detectDistanceTemp);

                  this.props.navigation.navigate("Main");
                }}
              >
                <Text style={Styles.saveText}>Salvar</Text>
              </TouchableOpacity>
            </View>

            <Footer />
          </View>
        </ScrollView>
      </>
    );
  }
}
