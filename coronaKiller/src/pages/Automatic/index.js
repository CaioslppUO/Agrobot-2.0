import React, { Component } from "react";
import {
  View,
  TextInput,
  TouchableOpacity,
  Text,
  ScrollView,
  AsyncStorage
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
    limit_auto: global.limit_auto,
    tickDefault_auto: global.correction_movements,
    steerDefault_auto: global.steer_auto,
    speedDefault_auto: global.speed_auto,
    shiftDirection_auto: global.correction_factor,
    move_time_auto: global.move_time_auto,
    stop_time_auto: global.stop_time_auto,
    detect_distance: global.detect_distance,
    limit_auto_temp: global.limit_auto,
    tickDefault_auto_temp: global.correction_movements,
    steerDefault_auto_temp: global.steer_auto,
    speedDefault_auto_temp: global.speed_auto,
    shiftDirection_auto_temp: global.correction_factor,
    move_time_auto_temp: global.move_time_auto,
    stop_time_auto_temp: global.stop_time_auto,
    detect_distance_temp: global.detect_distance
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
            <View style={styles.BoxesContainer}>
              <TextInput
                style={styles.boxText}
                placeholder={"Limite: " + this.state.limit_auto}
                onEndEditing={text => {
                  this.setState({ limit_auto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ limit_auto_temp: text })
                }}
              />
              <TextInput
                style={styles.boxText}
                placeholder={"Direção: " + this.state.steerDefault_auto}
                onSubmitEditing={text => {
                  this.setState({ steerDefault_auto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ steerDefault_auto_temp: text })
                }}
              />
              <TextInput
                style={styles.boxText}
                placeholder={"Velocidade: " + this.state.speedDefault_auto}
                onSubmitEditing={text => {
                  this.setState({ speedDefault_auto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ speedDefault_auto_temp: text })
                }}
              />
              <TextInput
                style={styles.boxText}
                placeholder={
                  "Nº de Movimentos de correção: " + this.state.tickDefault_auto
                }
                onSubmitEditing={text => {
                  this.setState({ tickDefault_auto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ tickDefault_auto_temp: text })
                }}
              />
              <TextInput
                style={styles.boxText}
                placeholder={
                  "Fator de Correção: " + this.state.shiftDirection_auto
                }
                onSubmitEditing={text => {
                  this.setState({ shiftDirection_auto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ shiftDirection_auto_temp: text })
                }}
              />
              <TextInput
                style={styles.boxText}
                placeholder={
                  "Distância de Colisão(m): " + this.state.detect_distance
                }
                onSubmitEditing={text => {
                  this.setState({ detect_distance: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ detect_distance_temp: text })
                }}
              />
              <TextInput
                style={styles.boxText}
                placeholder={"Andar por(seg): " + this.state.move_time_auto}
                onSubmitEditing={text => {
                  this.setState({ move_time_auto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ move_time_auto_temp: text })
                }}
              />
              <TextInput
                style={styles.boxText}
                placeholder={"Parar por(seg): " + this.state.stop_time_auto}
                onSubmitEditing={text => {
                  this.setState({ stop_time_auto: text.nativeEvent.text });
                }}
                onChangeText={text => {
                  this.setState({ stop_time_auto_temp: text })
                }}
              />
            </View>

            {/*View do botão de salvar*/}
            <View style={styles.saveButton}>
              <TouchableOpacity
                onPress={() => {
                  global.limit_auto = this.state.limit_auto_temp;
                  global.correction_movements = this.state.tickDefault_auto_temp;
                  global.steer_auto = this.state.steerDefault_auto_temp;
                  global.speed_auto = this.state.speedDefault_auto_temp;
                  global.correction_factor = this.state.shiftDirection_auto_temp;
                  global.move_time_auto = this.state.move_time_auto_temp;
                  global.stop_time_auto = this.state.stop_time_auto_temp;
                  global.detect_distance = this.state.detect_distance_temp;
                  
                  storeData("limit_auto",this.state.limit_auto_temp)
                  storeData("correction_movements",this.state.tickDefault_auto_temp)
                  storeData("steer_auto",this.state.steerDefault_auto_temp)
                  storeData("speed_auto",this.state.speedDefault_auto_temp)
                  storeData("correction_factor",this.state.shiftDirection_auto_temp)
                  storeData("move_time_auto",this.state.move_time_auto_temp)
                  storeData("stop_time_auto",this.state.stop_time_auto_temp)
                  storeData("detect_distance",this.state.detect_distance_temp)

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
