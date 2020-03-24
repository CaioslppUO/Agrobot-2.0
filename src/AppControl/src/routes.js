import { createStackNavigator } from 'react-navigation';
import Main from './pages/main';
import Config from './pages/config';
import Debug from './pages/debug';
import Menu from './pages/menu';

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