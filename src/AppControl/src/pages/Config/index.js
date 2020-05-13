import React, {Component} from 'react';
import { View,TextInput,TouchableOpacity,Text } from 'react-native';
import styles from './styles';

export default class Config extends Component {

    //Variáveis da classe
    state = {
        serverIp: global.serverIp,
        port: global.port,
        minPSpeed: global.minPulverizeSpeed,
        delay: global.delay
    };

    //Opções do controlador de navegação de páginas 
    static navigationOptions =  {
        title: "Config Interface",
        headerTitleStyle: {
            flexGrow: 1,
            marginLeft: '23%'
        }
    };

    render(){
        return (
            <>
                {/*View principal*/}
                <View style={styles.mainView}>

                    <Text style={styles.comunication}>Comunication</Text>
                    {/*View dos campos de preenchimento de comunicação*/}
                    <View style={styles.boxesView}>
                        <TextInput
                            style={styles.ipText}
                            placeholder="Server IP:"
                            onChangeText={(text) => {
                                    this.setState({serverIp: text})
                                }
                            }
                        />

                        <TextInput
                            style={styles.portText}
                            placeholder="Port:"
                            onChangeText={(text) => {
                                    this.setState({port: text})
                                }
                            }
                        />

                        <TextInput
                            style={styles.delayText}
                            placeholder="Delay(ms):"
                            onChangeText={(text) => {
                                    this.setState({delay: text})
                                }
                            }
                        />
                    </View>

                    <Text style={styles.control}>Control</Text>
                    {/*View dos campos de preenchimento de controle*/}
                    <View style={styles.boxesView}>
                        <TextInput
                            style={styles.minPSpeedText}
                            placeholder="Min Pulverize Speed:"
                            onChangeText={(text) => {
                                    this.setState({minPSpeed: text})
                                }
                            }
                        />
                    </View>
                    
                    {/*View do botão de salvar*/}
                    <View style={styles.saveView}>
                        <TouchableOpacity
                            onPress={() => {
                                let lastIp = global.serverIp
                                let lastMPS = global.minPulverizeSpeed
                                let lastDelay = global.delay
                                global.minPulverizeSpeed = this.state.minPSpeed
                                global.serverIp = this.state.serverIp
                                global.port = this.state.port
                                global.delay = parseFloat(this.state.delay)

                                if(global.serverIp.split(".").length != 4){
                                    alert('Invalid IP')
                                    global.serverIp = lastIp
                                }

                                if(global.minPulverizeSpeed < 0 || global.minPulverizeSpeed > 100){
                                    alert('Invalid Min Pulverize speed')
                                    global.minPulverizeSpeed = lastMPS
                                }
                                
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

