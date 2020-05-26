import { createStackNavigator } from "react-navigation";
import Main from "./pages/Main";
import Config from "./pages/Config";
import Automatic from "./pages/Automatic";

export default createStackNavigator(
  {
    Main,
    Config,
    Automatic
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
