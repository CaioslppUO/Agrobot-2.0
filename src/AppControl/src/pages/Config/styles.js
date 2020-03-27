import { StyleSheet } from 'react-native'

export default StyleSheet.create({
  mainView: {
      backgroundColor: '#ffffff',
      flex: 1,
  },
  boxesView: {
      flexDirection: 'column',
      marginLeft: '20%',
      marginTop: '5%',
      marginRight: '22%',
      height: 120
  },
  ipText: {
      fontSize: 30,
      borderRadius: 10,
      borderWidth: 1,
  },
  portText: {
      marginTop: '5%',
      fontSize: 30,
      borderRadius: 10,
      borderWidth: 1,
  },
  saveView: {
      marginTop: '20%',
      marginLeft: '35%',
      marginRight: '35%',
      height: 90
  },
  saveText: {
      fontSize: 35,
      borderWidth: 1,
      backgroundColor: '#89c5d6',
      textAlign: 'center',
      borderRadius: 10
  },
  comunication: {
      marginTop: '5%',
      fontSize: 30,
      marginLeft: '28%',
      color: '#596e9c',
      fontWeight: 'bold'
  },
  control: {
      marginTop: '10%',
      fontSize: 30,
      marginLeft: '37%',
      color: '#596e9c',
      fontWeight: 'bold'
  },
  minPSpeedText: {
      fontSize: 20,
      borderRadius: 10,
      borderWidth: 1,
  },
  versionView: {
      marginLeft: '89%',
      marginTop: '29%'
    },
  versionText: {
    color: '#02535c',
    fontSize: 10
  }
});