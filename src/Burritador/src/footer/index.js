import {View, Text, Image} from 'react-native';
import Styles from './styles';
import React from 'react';

const constLabiotImg = require('../resources/labiot.png');
const constPtiImg = require('../resources/pti.png');
const constUnioesteImg = require('../resources/unioeste.png');
const constItaipuImg = require('../resources/Itaipu.png');
const constHmccImg = require('../resources/hmcc.jpeg');
const constReceitaImg = require('../resources/receitaFederal.png');
const constMunicipalImg = require('../resources/municipal.png');

export default function footer() {
  return (
    <View View style={Styles.containerLogoVersion}>
      <View style={Styles.logosView}>
        <Image style={Styles.logoReceita} source={constReceitaImg} />
        <Image style={Styles.logoMunicipal} source={constMunicipalImg} />
        <Image style={Styles.logoHmcc} source={constHmccImg} />
      </View>
      <View style={Styles.logosView}>
        <Image style={Styles.logoLabiot} source={constLabiotImg} />
        <Image style={Styles.logoUnioeste} source={constUnioesteImg} />
        <Image style={Styles.logoPti} source={constPtiImg} />
        <Image style={Styles.logoItaipu} source={constItaipuImg} />
      </View>

      <View>
        <Text style={Styles.versionText}>V {global.version}</Text>
      </View>
    </View>
  );
}
