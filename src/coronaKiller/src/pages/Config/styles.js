import { StyleSheet } from 'react-native'

export default StyleSheet.create({
    mainContainer: {
      backgroundColor: '#ffffff',
      flex: 1,
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'space-between' ,
  },
  textInputContainer: {
      flexDirection: 'column',
			height: 550,
			alignItems: 'center',
  },
  textDefault: {
			alignItems: 'flex-start',
      marginTop: 10,
      fontSize: 25,
      borderRadius: 10,
			borderWidth: 1,
			width: 310
  },
  saveContainer: {
			marginTop: 150,
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
      marginTop: 50
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