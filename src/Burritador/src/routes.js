import * as React from 'react';
import {Button, View} from 'react-native';
import {createDrawerNavigator} from '@react-navigation/drawer';
import {NavigationContainer} from '@react-navigation/native';

import Home from './pages/Main';
import Connection from './pages/Connection';
import ManualControlConfig from './pages/Config';
import AutomaticControlConfig from './pages/Automatic';

const Stack = createDrawerNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={Home} />
        <Stack.Screen name="Configuracoes" component={ManualControlConfig} />
        <Stack.Screen name="Connection" component={Connection} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
