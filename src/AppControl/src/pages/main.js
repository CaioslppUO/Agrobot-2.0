/* 
 * Versão: 1.2.0
 * Data: 18/03/2020, 19:56
 * Autores: Caio, Lucas
*/

import React, {Component, useState} from 'react'
import { View,StyleSheet,TouchableOpacity,Text,Slider,Image } from 'react-native'
import AxisPad from 'react-native-axis-pad';


export default class Main extends Component{

  static navigationOptions =  {
    title: "Control Interface"
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

        <View style={styles.viewButtonMenu}>
            <TouchableOpacity style={styles.buttonMenu}onPress={execute}>
                      <Image
                        source={require('../resources/menu.png')}
                      />
            </TouchableOpacity>
        </View>

        <View style={styles.joystickView}>
            <AxisPad
                size={105}
                handlerSize = {125}
                handlerStyle = {styles.handlerView}
                wrapperStyle = {styles.wrapperView}
                resetOnRelease={true}
                autoCenter={true}
                onValue={({ x, y }) => {
                  //sendValues(y,x)
                }}
                />
        </View>
        
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

        <View style={styles.viewSlider}>

          <View style={styles.topBarSlider}>
            <TouchableOpacity style={styles.changeSpeedButtonLess}onPress={() => {
              if(this.state.speedSliderValue > 0){
                this.setState({ speedSliderValue: this.state.speedSliderValue-1 })}
              }
            }>
                      <Text style={styles.lessButtonText}>-</Text>
            </TouchableOpacity>

            <Text style={styles.speedText}>Speed {this.state.speedSliderValue}% </Text>

            <TouchableOpacity onPress={() => {
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

        <View style={styles.logos}>
            <Image
              source={require('../resources/unioeste.png')}
            />
            <Image
              source={require('../resources/pti.png')}
            />
            <Image
              source={require('../resources/labiot.png')}
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
    backgroundColor: 'white'
  },
  handlerView: {
    backgroundColor: '#3495EB'
  },
  main: {
    backgroundColor: 'white',
    flex: 1
  },
  buttonsView:{
    flexDirection: 'row',
    paddingLeft: 35,
    marginTop: '15%'
  },
  buttonPowerA: {
    borderRadius: 115,
    height: 42,
    borderWidth: 2,
    width: 100,
    backgroundColor: '#99a7ad'
  },
  buttonPowerB: {
    borderRadius: 115,
    height: 42,
    borderWidth: 2,
    width: 100,
    marginLeft: 10,
    backgroundColor: '#99a7ad'
  },
  buttonPulverizer: {
    borderRadius: 115,
    height: 42,
    borderWidth: 2,
    width: 100,
    marginLeft: 10,
    backgroundColor: '#99a7ad'
  },
  powerButtonText:{
    textAlign: 'center',
    marginTop: '7%'
  },
  pulverizerButtonText: {
    textAlign: 'center',
  },
  viewButtonMenu: {
    marginLeft: '88%',
    marginRight: '0%',
    backgroundColor: 'lightgrey'
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
    marginTop: '20%'
  },
  slider: {
    transform: [{scaleX: 2.0}, {scaleY: 2.0}],
    marginLeft: '22%',
    marginRight: '23%'
  },
  speedText: {
    marginLeft: '15%',
    marginBottom: '5%',
    fontSize: 25,
    borderRadius: 115,
    marginRight: '15%'
  },
  changeSpeedButtonLess: {
    marginLeft: '5%'
  },
  lessButtonText:{
    fontSize: 35,
    height: 46,
    width: 50,
    textAlign: 'center',
  },
  moreButtonText: {
    fontSize: 35,
    height: 46,
    width: 50,
    textAlign: 'center',
  },
  topBarSlider: {
    flexDirection: 'row'
  },
  logos: {
    flexDirection: 'row',
    marginLeft: '15%',
    marginTop: '10%'
  }
});

