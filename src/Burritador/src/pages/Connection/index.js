import React, {Component} from 'react';
import {View, TouchableOpacity, Text} from 'react-native';

import Styles from './styles';
import Footer from '../../footer';
import {globalStyles} from '../../styles';

export default function Connection({navigation}) {
  function tryConnection() {
    for (let i = 0; i < 10; i++) {
      command =
        'http://192.168.1.2:8080/0*speed$' +
        (i % 2 === 0 ? 0 : 1) +
        '*steer$0*limit$0*powerA$0*powerB$0*pulverize$0';
      new WebSocket(command);
    }
  }
  return (
    <>
      <View style={globalStyles.mainContainer}>
        <View style={Styles.spacing} />

        <View style={Styles.containerTutorial}>
          <Text style={Styles.tutorialText}>
            1 - Após ligar o robô, aguarde 2 minutos.
          </Text>
          <Text style={Styles.tutorialText}>
            2 - Clique em estabelecer conexão.
          </Text>
          <Text style={Styles.tutorialText}>
            3 - Caso o led não se acenda, aguarde 5 segundos, clique novamente
            em estabelecer conexão. Repita esse processo ate o led acender.
          </Text>
          <Text style={Styles.tutorialText}>
            4 - Com o led aceso clique em ok.
          </Text>
        </View>

        <View style={Styles.containerButtons}>
          <TouchableOpacity
            style={Styles.buttonTryConnection}
            onPress={() => {
              tryConnection();
            }}>
            <Text style={Styles.buttonTryText}>Estabelecer Conexão</Text>
          </TouchableOpacity>
          <View style={Styles.spacing} />
          <TouchableOpacity
            style={Styles.buttonTryConnection}
            onPress={() => {
              navigation.navigate('Home');
            }}>
            <Text style={Styles.buttonTryText}>OK</Text>
          </TouchableOpacity>
        </View>

        <Footer />
      </View>
    </>
  );
}
