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
      marginBottom: '16%',
      height: 120
  },
  firstBoxText: {
      fontSize: 20,
      borderRadius: 10,
      borderWidth: 1,
  },
  boxText: {
      marginTop: '3%',
      fontSize: 20,
      borderRadius: 10,
      borderWidth: 1,
  },
  saveView: {
      marginTop: '27%',
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
  parameters: {
      marginTop: '5%',
      fontSize: 30,
      marginLeft: '28%',
      color: '#596e9c',
      fontWeight: 'bold'
  },
  versionView: {
      marginLeft: '89%',
      marginTop: '29%'
    },
  versionText: {
    color: '#02535c',
    fontSize: 10
  },
});