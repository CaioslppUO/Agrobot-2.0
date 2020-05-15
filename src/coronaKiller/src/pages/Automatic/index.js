import React, { Component } from 'react';
import { View, TextInput, TouchableOpacity, Text } from 'react-native';
import styles from './styles';

export default class Automatic extends Component {

  //Opções do controlador de navegação de páginas 
  static navigationOptions = {
    title: "Configuração do Modo Automático",
    headerTitleStyle: {
      flexGrow: 1,
      fontSize : 15
    }
  };

  //Variáveis da classe
  state = {
    limit_auto: global.limit_auto,
    tickDefault_auto: global.tickDefault_auto,
    steerDefault_auto: global.steerDefault_auto,
    speedDefault_auto: global.speedDefault_auto,
    shiftDirection_auto: global.shiftDirection_auto,
    move_time_auto: global.move_time_auto,
    stop_time_auto: global.stop_time_auto,
    detect_distance: global.detect_distance
  };

  render() {
    function sendToParamServer(limit, tickDefault, steerDefault, speedDefault, shiftDirection, detectDist) {
        new WebSocket('http://' + global.serverIp + ':' + global.port_auto + '/' + limit + "$" + tickDefault + "$" + steerDefault + "$" +
            speedDefault + "$" + shiftDirection + "$" + detectDist)
    }
    return (
      <>
        {/*View principal*/}
        <View style={styles.mainContainer}>

          <Text style={styles.parameters}>Parâmetros</Text>
          
          {/*View dos campos de preenchimento de comunicação*/}
          <View style={styles.BoxesContainer}>
            <TextInput
              style={styles.boxText}
                placeholder="Limite:"
                onChangeText={(text) => {
                  this.setState({ limit_auto: text })
                }}
            />
            <TextInput
              style={styles.boxText}
              placeholder="SteerDefault:"
              onChangeText={(text) => {
                this.setState({ steerDefault_auto: text })
              }}
            />
            <TextInput
              style={styles.boxText}
              placeholder="SpeedDefault:"
              onChangeText={(text) => {
                this.setState({ speedDefault_auto: text })
              }}
            />
            <TextInput
              style={styles.boxText}
              placeholder="tickDefault:"
              onChangeText={(text) => {
                this.setState({ tickDefault_auto: text })
              }}
            />
            <TextInput
              style={styles.boxText}
              placeholder="ShiftDirection:"
              onChangeText={(text) => {
                this.setState({ shiftDirection_auto: text })
              }}
            />
            <TextInput
              style={styles.boxText}
              placeholder="collisionDefault:"
              onChangeText={(text) => {
                this.setState({ detect_distance: text })
              }}
            />
            <TextInput
              style={styles.boxText}
              placeholder="Andar por:"
              onChangeText={(text) => {
                this.setState({ move_time_auto: text })
              }}
            />
            <TextInput
              style={styles.boxText}
              placeholder="Parar por:"
              onChangeText={(text) => {
                this.setState({ stop_time_auto: text })
              }}
            />
          </View>
          
          {/*View do botão de salvar*/}
          <View style={styles.saveButton}>
            <TouchableOpacity
              onPress={() => {
                let lastLimit = global.limit_auto
                let lastTick = global.tickDefault_auto
                let lastSteer = global.steerDefault_auto
                let lastSpeed = global.speedDefault_auto
                let lastShift = global.shiftDirection_auto
                let lastMoveTime = globa.move_time_auto
                let lastStopTime = global.stop_time_auto
                let lastDetectDist = globa.detect_distance
                global.limit_auto = this.state.limit_auto
                global.tickDefault_auto = this.state.tickDefault_auto
                global.steerDefault_auto = this.state.steerDefault_auto
                global.speedDefault_auto = this.state.speedDefault_auto
                global.shiftDirection_auto = this.state.shiftDirection_auto
                global.move_time_auto = this.state.move_time_auto
                global.stop_time_auto = this.state.stop_time_auto
                global.detect_distance = this.state.detect_distance
                sendToParamServer(this.state.limit_auto,this.state.tickDefault_auto,this.state.steerDefault_auto,this.state.speedDefault_auto,this.state.shiftDirection_auto,this.state.detect_distance)
                this.props.navigation.navigate('Main')
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
      </>
    );
  }
}