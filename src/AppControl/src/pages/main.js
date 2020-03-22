/* 
 * Versão: 1.2.1
 * Data: 21/03/2020, 23:36
 * Autores: Caio, Lucas
*/

import React, {Component, useState} from 'react'
import { View,StyleSheet,TouchableOpacity,Text,Slider,Image,Button } from 'react-native'
import AxisPad from 'react-native-axis-pad';

/* 
 * Página principal
*/
export default class Main extends Component{

  //Opções do controlador de navegação de páginas 
  static navigationOptions =  {
    title: "Control Interface",
    headerRight: 
    //Botão do menu
    <TouchableOpacity onPress={() => {alert('menu')}}>
      <Image
        source={require('../resources/menu.png')}
      />
    </TouchableOpacity>
  };

  //Variáveis globais da classe
  state = {
    speedSliderValue: 50
  };

  //Renderização do componente
  render(){

    function execute() {
      alert("doNothing")
    }

    return (
      <>
      {/*View principal*/}
      <View style={styles.main}>

        {/* View do joystick */}
        <View style={styles.joystickView}>
            <AxisPad
                size={190}
                handlerSize = {135}
                handlerStyle = {styles.handlerView}
                wrapperStyle = {styles.wrapperView}
                resetOnRelease={true}
                autoCenter={false}
                onValue={({ x, y }) => {
                  //sendValues(y,x)
                }}
                />
        </View>
        
        {/* View dos botoes de power e pulverizer*/}
        <View style={styles.powerButtonsView}>
          <TouchableOpacity style={styles.buttonPowerA}onPress={execute}>
            <Text style={styles.powerButtonText}>On / Off A</Text>
          </TouchableOpacity>

          <TouchableOpacity style={styles.buttonPowerB}onPress={execute}>
            <Text style={styles.powerButtonText}>On / Off B</Text>
          </TouchableOpacity>

          <TouchableOpacity style={styles.buttonPulverizer}onPress={execute}>
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
                this.setState({ speedSliderValue: this.state.speedSliderValue-1 })}
              }
            }>
              <Text style={styles.lessButtonText}>-</Text>
            </TouchableOpacity>
            <Text style={styles.speedText}>Speed {this.state.speedSliderValue}% </Text>
            {/* Botão de + para aumentar o valor do slider */}
            <TouchableOpacity style={styles.backgroundsliderText} onPress={() => {
              if(this.state.speedSliderValue < 100){
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
          onValueChange={speedSliderValue => this.setState({speedSliderValue})}
          style={styles.slider}
          step={1}
          />

        </View>

        {/* View das logos */}
        <View style={styles.logosView}>
            <Image
              style={styles.logoUnioeste}
              source={require('../resources/unioeste.png')}
            />
            <Image
              style={styles.logoLabiot}
              source={require('../resources/labiot.png')}
            />
            <Image
              style={styles.logoPti}
              source={require('../resources/pti.png')}
            />
        </View>
      </View>
      </>
    );
  }
}

{/*Estilos*/}
const styles = StyleSheet.create({
  joystickView: {
    marginTop: "45%",
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
  },
  wrapperView: {
    backgroundColor: '#ffffff'
  },
  handlerView: {
    backgroundColor: '#3495EB'
  },
  main: {
    backgroundColor: '#ffffff',
    flex: 1
  },
  powerButtonsView:{
    flexDirection: 'row',
    marginTop: '10%',
    marginBottom: '5%'
  },
  buttonPowerA: {
    borderRadius: 115,
    height: 42,
    width: 100,
    borderWidth: 2,
    margin: '2%',
    marginLeft: '10%',
    backgroundColor: '#99a7ad'
  },
  buttonPowerB: {
    borderRadius: 115,
    height: 42,
    width: 100,
    borderWidth: 2,
    margin: '2%',
    
    backgroundColor: '#99a7ad'
  },
  buttonPulverizer: {
    borderRadius: 115,
    height: 42,
    width: 100,
    borderWidth: 2,
    margin: '2%',
    
    backgroundColor: '#99a7ad'
  },
  powerButtonText:{
    textAlign: 'center',
    padding: 8
  },
  pulverizerButtonText: {
    textAlign: 'center',
  },
  buttonMenu: {
    height: 40,
    width: 50,
  },
  menuButtonText: {
    textAlign: 'center',
    marginTop: '7%'
  },
  sliderView: {
    width: '100%',
    height: 65,
    justifyContent: 'center',
    flexDirection: 'column',
  },
  backgroundsliderText: {
    width: 40,
    flexDirection: 'row'
  },
  slider: {
    transform: [{scaleX: 2.0}, {scaleY: 2.0}],
    marginLeft: '22%',
    marginRight: '23%',
    justifyContent: 'flex-end'
  },
  changeSpeedButtonLess: {
    justifyContent: 'flex-end'
  },
  speedText: {
    fontSize: 20,
    justifyContent: 'center',
    marginLeft:'5%',
    margin: 5
  },
  lessButtonText:{
    fontSize: 35,
    height: 50,
    width: 40,
    marginLeft: 10,
    margin: -5
  },
  moreButtonText: {
    fontSize: 35,
    height: 50,
    width: 50,
    marginLeft: 10,
    margin: -3
  },
  topBarSliderView: {
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'space-between'
  },
  logosView: {
    flexDirection: 'row',
    marginTop: '10%'
  },
  logoUnioeste: {
    margin:'5%',
  },
  logoPti: {
    height: 50,
    width: 110,
    margin:'5%'
  },
  logoLabiot: {
    margin:'5%'
  }
});

