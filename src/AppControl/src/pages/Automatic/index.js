import React, { Component } from 'react';
import { View, TextInput, TouchableOpacity, Text } from 'react-native';
import styles from './styles';

export default class Automatic extends Component {

    //Opções do controlador de navegação de páginas 
    static navigationOptions = {
        title: "Auto Config Interface",
        headerTitleStyle: {
            flexGrow: 1,
            marginLeft: '18%'
        }
    };

    //Variáveis da classe
    state = {
        limit_auto: global.limit_auto,
        tickDefault_auto: global.tickDefault_auto,
        steerDefault_auto: global.steerDefault_auto,
        speedDefault_auto: global.speedDefault_auto,
        shiftDirection_auto: global.shiftDirection_auto
    };

    render() {
        function sendMsg(limit, tickDefault, steerDefault, speedDefault, shiftDirection) {
            new WebSocket('http://' + global.serverIp + ':' + global.port_auto + '/' + limit + "$" + tickDefault + "$" + steerDefault + "$" +
                speedDefault + "$" + shiftDirection)
        }

        return (
            <>
                {/*View principal*/}
                <View style={styles.mainView}>

                    <Text style={styles.parameters}>Parameters</Text>
                    {/*View dos campos de preenchimento de comunicação*/}
                    <View style={styles.boxesView}>
                        <TextInput
                            style={styles.firstBoxText}
                            placeholder="Limit:"
                            onChangeText={(text) => {
                                this.setState({ limit_auto: text })
                            }
                            }
                        />

                        <TextInput
                            style={styles.boxText}
                            placeholder="SteerDefault:"
                            onChangeText={(text) => {
                                this.setState({ steerDefault_auto: text })
                            }
                            }
                        />

                        <TextInput
                            style={styles.boxText}
                            placeholder="SpeedDefault:"
                            onChangeText={(text) => {
                                this.setState({ speedDefault_auto: text })
                            }
                            }
                        />

                        <TextInput
                            style={styles.boxText}
                            placeholder="tickDefault:"
                            onChangeText={(text) => {
                                this.setState({ tickDefault_auto: text })
                            }
                            }
                        />

                        <TextInput
                            style={styles.boxText}
                            placeholder="ShiftDirection:"
                            onChangeText={(text) => {
                                this.setState({ shiftDirection_auto: text })
                            }
                            }
                        />

                    </View>

                    {/*View do botão de salvar*/}
                    <View style={styles.saveView}>
                        <TouchableOpacity
                            onPress={() => {
                                let lastLimit = global.limit_auto
                                let lastTick = global.tickDefault_auto
                                let lastSteer = global.steerDefault_auto
                                let lastSpeed = global.speedDefault_auto
                                let lastShift = global.shiftDirection_auto

                                global.limit_auto = this.state.limit_auto
                                global.tickDefault_auto = this.state.tickDefault_auto
                                global.steerDefault_auto = this.state.steerDefault_auto
                                global.speedDefault_auto = this.state.speedDefault_auto
                                global.shiftDirection_auto = this.state.shiftDirection_auto

                                sendMsg(this.state.limit_auto,this.state.tickDefault_auto,this.state.steerDefault_auto,this.state.speedDefault_auto,this.state.shiftDirection_auto)
                                this.props.navigation.navigate('Main')
                            }}
                        >
                            <Text style={styles.saveText}>Save</Text>
                        </TouchableOpacity>
                    </View>

                    {/*View da versão*/}
                    <View style={styles.versionView}>
                        <Text style={styles.versionText}>V {global.version}</Text>
                    </View>
                </View>
            </>
        );
    }
}