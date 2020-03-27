import { createStackNavigator } from 'react-navigation';
import Main from './pages/Main';
import Config from './pages/Config';
import Debug from './pages/Debug';
import Menu from './pages/Menu';

export default createStackNavigator({
    Main,
    Config,
    Menu,
    Debug
},
{
    navigationOptions: {
        headerStyle: {
            backgroundColor: "#02535c",
        },
        headerTintColor: "#FFF",
    }
})