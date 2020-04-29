import { createStackNavigator } from 'react-navigation';
import Mapa from './pages/Mapa';

export default createStackNavigator({
    Mapa,
},
{
    navigationOptions: {
        headerStyle: {
            backgroundColor: "#02535c",
        },
        headerTintColor: "#FFF",
    }
})