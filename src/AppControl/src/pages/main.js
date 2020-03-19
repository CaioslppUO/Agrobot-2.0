/* 
 * Versão: 1.2.1
 * Data: 18/03/2020, 23:20
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
    // backgroundColor: '#02535c'
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
    // marginTop: '20%',
    width: '100%',
    height: 65,
    backgroundColor:'#aaa',
    justifyContent: 'center',
    flexDirection: 'column'
  },
  backgroundsliderText: {
    backgroundColor: '#f0f'
  },
  slider: {
    transform: [{scaleX: 2.0}, {scaleY: 2.0}],
    marginLeft: '22%',
    marginRight: '23%',
    justifyContent: 'flex-end'
  },
  changeSpeedButtonLess: {
    marginLeft: '5%'
  },
  speedText: {
    fontSize: 20,
    justifyContent: 'center',
    alignItems: 'center'
  },
  lessButtonText:{
    fontSize: 35,
    height: 50,
    width: 50,
    marginLeft: 10,
    alignItems: 'center'
  },
  moreButtonText: {
    fontSize: 35,
    height: 50,
    width: 50,
    marginRight: 10,
    alignItems: 'center'
  },
  topBarSlider: {
    flex: 1,
    flexDirection: 'row',
    backgroundColor: '#777',
    justifyContent: 'space-between'
  },
  logos: {
    flexDirection: 'row',
    marginLeft: '15%',
    marginTop: '10%'
  }
});

