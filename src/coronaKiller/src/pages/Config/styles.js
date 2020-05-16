import { StyleSheet } from 'react-native'

export default StyleSheet.create({
    mainContainer: {
      backgroundColor: '#ffffff',
      flex: 1,
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'space-between' 
  },
  textInputContainer: {
      flexDirection: 'column',
      height: 120
  },
  textDefault: {
      marginTop: 10,
      fontSize: 25,
      borderRadius: 10,
      borderWidth: 1,
  },
  saveContainer: {
      height: 90,
      width: 150
  },
  saveText: {
      fontSize: 35,
      borderWidth: 1,
      backgroundColor: '#89c5d6',
      textAlign: 'center',
      borderRadius: 10
  },
  comunication: {
      fontSize: 30,
      color: '#596e9c',
      fontWeight: 'bold',
  },
  versionContainer: {
    alignItems:'flex-end',
    width: '100%'
  },
  versionText: {
  	color: '#02535c',
  	fontSize: 10
  },
});