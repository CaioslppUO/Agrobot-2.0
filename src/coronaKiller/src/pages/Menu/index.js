import React,{Component} from 'react';
import { View,Text,TouchableOpacity,BackHandler } from 'react-native';

import styles from './styles';

export default class Menu extends Component {
    //Opções do controlador de navegação de páginas 
    static navigationOptions =  {
        title: "Menu",
        headerTitleStyle: {
            flexGrow: 1,
            marginLeft: '35%'
        }
    };

    UNSAFE_componentWillMount() {
        BackHandler.addEventListener('hardwareBackPress', this.backPressed);
    }

    componentWillUnmount(){
        BackHandler.removeEventListener('hardwareBackPress', this.backPressed)
    }

    render(){
        return (
            <>
            {/*View principal*/}
            <View style={styles.mainView}>

                {/*View dos botões*/}
                <View style={styles.buttonsView}>
                    {/*Botão do controle manual*/}
                    <TouchableOpacity
                    style={styles.menuButton}
                    onPress={() => {this.props.navigation.navigate('Main')}}>
                        <Text style={styles.buttonText}>Controle</Text>
                    </TouchableOpacity>

                    {/*Botão do menu de configuração*/}
                    <TouchableOpacity
                    style={styles.menuButton}
                    onPress={() => {this.props.navigation.navigate('Config')}}>
                        <Text style={styles.buttonText}>Configuração</Text>
                    </TouchableOpacity>

                    {/*Botão de debug*/}
                    <TouchableOpacity
                    style={styles.menuButton}
                    onPress={() => {this.props.navigation.navigate('Automatic')}}>
                        <Text style={styles.buttonText}>Configuração Modo Automático</Text>
                    </TouchableOpacity>

                    {/*Botão de sair*/}
                    <TouchableOpacity
                    style={styles.exitButton}
                    onPress={() => {
                        BackHandler.exitApp()
                    }}>
                        <Text style={styles.buttonText}>Sair</Text>
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

