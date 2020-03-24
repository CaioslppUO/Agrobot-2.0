import React, {Component} from 'react';
import { View,TextInput,StyleSheet,TouchableOpacity,Text } from 'react-native';

export default class Config extends Component {

    //Variáveis globais da classe
    state = {
        serverIp: '',
        port: ''
    }

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

                    {/*View dos campos de preenchimento*/}
                    <View style={styles.boxesView}>
                        <TextInput
                            style={styles.ipText}
                            placeholder="Server IP"
                            onChangeText={(text) => {
                                    this.setState({serverIp: text})
                                }
                            }
                        />

                        <TextInput
                            style={styles.portText}
                            placeholder="Port"
                            onChangeText={(text) => {
                                    this.setState({port: text})
                                }
                            }
                        />
                    </View>

                    <View style={styles.saveView}>
                        <TouchableOpacity
                            onPress={() => {
                                alert(this.state.serverIp+':'+this.state.port)
                            }}
                        >
                            <Text style={styles.saveText}>Save</Text>
                        </TouchableOpacity>
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
        flexDirection: 'column'
    },
    ipText: {
        fontSize: 30
    },
    portText: {

    },
    saveView: {
        marginLeft: '43%',
        marginRight: '40%'
    },
    saveText: {
        fontSize: 30,
        borderWidth: 1,
        backgroundColor: '#89c5d6',
        textAlign: 'center',
        borderRadius: 150
    }
});