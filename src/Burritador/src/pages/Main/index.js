import React, {useState, useEffect} from 'react';
import {View, TouchableOpacity, Text, Slider, Dimensions} from 'react-native';
import AxisPad from 'react-native-axis-pad';
import Styles from './styles';
import Icon from 'react-native-vector-icons/FontAwesome';
import Footer from '../../footer';
import {globalStyles} from '../../styles';
import Src from './src.js';

// Controla o código fonte.

export default function Main({navigation}) {
  useEffect(() => {
    navigation.navigate('Connection');
  }, []);

  const src = new Src();
  console.disableYellowBox = true;
  const JoystickHandlerSize = parseInt(Dimensions.get('window').height * 0.15);
  const JoystickSize = parseInt(Dimensions.get('window').height * 0.25);

  return (
    <>
      <View style={[globalStyles.mainContainer, Styles.mainContainer]}>
        <View style={Styles.joystickView}>
          <AxisPad
            size={JoystickSize}
            handlerSize={JoystickHandlerSize}
            handlerStyle={Styles.handlerView}
            wrapperStyle={Styles.wrapperView}
            autoCenter={false}
            resetOnRelease={true}
            onValue={({x, y}) => {
              // Não alterar o nome x e y.
              joystick_x = x;
              joystick_y = y;
              // if (global.communicationInterval === 5) {
              //   src.sendManualCommand(
              //     joystick_x,
              //     joystick_y,
              //     global.sliderSensibility,
              //   );
              //   global.communicationInterval = 0;
              // } else {
              //   if (joystick_x == 0 && joystick_y == 0) {
              //     src.sendManualCommand(0, 0, global.sliderSensibility);
              //   }
              //   global.communicationInterval = global.communicationInterval + 1;
              // }
              // if (this.state.autoMode != 0) {
              //   this.setState({buttonAutoColor: '#000'});
              //   this.setState({autoMode: 0});
              //   src.stopAutoMode();
              // }
            }}
          />
        </View>

        <View style={Styles.containerButtons}>
          <View style={Styles.secondaryButtonContainer}>
            <TouchableOpacity
              style={Styles.actionButton}
              onPress={() => {
                // this.setState({
                //   buttonPowerColor:
                //     this.state.buttonPowerColor == '#f00' ? '#0f0' : '#f00',
                // });
                src.powerButtonPressed();
              }}>
              <Icon
                name="power-off"
                size={30}
                // color={this.state.buttonPowerColor}
              />
            </TouchableOpacity>

            <TouchableOpacity
              style={Styles.actionButton}
              onPress={() => {
                // this.setState({
                //   buttonUvColor:
                //     this.state.buttonUvColor == '#000' ? '#993399' : '#000',
                // });
                src.uvButtonPressed();
              }}>
              <Icon
                name="lightbulb-o"
                size={30}
                // color={this.state.buttonUvColor}
              />
            </TouchableOpacity>

            <TouchableOpacity
              style={Styles.actionButton}
              onPress={() => {
                // this.setState({
                //   buttonAutoColor:
                //     this.state.buttonAutoColor == '#000' ? '#0f0' : '#000',
                // });
                src.automaticButtonPressed(this.state.autoMode);
                // this.setState({autoMode: this.state.autoMode == 0 ? 1 : 0});
              }}>
              <Icon name="car" size={30} color="#0ff" />
            </TouchableOpacity>
          </View>

          <View style={Styles.secondaryButtonContainer}>
            <TouchableOpacity
              style={Styles.stopButton}
              onPress={() => {
                // this.setState({buttonAutoColor: '#000'});
                // this.setState({buttonUvColor: '#000'});
                src.stopRobot();
                // this.setState({autoMode: 0});
              }}>
              <Text style={Styles.stopButtonText}>PARAR</Text>
            </TouchableOpacity>
          </View>
        </View>

        <View style={Styles.sliderContainer}>
          <View style={Styles.topBarSliderView}>
            <TouchableOpacity
              style={Styles.buttonContactArea}
              onPress={() => {
                // if (this.state.limitSliderValue > 0) {
                // global.limit = this.state.limitSliderValue - 1;
                // this.setState({
                // limitSliderValue: this.state.limitSliderValue - 1,
                // });
                // }
              }}>
              <Text style={Styles.incDecText}>-</Text>
            </TouchableOpacity>

            <Text style={Styles.speedText}>
              {/* Velocidade {this.state.limitSliderValue}%{' '} */}
            </Text>

            <TouchableOpacity
              style={Styles.buttonContactArea}
              onPress={() => {
                //   if (this.state.limitSliderValue < 100) {
                //     global.limit = this.state.limitSliderValue + 1;
                //     this.setState({
                //       limitSliderValue: this.state.limitSliderValue + 1,
                //     });
                // }
              }}>
              <Text style={Styles.incDecText}>+</Text>
            </TouchableOpacity>
          </View>

          <Slider
            maximumValue={100}
            minimumValue={0}
            value={100} //{this.state.limitSliderValue}
            onValueChange={(limitSliderValue) => {
              global.limit = limitSliderValue;
              // this.setState({limitSliderValue});
            }}
            style={Styles.slider}
            step={1}
          />
        </View>

        <Footer />
      </View>
    </>
  );
}
