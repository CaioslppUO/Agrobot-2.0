import { createStackNavigator } from "react-navigation";
import Main from "./pages/Main";
import Config from "./pages/Config";
import Automatic from "./pages/Automatic";
import Connection from './pages/Connection'

export default createStackNavigator(
  {
    Main,
    Config,
    Automatic,
    Connection
  },
  {
    navigationOptions: {
      headerStyle: {
        backgroundColor: "#02535c"
      },
      headerTintColor: "#FFF"
    }
  }
);
