import React, {Component} from 'react';
import { View,TextInput,StyleSheet,TouchableOpacity,Text } from 'react-native';

export default class Config extends Component {

    //Variáveis da classe
    state = {
        serverIp: global.serverIp,
        port: global.port,
        minPSpeed: global.minPulverizeSpeed
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
                                global.minPulverizeSpeed = this.state.minPSpeed
                                global.serverIp = this.state.serverIp
                                global.port = this.state.port

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

const styles = StyleSheet.create({
    mainView: {
        backgroundColor: '#ffffff',
        flex: 1,
    },
    boxesView: {
        flexDirection: 'column',
        marginLeft: '20%',
        marginTop: '5%',
        marginRight: '22%',
        height: 120
    },
    ipText: {
        fontSize: 30,
        borderRadius: 10,
        borderWidth: 1,
    },
    portText: {
        marginTop: '5%',
        fontSize: 30,
        borderRadius: 10,
        borderWidth: 1,
    },
    saveView: {
        marginTop: '20%',
        marginLeft: '35%',
        marginRight: '35%',
        height: 90
    },
    saveText: {
        fontSize: 35,
        borderWidth: 1,
        backgroundColor: '#89c5d6',
        textAlign: 'center',
        borderRadius: 10
    },
    comunication: {
        marginTop: '5%',
        fontSize: 30,
        marginLeft: '28%',
        color: '#596e9c',
        fontWeight: 'bold'
    },
    control: {
        marginTop: '10%',
        fontSize: 30,
        marginLeft: '37%',
        color: '#596e9c',
        fontWeight: 'bold'
    },
    minPSpeedText: {
        fontSize: 20,
        borderRadius: 10,
        borderWidth: 1,
    },
    versionView: {
        marginLeft: '89%',
        marginTop: '29%'
      },
    versionText: {
      color: '#02535c',
      fontSize: 10
    }
});