import { View, Text, Image } from "react-native";
import Styles from "./styles";
import React, { Component } from "react";

const constLabiotImg = require("../resources/labiot.png");
const constPtiImg = require("../resources/pti.png");
const constUnioesteImg = require("../resources/unioeste.png");
const constItaipuImg = require("../resources/Itaipu.png");

export default class footer extends Component {
  render() {
    return (
      <View View style={Styles.containerLogoVersion}>
        <View style={Styles.logosView}>
          <Image style={Styles.logoUnioeste} source={constUnioesteImg} />
          <Image style={Styles.logoLabiot} source={constLabiotImg} />
          <Image style={Styles.logoPti} source={constPtiImg} />
          <Image style={Styles.logoItaipu} source={constItaipuImg} />
        </View>

        <View>
          <Text style={Styles.versionText}>V {global.version}</Text>
        </View>
      </View>
    );
  }
}
