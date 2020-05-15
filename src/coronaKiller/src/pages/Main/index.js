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
    function sendToWebServerManual(speed, steer, limit, powerA, powerB, pulveize) {
      new WebSocket('http://' + global.serverIp + ':' + global.port + '/' + global.priority + '*'
        + 'speed$' + speed + '*steer$' + steer + '*limit$' + limit + '*powerA$' + powerA + '*powerB$' + powerB
        + '*pulverize$' + pulveize)
    }

    function sendToParamServer(limit, tickDefault, steerDefault, speedDefault, shiftDirection) {
      new WebSocket('http://' + global.serverIp + ':' + global.port_auto + '/' + limit + "$" + tickDefault + "$" + steerDefault + "$" +
          speedDefault + "$" + shiftDirection)
   }

    function turnBoardOn(board) {
      if (board == 'Power') {
        sendToWebServerManual(0, 0, 0, 1, 0, 0)
      } else {
        sendToWebServerManual(0, 0, 0, 0, 0, 1)
      }
    }

    return (
      <>
        {/*View principal*/}
        <View style={styles.mainContainer}>

          {/*View do botão do menu*/}
          <View style={styles.menuButton}>
            {/*Botão do menu*/}
            <TouchableOpacity
              onPress={() => {
                this.props.navigation.navigate('Menu')
              }
              }>
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
                //Defining the values of speed and steer
                global.speed = -Math.round(y * 100)
                global.steer = Math.round(x * 100)
                  setTimeout(() => {
                    sendCompleteMsg(global.speed, global.steer, global.limit, global.powerA, global.powerB, 0)
                  }, global.delay)
              }}
            />
          </View>

          <View style={styles.containerButtons}>

            {/* View dos botoes*/}
            <View style={styles.powerButtonsContainer}>

              {/*Botão da placa A*/}
              <TouchableOpacity
                style={{backgroundColor: this.state.buttonOnOffPower, borderRadius: 115, height: 42, width: 100, borderWidth: 2, alignItems: 'center', justifyContent: 'center'}}
                onPress={() => {
                  this.setState({ buttonOnOffPower: this.state.buttonOnOffPower == '#99a7ad' ? '#3cc761' : '#99a7ad' })
                  turnBoardOn('Power')
                }}>
                <Text style={styles.ButtonText}>Ligar Robô</Text>
              </TouchableOpacity>
              
              {/*Botão da lâmpada UV*/}
              <TouchableOpacity
                style={{ backgroundColor: this.state.buttonOnOffUv, borderRadius: 115, height: 42, width: 100, borderWidth: 2, alignItems: 'center', justifyContent: 'center'}}
                onPress={() => {
                  this.setState({ buttonOnOffUv: this.state.buttonOnOffUv == '#99a7ad' ? '#3cc761' : '#99a7ad' })
                  turnBoardOn('UV')
                }}>
                <Text style={styles.ButtonText}>Ligar UV</Text>
              </TouchableOpacity>
              
              {/*Botão ligar modo automático*/}
              <TouchableOpacity
                style={{ backgroundColor: this.state.buttonOnOffAuto, borderRadius: 115, height: 42, width: 100, borderWidth: 2, alignItems: 'center', justifyContent: 'center'}}
                onPress={() => {
                  this.setState({ buttonOnOffAuto: this.state.buttonOnOffAuto == '#99a7ad' ? '#3cc761' : '#99a7ad' })
                  if (this.state.autoMode == 0) {
                    if (global.move_time_auto == 0 && global.stop_time_auto == 0) {
                      sendToParamServer(global.limit_auto, global.tickDefault_auto, global.steerDefault_auto, global.speedDefault_auto, global.shiftDirection_auto)
                    } else {
                      this.state.move_time_interval_id = setInterval(() => {
                        sendToParamServer(global.limit_auto, global.tickDefault_auto, global.steerDefault_auto, global.speedDefault_auto, global.shiftDirection_auto)
                        setTimeout(() =>{
                          sendToParamServer(0, 0, 0, 0, 0)
                        },global.move_time_auto)
                      },global.move_time_auto + global.stop_time_auto)
                    }
                  } else {
                    clearInterval(this.state.move_time_interval_id)
                    sendToParamServer(0, 0, 0, 0, 0)
                  }
                  this.setState({ autoMode: this.state.autoMode == 0 ? 1 : 0 })
                }}>
                <Text style={styles.ButtonText}>Modo Automático</Text>
              </TouchableOpacity>
          
            </View>

            <View style={styles.powerButtonsContainer}>
              <TouchableOpacity
                style={{ backgroundColor: '#cc1414', borderRadius: 115, height: 62, width: 200, borderWidth: 2, alignItems: 'center', justifyContent: 'center'}}
                  onPress={() => {
                    this.setState({ buttonOnOffAuto: '#99a7ad' })
                    if(this.state.move_time_interval_id != null){
                      clearInterval(this.state.move_time_interval_id)
                    }
                    this.setState({ autoMode: 0})
                    sendToWebServerManual(0, 0, 0, 0, 0, 0)
                    sendToParamServer(0, 0, 0, 0, 0)
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