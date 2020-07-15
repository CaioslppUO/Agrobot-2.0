import React, { Component } from "react";
import {View,TextInput,TouchableOpacity,Text,ScrollView,AsyncStorage
} from "react-native";
import styles from "./styles";

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
    storeData = async (name, value) => {
      try {
        await AsyncStorage.setItem(name, value);
      } catch (error) {
        alert("Erro ao salvar a variável " + name + ". Erro: " + error)
      }
    }

    return (
      <>
        <ScrollView showsVerticalScrollIndicator={false}>

          {/*View principal*/}
          <View style={styles.mainContainer}>

            <Text style={styles.parameters}>Parâmetros</Text>

            {/*View dos campos de preenchimento de comunicação*/}
            <View style={styles.boxesContainer}>

              <TextInput
                style={styles.boxText}
                placeholder={"Limite: " + this.state.limitAuto}
                onEndEditing={text => {
                  this.setState({ limitAuto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ limitAutoTemp: text })
                }}
              />

              <TextInput
                style={styles.boxText}
                placeholder={"Direção: " + this.state.steerDefaultAuto}
                onSubmitEditing={text => {
                  this.setState({ steerDefaultAuto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ steerDefaultAutoTemp: text })
                }}
              />

              <TextInput
                style={styles.boxText}
                placeholder={"Velocidade: " + this.state.speedDefaultAuto}
                onSubmitEditing={text => {
                  this.setState({ speedDefaultAuto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ speedDefaultAutoTemp: text })
                }}
              />

              <TextInput
                style={styles.boxText}
                placeholder={
                  "Nº de Movimentos de correção: " + this.state.tickDefaultAuto
                }
                onSubmitEditing={text => {
                  this.setState({ tickDefaultAuto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ tickDefaultAutoTemp: text })
                }}
              />

              <TextInput
                style={styles.boxText}
                placeholder={
                  "Fator de Correção: " + this.state.shiftDirectionAuto
                }
                onSubmitEditing={text => {
                  this.setState({ shiftDirectionAuto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ shiftDirectionAutoTemp: text })
                }}
              />

              <TextInput
                style={styles.boxText}
                placeholder={
                  "Distância de Colisão(m): " + this.state.detectDistance
                }
                onSubmitEditing={text => {
                  this.setState({ detectDistance: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ detectDistanceTemp: text })
                }}
              />

              <TextInput
                style={styles.boxText}
                placeholder={"Andar por(seg): " + this.state.moveTimeAuto}
                onSubmitEditing={text => {
                  this.setState({ moveTimeAuto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ moveTimeAutoTemp: text })
                }}
              />

              <TextInput
                style={styles.boxText}
                placeholder={"Parar por(seg): " + this.state.stopTimeAuto}
                onSubmitEditing={text => {
                  this.setState({ stopTimeAuto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ stopTimeAutoTemp: text })
                }}
              />

            </View>

            {/*View do botão de salvar*/}
            <View style={styles.saveButton}>

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
                  
                  storeData("limitAuto",this.state.limitAutoTemp)
                  storeData("correctionMovements",this.state.tickDefaultAutoTemp)
                  storeData("steerAuto",this.state.steerDefaultAutoTemp)
                  storeData("speedAuto",this.state.speedDefaultAutoTemp)
                  storeData("correctionFactor",this.state.shiftDirectionAutoTemp)
                  storeData("moveTimeAuto",this.state.moveTimeAutoTemp)
                  storeData("stopTimeAuto",this.state.stopTimeAutoTemp)
                  storeData("detectDistance",this.state.detectDistanceTemp)

                  this.props.navigation.navigate("Main");
                }}
              >
                <Text style={styles.saveText}>Salvar</Text>
              </TouchableOpacity>

            </View>

            {/*View da versão*/}
            <View style={styles.versionContainer}>

              <Text style={styles.versionText}>V {global.version}</Text>

            </View>

          </View>

        </ScrollView>
      </>
    );
  }
}
