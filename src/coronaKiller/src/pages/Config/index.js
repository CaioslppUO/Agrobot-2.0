import React, { Component } from 'react';
import { View, TextInput, TouchableOpacity, Text, BackHandler } from 'react-native';
import styles from './styles';

export default class Config extends Component {

    //Variáveis da classe
    state = {
        serverIp: global.serverIp,
        port: global.port_manual,
        minPSpeed: global.minPulverizeSpeed,
        delay: global.comunication_delay
    };

    //Opções do controlador de navegação de páginas 
    static navigationOptions = {
        title: "Configuração",
        headerTitleStyle: {
            flexGrow: 1,
            marginLeft: '25%'
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

                    <Text style={styles.comunication}>Comunicação</Text>
                    {/*View dos campos de preenchimento de comunicação*/}
                    <View style={styles.textInputContainer}>
                        <TextInput
                            style={styles.textDefault}
                            placeholder="IP do robô:"
                            onChangeText={(text) => {
                                this.setState({ serverIp: text })
                            }
                            }
                        />

                        <TextInput
                            style={styles.textDefault}
                            placeholder="Porta:"
                            onChangeText={(text) => {
                                this.setState({ port: text })
                            }
                            }
                        />

                        <TextInput
                            style={styles.textDefault}
                            placeholder="Tempo de resposta(ms):"
                            onChangeText={(text) => {
                                this.setState({ delay: text })
                            }
                            }
                        />
                    </View>

                    {/*View do botão de salvar*/}
                    <View style={styles.saveContainer}>
                        <TouchableOpacity
                            onPress={() => {
                                let lastIp = global.serverIp
                                let lastMPS = global.minPulverizeSpeed
                                let lastDelay = global.comunication_delay
                                global.minPulverizeSpeed = this.state.minPSpeed
                                global.serverIp = this.state.serverIp
                                global.port_manual = this.state.port
                                global.comunication_delay = parseFloat(this.state.delay)

                                if (global.serverIp.split(".").length != 4) {
                                    alert('Invalid IP')
                                    global.serverIp = lastIp
                                }

                                if (global.minPulverizeSpeed < 0 || global.minPulverizeSpeed > 100) {
                                    alert('Invalid Min Pulverize speed')
                                    global.minPulverizeSpeed = lastMPS
                                }

                                this.props.navigation.navigate('Main')
                            }}
                        >
                            <Text style={styles.saveText}>Salvar</Text>
                        </TouchableOpacity>
                    </View>

                    {/*View da versão*/}
                    <View style={styles.versionContainer}>
                        <Text style={styles.versionText}>V {global.version}</Text>
                    </View>
                </View>
            </>
        );
    }
}

