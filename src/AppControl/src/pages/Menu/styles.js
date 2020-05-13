import { StyleSheet } from 'react-native'

export default StyleSheet.create({
  mainView: {
      backgroundColor: '#ffffff',
      flex: 1,
      flexDirection: 'column',
      // justifyContent: 'space-between',
      alignItems: 'center',

  },
  buttonsView: {
      justifyContent: 'space-between',
      width: 150,
  },
  versionView: {
      marginLeft: '89%',
      marginTop: '13%'
    },
  versionText: {
    color: '#02535c',
    fontSize: 10
  },
  menuButton: {
    fontSize: 30,
    borderWidth: 1,
    textAlign: 'center',
    backgroundColor: '#89c5d6',
    borderRadius: 10,
    marginTop: '40%'
  },
  buttonText: {
    fontSize: 35,
    borderWidth: 1,
    textAlign: 'center',
    backgroundColor: '#89c5d6',
    borderRadius: 10
  },
  exitButton: {
    fontSize: 35,
    borderWidth: 1,
    textAlign: 'center',
    backgroundColor: '#89c5d6',
    borderRadius: 10,
    marginTop: '120%'
  }
});
