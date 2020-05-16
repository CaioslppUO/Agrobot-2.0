import React, { Component, useState } from 'react'
import { View, TouchableOpacity, Text, Slider, Image } from 'react-native'
import AxisPad from 'react-native-axis-pad';
import NavigationActions from 'react-navigation/src/NavigationActions';
import styles from './styles';

/**
 * Constantes de imagens
 */
const menuImg = require('../../resources/menu.png')
const LabiotImg = require('../../resources/labiot.png')
const ptiImg = require('../../resources/pti.png')
const unioesteImg = require('../../resources/unioeste.png')
const itaipuImg = require('../../resources/Itaipu.png')

/* 
 * Página principal
*/
export default class Main extends Component {

  //Variáveis globais da classe
  state = {
    speedSliderValue: 50,
    buttonOnOffPower: '#99a7ad',
    buttonOnOffUv: '#99a7ad',
    buttonOnOffAuto: '#99a7ad',
    buttonStop: '#cc1414',
    autoMode: 0,
    move_time_interval_id: null,
  };

  //Opções do controlador de navegação de páginas 
  static navigationOptions = {
    title: "Controle",
    headerTitleStyle: {
      textAlign: 'center',
      alignSelf: 'center',
      flexGrow: 1
    }
  };

  //Renderização do componente
  render() {
    console.disableYellowBox = true;

    //Envia a mensagem de controle manual para o webServerManual
    function sendToWebServerManual(speed, steer, limit, power, uv) {
      new WebSocket('http://' + global.serverIp + ':' + global.port_manual + '/' + 0 + '*'
        + 'speed$' + speed + '*steer$' + steer + '*limit$' + limit + '*powerA$' + power + '*powerB$' + 0
        + '*pulverize$' + uv)
    }

    //Envia a mensagem de controle automático para o webserver de parâmetros
    function sendToParamServer(limit, tickDefault, steerDefault, speedDefault, shiftDirection) {
      new WebSocket('http://' + global.serverIp + ':' + global.port_auto + '/' + limit + "$" + tickDefault + "$" + steerDefault + "$" +
        speedDefault + "$" + shiftDirection)
    }

    //Envia o sinal para o relé ligar ou desligar
    function sendSignalToRelay(relay_id) {
      if (relay_id == 'Power') {
        sendToWebServerManual(0, 0, 0, 1, 0)
      } else {
        sendToWebServerManual(0, 0, 0, 0, 1)
      }
    }

    //Função que pega os valores de x e y do JoyStick e os envia para o robô
    function sendManualCommand(x, y) {
      global.speed = -Math.round(y * 100)
      global.steer = Math.round(x * 100)
      setTimeout(() => {
        sendToWebServerManual(global.speed, global.steer, global.limit, 0, 0)
      }, global.comunication_delay)
    }

    //Função que envia os valores corretos para ligar a placa do robô
    function powerButtonPressed() {
      sendSignalToRelay('Power')
    }

    //Função que envia os valores corretos para ligar a lâmpada UV
    function uvButtonPressed() {
      sendSignalToRelay('UV')
    }

    //Função que liga/desliga o modo de controle automático
    function automaticButtonPressed(autoMode,move_time_interval_id) {
      if (autoMode == 0) {
        if (global.move_time_auto == 0 && global.stop_time_auto == 0) {
          sendToParamServer(global.limit_auto, global.correction_movements, global.steer_auto, global.speed_auto, global.correction_factor)
          return null
        } else {
           return setInterval(() => {
            sendToParamServer(global.limit_auto, global.correction_movements, global.steer_auto, global.speed_auto, global.correction_factor)
            setTimeout(() => {
              sendToParamServer(0, 0, 0, 0, 0)
            }, global.move_time_auto)
          }, global.move_time_auto + global.stop_time_auto)
        }
      } else {
        if(move_time_interval_id != null){
          clearInterval(move_time_interval_id)
        }
        sendToParamServer(0, 0, 0, 0, 0)
        return null
      }
    }

    //Função que para o robô
    function stopRobot(move_time_interval_id){
      if (move_time_interval_id != null) {
        clearInterval(move_time_interval_id)
      }
      sendToWebServerManual(0, 0, 0, 0, 0, 0)
      sendToParamServer(0, 0, 0, 0, 0)
    }

    return (
      <>
        {/*View principal*/}
        <View style={styles.mainContainer}>

          {/*View do botão do menu*/}
          <View style={styles.menuButton}>
            {/*Botão do menu*/}
            <TouchableOpacity onPress={() => { this.props.navigation.navigate('Menu') }}>
              <Image
                source={menuImg}
              />
            </TouchableOpacity>
          </View>

          {/* View do joystick */}
          <View style={styles.joystickView}>
            <AxisPad
              size={190}
              handlerSize={135}
              handlerStyle={styles.handlerView}
              wrapperStyle={styles.wrapperView}
              autoCenter={false}
              resetOnRelease={true}
              onValue={({ x, y }) => { 
                sendManualCommand(x,y)
                if(this.state.autoMode != 0){
                  this.setState({ buttonOnOffAuto: '#99a7ad' })
                  this.setState({ autoMode: 0 })
                  if(this.state.move_time_interval_id != null){
                    clearInterval(this.state.move_time_interval_id)
                  }
                }
              }}
            />
          </View>

          {/* View dos botoes*/}
          <View style={styles.containerButtons}>
            <View style={styles.powerButtonsContainer}>
              {/*Botão da placa A*/}
              <TouchableOpacity
                style={{ backgroundColor: this.state.buttonOnOffPower, borderRadius: 115, height: 42, width: 100, borderWidth: 2, alignItems: 'center', justifyContent: 'center' }}
                onPress={() => {
                  this.setState({ buttonOnOffPower: this.state.buttonOnOffPower == '#99a7ad' ? '#3cc761' : '#99a7ad' })
                  powerButtonPressed()
                }}>
                <Text style={styles.ButtonText}>Ligar Robô</Text>
              </TouchableOpacity>

              {/*Botão da lâmpada UV*/}
              <TouchableOpacity
                style={{ backgroundColor: this.state.buttonOnOffUv, borderRadius: 115, height: 42, width: 100, borderWidth: 2, alignItems: 'center', justifyContent: 'center' }}
                onPress={() => {
                  this.setState({ buttonOnOffUv: this.state.buttonOnOffUv == '#99a7ad' ? '#3cc761' : '#99a7ad' })
                  uvButtonPressed()
                }}>
                <Text style={styles.ButtonText}>Ligar UV</Text>
              </TouchableOpacity>

              {/*Botão ligar modo automático*/}
              <TouchableOpacity
                style={{ backgroundColor: this.state.buttonOnOffAuto, borderRadius: 115, height: 42, width: 100, borderWidth: 2, alignItems: 'center', justifyContent: 'center' }}
                onPress={() => {
                  this.setState({ buttonOnOffAuto: this.state.buttonOnOffAuto == '#99a7ad' ? '#3cc761' : '#99a7ad' })
                  this.state.move_time_interval_id = automaticButtonPressed(this.state.autoMode,this.state.move_time_interval_id)
                  this.setState({ autoMode: this.state.autoMode == 0 ? 1 : 0 })
                }}>
                <Text style={styles.ButtonText}>Modo Automático</Text>
              </TouchableOpacity>

            </View>

            {/*Botão parar robô*/}
            <View style={styles.powerButtonsContainer}>
              <TouchableOpacity
                style={{ backgroundColor: '#cc1414', borderRadius: 115, height: 62, width: 200, borderWidth: 2, alignItems: 'center', justifyContent: 'center' }}
                onPress={() => {
                  this.setState({ buttonOnOffAuto: '#99a7ad' })
                  stopRobot(this.state.move_time_interval_id)
                  this.setState({ autoMode: 0 })
                }}>
                <Text style={styles.ButtonText}>PARAR</Text>
              </TouchableOpacity>
            </View>
          </View>

          {/* View do slider*/}
          <View style={styles.sliderContainer}>
            {/* View dos botoes + e - e do valor de speed */}
            <View style={styles.topBarSliderView}>

              {/* Botão de - para diminuir o valor do slider */}
              <TouchableOpacity
                onPress={() => {
                  if (this.state.speedSliderValue > 0) {
                    global.limit = this.state.speedSliderValue - 1
                    this.setState({ speedSliderValue: this.state.speedSliderValue - 1 })
                  }
                }}
              >
                <Text style={styles.sinalText}>-</Text>
              </TouchableOpacity>

              <Text style={styles.speedText}>Velocidade {this.state.speedSliderValue}% </Text>

              {/* Botão de + para aumentar o valor do slider */}
              <TouchableOpacity onPress={() => {
                if (this.state.speedSliderValue < 100) {
                  global.limit = this.state.speedSliderValue + 1
                  this.setState({ speedSliderValue: this.state.speedSliderValue + 1 })
                }
              }
              }>
                <Text style={styles.sinalText}>+</Text>
              </TouchableOpacity>
            </View>

            {/*Slider*/}
            <Slider
              maximumValue={100}
              minimumValue={0}
              value={this.state.speedSliderValue}
              onValueChange={
                speedSliderValue => {
                  global.limit = speedSliderValue
                  this.setState({ speedSliderValue })
                }
              }
              style={styles.slider}
              step={1}
            />

          </View>

          {/* View de logo e versão */}
          <View style={styles.containerLogoVersion}>

            {/* View das logos */}
            <View style={styles.logosView}>

              <Image
                style={styles.logoUnioeste}
                source={unioesteImg}
              />
              <Image
                style={styles.logoLabiot}
                source={LabiotImg}
              />
              <Image
                style={styles.logoPti}
                source={ptiImg}
              />
              <Image
                style={styles.logoItaipu}
                source={itaipuImg}
              />

            </View>

            {/*View da versão*/}
            <View>
              <Text style={styles.versionText}>V {global.version}</Text>
            </View>

          </View>

        </View>
      </>
    );
  }
}