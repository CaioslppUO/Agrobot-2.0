import React,{Component} from 'react';
import { View,Text,StyleSheet,TouchableOpacity,BackHandler } from 'react-native';

export default class Menu extends Component {
    //Opções do controlador de navegação de páginas 
    static navigationOptions =  {
        title: "Menu",
        headerTitleStyle: {
            flexGrow: 1,
            marginLeft: '35%'
        }
    };

    componentWillMount() {
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
                        <Text style={styles.buttonText}>Control</Text>
                    </TouchableOpacity>

                    {/*Botão do menu de configuração*/}
                    <TouchableOpacity
                    style={styles.menuButton}
                    onPress={() => {this.props.navigation.navigate('Config')}}>
                        <Text style={styles.buttonText}>Config</Text>
                    </TouchableOpacity>

                    {/*Botão de debug*/}
                    <TouchableOpacity
                    style={styles.menuButton}
                    onPress={() => {this.props.navigation.navigate('Debug')}}>
                        <Text style={styles.buttonText}>Debug</Text>
                    </TouchableOpacity>

                    {/*Botão de sair*/}
                    <TouchableOpacity
                    style={styles.exitButton}
                    onPress={() => {
                        BackHandler.exitApp()
                    }}>
                        <Text style={styles.buttonText}>Exit</Text>
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
        flex: 1
    },
    buttonsView: {
        marginLeft: '34%',
        marginTop: '15%',
        marginRight: '30%',
    },
    versionView: {
        marginLeft: '89%',
        marginTop: '13%'
      },
      versionText: {
        color: '#02535c',
        fontSize: 10
      },
      menuButton: {
        fontSize: 35,
        borderWidth: 1,
        textAlign: 'center',
        backgroundColor: '#89c5d6',
        borderRadius: 10,
        marginTop: '40%'
      },
      buttonText: {
        fontSize: 35,
        borderWidth: 1,
        textAlign: 'center',
        backgroundColor: '#89c5d6',
        borderRadius: 10
      },
      exitButton: {
        fontSize: 35,
        borderWidth: 1,
        textAlign: 'center',
        backgroundColor: '#89c5d6',
        borderRadius: 10,
        marginTop: '150%'
      }
});