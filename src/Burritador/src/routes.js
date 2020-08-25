import * as React from "react";

import { createDrawerNavigator } from "@react-navigation/drawer";
import { NavigationContainer } from "@react-navigation/native";

import Home from "./pages/Main";
import Connection from "./pages/Connection";
import ManualControlConfig from "./pages/Config";
import AutomaticControlConfig from "./pages/Automatic";

const Drawer = createDrawerNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Drawer.Navigator initialRouteName="Home">
        <Drawer.Screen name="Home" component={Home} />
        <Drawer.Screen name="Configurações" component={ManualControlConfig} />
        <Drawer.Screen name="Connection" component={Connection} />
        <Drawer.Screen name="Automatic" component={AutomaticControlConfig} />
      </Drawer.Navigator>
    </NavigationContainer>
  );
}
