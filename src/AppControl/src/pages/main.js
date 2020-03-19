/* 
 * Versão: 1.2.0
 * Data: 19/03/2020, 00:00
 * Autores: Caio, Lucas
*/

import React, {Component, useState} from 'react'
import { View,StyleSheet,TouchableOpacity,Text,Slider,Image,Button } from 'react-native'
import AxisPad from 'react-native-axis-pad';


export default class Main extends Component{

  static navigationOptions =  {
    title: "Control Interface",
    headerRight: <Button 
      color="#02535c" 
      title="Menu" 
      onPress={
        () => alert('clicked')
      }
      />
  };

  state = {
    speedSliderValue: 50
  };

  render(){

    function execute() {
      alert("doNothing")
    }

    return (
      <>
      <View style={styles.main}>

        {/* View do joystick */}
        <View style={styles.joystickView}>
            <AxisPad
                size={190}
                handlerSize = {100}
                handlerStyle = {styles.handlerView}
                wrapperStyle = {styles.wrapperView}
                resetOnRelease={true}
                autoCenter={false}
                onValue={({ x, y }) => {
                  //sendValues(y,x)
                }}
                />
        </View>
        
        {/* View dos botoes de power */}
        <View style={styles.buttonsView}>
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

        {/* View dos botoes do slider e do slider */}
        <View style={styles.viewSlider}>
            {/* View dos botoes + e - e do valor de speed */}
          <View style={styles.topBarSlider}>
            {/* Botão de - para diminuir o valor do slider */}
            <TouchableOpacity style={styles.backgroundsliderText} onPress={() => {
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
        <View style={styles.containerlogos}>
            <Image
              style={styles.logosUnioeste}
              source={require('../resources/unioeste.png')}
            />
            <Image
              style={styles.logosLabiot}
              source={require('../resources/labiot.png')}
            />
            <Image
              style={styles.logosPti}
              source={require('../resources/pti.png')}
            />
        </View>

      </View>
      </>
    );
  }
}

const styles = StyleSheet.create({
  joystickView: {
    marginTop: "30%",
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
  buttonsView:{
    flexDirection: 'row',
    marginTop: '15%',
    // backgroundColor: '#777'
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
  viewSlider: {
    width: '100%',
    height: 65,
    // backgroundColor:'#aaa',
    justifyContent: 'center',
    flexDirection: 'column'
  },
  backgroundsliderText: {
    // backgroundColor: '#f0f',
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
  topBarSlider: {
    flex: 1,
    flexDirection: 'row',
    // backgroundColor: '#777',
    justifyContent: 'space-between'
  },
  containerlogos: {
    flexDirection: 'row',
    // backgroundColor: '#aaa'
  },
  logosUnioeste: {
    margin:'5%',
  },
  logosPti: {
    height: 50,
    width: 110,
    margin:'5%'
  },
  logosLabiot: {
    margin:'5%'
  }
});

