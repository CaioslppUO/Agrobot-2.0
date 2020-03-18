/* 
 * Versão: 1.0.0
 * Data: 18/03/2020, 17:01
 * Autores: Caio, Lucas
*/

import React, {Component} from 'react'
import { Text,View,ScrollView,StyleSheet } from 'react-native'


export default class Main extends Component{

  static navigationOptions =  {
    title: "Control Interface"
  };

  render(){
    return (
      <>
        <View>
          <Text>Main Page</Text>
        </View>
      </>
    );
  }
}

const styles = StyleSheet.create({

});

