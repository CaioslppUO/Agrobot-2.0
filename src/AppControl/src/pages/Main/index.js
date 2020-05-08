/* 
 * Versão: 2.2.7
 * Data: 23/03/2020, 21:09
 * Autores: Caio, Lucas
*/

import React, {Component, useState} from 'react'
import { View,TouchableOpacity,Text,Slider,Image } from 'react-native'
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



/* 
 * Página principal
*/
export default class Main extends Component{

  //Variáveis globais da classe
  state = {
    speedSliderValue: 50,
    buttonOnOffA: '#99a7ad',
    buttonOnOffB: '#99a7ad',
    buttonOnOffP: '#99a7ad',
  };

  //Opções do controlador de navegação de páginas 
  static navigationOptions =  {
    title: "Control Interface",
    headerTitleStyle: {
      textAlign: 'center',
      alignSelf: 'center',
      flexGrow: 1
    }
  };

  //Renderização do componente
  render(){
    function sendCompleteMsg(speed,steer,limit,powerA,powerB,pulveize){
      new WebSocket('http://' + global.serverIp + ':' + global.port + '/' + global.priority + '*'
      + 'speed$' + speed + '*steer$' + steer + '*limit$' + limit +'*powerA$' + powerA + '*powerB$' + powerB
      + '*pulverize$' + pulveize)
    }
  
    function turnBoardOn(board){
        if(board == 'A'){
            sendCompleteMsg(0,0,0,1,0,0)
        }else{
            sendCompleteMsg(0,0,0,0,1,0)
        }
    }

    return (
      <>
      {/*View principal*/}
      <View style={styles.mainView}>

        {/*View do botão do menu*/}
        <View style={styles.menuButtonView}>
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
                handlerSize = {135}
                handlerStyle = {styles.handlerView}
                wrapperStyle = {styles.wrapperView}
                autoCenter={false}
                resetOnRelease={true}
                onValue={({ x, y }) => {
                  //Defining the values of speed and steer
                  global.speed = -Math.round(y * 100)
                  global.steer =  Math.round(x * 100)
                  if(global.pulverizer == 1 && global.speed >= global.minPulverizeSpeed){
                    sendCompleteMsg(global.speed,global.steer,global.limit,global.powerA,global.powerB,1);
                  }else{
                    sendCompleteMsg(global.speed,global.steer,global.limit,global.powerA,global.powerB,0);
                  }
                }}
                />
        </View>
        
        {/* View dos botoes de power e pulverizer*/}
        <View style={styles.powerButtonsView}>

          {/*Botão da placa A*/}
          <TouchableOpacity 
            style={{backgroundColor: this.state.buttonOnOffA,borderRadius: 115,height: 42,width: 100,borderWidth: 2,margin: '2%',marginLeft: '10%',}} 
            onPress={() => {
              this.setState({buttonOnOffA: this.state.buttonOnOffA == '#99a7ad'? '#3cc761' : '#99a7ad'})
              turnBoardOn('A')
            }
          }>
            <Text style={styles.powerButtonText}>On / Off A</Text>
          </TouchableOpacity>

          {/*Botão da placa B*/}
          <TouchableOpacity 
            style={{backgroundColor: this.state.buttonOnOffB,borderRadius: 115,height: 42,width: 100,borderWidth: 2,margin: '2%',marginLeft: '2%',}} 
            onPress={() => {
              this.setState({buttonOnOffB: this.state.buttonOnOffB == '#99a7ad'? '#3cc761' : '#99a7ad'})
              turnBoardOn('B')
            }
          }>
            <Text style={styles.powerButtonText}>On / Off B</Text>
          </TouchableOpacity>

          {/*Botão do Pulverizador*/}
          <TouchableOpacity 
            style={{backgroundColor: this.state.buttonOnOffP,borderRadius: 115,height: 42,width: 100,borderWidth: 2,margin: '2%',marginLeft: '2%',}} 
            onPress={() => {
              this.setState({buttonOnOffP: this.state.buttonOnOffP == '#99a7ad'? '#3cc761' : '#99a7ad'})
              global.pulverizer == 0? global.pulverizer = 1:global.pulverizer = 0
            }
          }>
            <Text style={styles.pulverizerButtonText}>On / Off Pulverizer</Text>
          </TouchableOpacity>
        </View>

        {/* View do slider*/}
        <View style={styles.sliderView}>
            {/* View dos botoes + e - e do valor de speed */}
          <View style={styles.topBarSliderView}>
            {/* Botão de - para diminuir o valor do slider */}
            <TouchableOpacity onPress={() => {
              if(this.state.speedSliderValue > 0){
                global.limit = this.state.speedSliderValue-1
                this.setState({ speedSliderValue: this.state.speedSliderValue-1 })}
              }
            }>
              <Text style={styles.lessButtonText}>-</Text>
            </TouchableOpacity>
            <Text style={styles.speedText}>Speed {this.state.speedSliderValue}% </Text>
            {/* Botão de + para aumentar o valor do slider */}
            <TouchableOpacity style={styles.backgroundsliderText} onPress={() => {
              if(this.state.speedSliderValue < 100){
                global.limit = this.state.speedSliderValue+1
                this.setState({ speedSliderValue: this.state.speedSliderValue+1 })}
              }
            }>
              <Text style={styles.moreButtonText}>+</Text>
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
              this.setState({speedSliderValue})
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
          
        </View>

          {/*View da versão*/}
          <View style={styles.versionView}>
          <Text style={styles.versionText}>V {global.version}</Text>
        </View>
          
        </View>
      </View>
      </>
    );
  }
}