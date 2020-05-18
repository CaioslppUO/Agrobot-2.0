import React, { Component } from 'react';
import { View, Text, TouchableOpacity, BackHandler } from 'react-native';

import styles from './styles';

export default class Menu extends Component {
  //Opções do controlador de navegação de páginas 
  static navigationOptions = {
    title: "Menu",
    headerTitleStyle: {
      flexGrow: 1,
      marginLeft: '35%'
    }
  };

  componentWillMount() {
    BackHandler.addEventListener('hardwareBackPress', () => { });
  }

  componentWillUnmount() {
    BackHandler.removeEventListener('hardwareBackPress', this.backPressed)
  }

  render() {
    return (
      <>
        {/*View principal*/}
        <View style={styles.mainContainer}>

          {/*View dos botões*/}
          <View style={styles.buttonContainer}>
            {/*Botão do controle manual*/}
            <TouchableOpacity
              style={styles.Button}
              onPress={() => { this.props.navigation.navigate('Main') }}>
              <Text style={styles.buttonText}>Controle</Text>

            </TouchableOpacity>

            {/*Botão do menu de configuração*/}
            <TouchableOpacity
              style={styles.Button}
              onPress={() => { this.props.navigation.navigate('Config') }}>
              <Text style={styles.buttonText}>Configuração</Text>
            </TouchableOpacity>

            {/*Botão de debug*/}
            <TouchableOpacity
              style={styles.Button}
              onPress={() => { this.props.navigation.navigate('Automatic') }}>
              <Text style={styles.buttonText}>Configuração Modo Automático</Text>
            </TouchableOpacity>

          </View>


          {/*Botão de sair*/}
          <TouchableOpacity
            style={styles.Button}
            onPress={() => {
              BackHandler.exitApp()
            }}>
            <Text style={styles.buttonText}>Sair</Text>
          </TouchableOpacity>

          {/*View da versão*/}
          <View style={styles.containerVersion}>
            <Text style={styles.versionText}>V {global.version}</Text>
          </View>

        </View>
      </>
    );
  }
}

