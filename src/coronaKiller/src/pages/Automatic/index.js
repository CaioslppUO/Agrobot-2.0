import React, { Component } from 'react';
import { View, TextInput, TouchableOpacity, Text, ScrollView } from 'react-native';
import styles from './styles';

export default class Automatic extends Component {

  //Opções do controlador de navegação de páginas 
  static navigationOptions = {
    title: "Configuração do Modo Automático",
    alignContent: 'center',
    headerTitleStyle: {
      flexGrow: 1,
      fontSize : 15
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
    detect_distance: global.detect_distance
  };

  render() {
    return (
      <>
      <ScrollView
        showsVerticalScrollIndicator={false}>
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
              placeholder="Direção:"
              onChangeText={(text) => {
                this.setState({ steerDefault_auto: text })
              }}
            />
            <TextInput
              style={styles.boxText}
              placeholder="Velocidade:"
              onChangeText={(text) => {
                this.setState({ speedDefault_auto: text })
              }}
            />
            <TextInput
              style={styles.boxText}
              placeholder="Nº de Movimentos de correção:"
              onChangeText={(text) => {
                this.setState({ tickDefault_auto: text })
              }}
            />
            <TextInput
              style={styles.boxText}
              placeholder="Fator de Correção:"
              onChangeText={(text) => {
                this.setState({ shiftDirection_auto: text })
              }}
            />
            <TextInput
              style={styles.boxText}
              placeholder="Distância de Colisão(m):"
              onChangeText={(text) => {
                this.setState({ detect_distance: text })
              }}
            />
            <TextInput
              style={styles.boxText}
              placeholder="Andar por(seg):"
              onChangeText={(text) => {
                this.setState({ move_time_auto: text })
              }}
            />
            <TextInput
              style={styles.boxText}
              placeholder="Parar por(seg):"
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
                let lastTick = global.correction_movements
                let lastSteer = global.steer_auto
                let lastSpeed = global.speed_auto
                let lastShift = global.correction_factor
                let lastMoveTime = global.move_time_auto
                let lastStopTime = global.stop_time_auto
                let lastDetectDist = global.detect_distance
                global.limit_auto = this.state.limit_auto
                global.correction_movements = this.state.tickDefault_auto
                global.steer_auto = this.state.steerDefault_auto
                global.speed_auto = this.state.speedDefault_auto
                global.correction_factor = this.state.shiftDirection_auto
                global.move_time_auto = parseFloat(this.state.move_time_auto) * 1000
                global.stop_time_auto = parseFloat(this.state.stop_time_auto) * 1000
                global.detect_distance = this.state.detect_distance
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
        </ScrollView>
      </>
    );
  }
}