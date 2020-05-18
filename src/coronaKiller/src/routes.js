import { createStackNavigator } from 'react-navigation';
import Main from './pages/Main';
import Config from './pages/Config';
import Automatic from './pages/Automatic';
import Menu from './pages/Menu';

export default createStackNavigator({
    Main,
    Config,
    Menu,
    Automatic
},
{
    navigationOptions: {
        headerStyle: {
            backgroundColor: "#02535c",
        },
        headerTintColor: "#FFF",
    }
})