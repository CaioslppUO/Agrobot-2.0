/* 
 * Versão: 2.2.3
 * Data: 23/03/2020, 21:09
 * Autores: Caio, Lucas
*/

import React, {Component, useState} from 'react'
import { View,StyleSheet,TouchableOpacity,Text,Slider,Image } from 'react-native'
import AxisPad from 'react-native-axis-pad';
import NavigationActions from 'react-navigation/src/NavigationActions';

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
    navigation: ''
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

    function execute() {
      alert("doNothing")
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
              this.props.navigation.navigate('Config')
            }
          }>
            <Image
              source={require('../resources/menu.png')}
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
                resetOnRelease={true}
                autoCenter={false}
                onValue={({ x, y }) => {
                  //sendValues(y,x)
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
              this.props.navigation.navigate('Config')
            }
          }>
            <Text style={styles.powerButtonText}>On / Off A</Text>
          </TouchableOpacity>

          {/*Botão da placa B*/}
          <TouchableOpacity 
            style={{backgroundColor: this.state.buttonOnOffB,borderRadius: 115,height: 42,width: 100,borderWidth: 2,margin: '2%',marginLeft: '2%',}} 
            onPress={() => {this.setState({buttonOnOffB: this.state.buttonOnOffB == '#99a7ad'? '#3cc761' : '#99a7ad'})}
          }>
            <Text style={styles.powerButtonText}>On / Off B</Text>
          </TouchableOpacity>

          {/*Botão do Pulverizador*/}
          <TouchableOpacity 
            style={{backgroundColor: this.state.buttonOnOffP,borderRadius: 115,height: 42,width: 100,borderWidth: 2,margin: '2%',marginLeft: '2%',}} 
            onPress={() => {this.setState({buttonOnOffP: this.state.buttonOnOffP == '#99a7ad'? '#3cc761' : '#99a7ad'})}
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

        {/*View da versão*/}
        <View style={styles.versionView}>
            <Text style={styles.versionText}>V 2.2.3</Text>
        </View>
      </View>
      </>
    );
  }
}

{/*Estilos*/}
const styles = StyleSheet.create({
  menuButtonView:{
    marginLeft: '87%'
  },
  joystickView: {
    marginTop: "34%",
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
  mainView: {
    backgroundColor: '#ffffff',
    flex: 1
  },
  powerButtonsView:{
    flexDirection: 'row',
    marginTop: '10%',
    marginBottom: '5%'
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
  },
  versionView: {
    marginLeft: '89%',
  },
  versionText: {
    color: '#02535c',
    fontSize: 10
  }
});

