import React from 'react';
import {View, Text} from 'react-native';
import AxisPad from 'react-native-axis-pad';

const App = () => {
  return (
    <>
      <View>
        <Text>ola mundo</Text>
        <AxisPad
          size={300}
          handlerSize={200}
          // handlerStyle={Styles.handlerView}
          // wrapperStyle={Styles.wrapperView}
          autoCenter={false}
          resetOnRelease={true}
          onValue={({x, y}) => {
            console.log(x, y);
          }}
        />
      </View>
    </>
  );
};

export default App;
