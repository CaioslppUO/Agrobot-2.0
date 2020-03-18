import { createStackNavigator } from 'react-navigation';
import Main from './pages/main';
import Config from './pages/config';
import Debug from './pages/debug';

export default createStackNavigator({
    Main,
},{
    navigationOptions: {
        headerStyle: {
            backgroundColor: "#3495EB",
        },
        headerTintColor: "#FFF",
        headerTitleStyle: {
            textAlign: 'center',
            alignSelf: 'center',
            flexGrow: 1
        }
    }
})