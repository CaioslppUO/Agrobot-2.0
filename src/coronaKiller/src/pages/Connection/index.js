import React, { Component } from "react";
import {
    View,
    TouchableOpacity,
    Text
} from "react-native";

import NavigationActions from "react-navigation/src/NavigationActions";
import styles from "./styles";

export default class Connection extends Component {
    state = {
        speed: 0
    }
    static navigationOptions = {
        title: "Teste de conexão",
        alignContent: "center",
        headerTitleStyle: {
            flexGrow: 1,
            fontSize: 15
        }
    };
    
    render() {
        //Envia a mensagem de controle manual para o webServerManual
        function sendToWebServerManual(speed) {
            command =
                "http://" +
                global.serverIp +
                ":" +
                global.port_manual +
                "/0*speed$" +
                speed +
                "*steer$0*limit$0*powerA$0*powerB$0*pulverize$0"
            new WebSocket(command);
        }
        return (
            <>
                <View style={styles.container}>

                    <TouchableOpacity style={styles.buttonTryConnection} onPress={() => {
                        this.setState({ speed:speed===0? 1 : 0})
                        sendToWebServerManual(this.state.speed)
                        }}>
                        <Text style={styles.buttonTryText}>Tentar conexão</Text>
                    </TouchableOpacity>
                    <View style={styles.buttonTryConnectionn} />

                    <TouchableOpacity style={styles.buttonTryConnection}
                        onPress={() => { this.props.navigation.navigate("Main"); }}>
                        <Text style={styles.buttonTryText}>OK</Text>
                    </TouchableOpacity>

                </View>
            </>
        );
    }
}