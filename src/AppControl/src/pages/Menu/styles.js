import { StyleSheet } from 'react-native'

export default StyleSheet.create({
  mainContainer: {
    flex: 1,
    flexDirection: 'column',
    justifyContent: 'space-between',
    alignItems: 'center',

  },
  versionText: {
    color: '#02535c',
    justifyContent: 'flex-end',
    fontSize: 10
  },
  containerVersion:{
    width: '100%',
    justifyContent: 'flex-end',
    alignItems: 'flex-end'
  },
  buttonContainer: {
    flexDirection: 'column',
    justifyContent: 'flex-start',
    marginTop: 15,
    alignItems: 'center',
  },
  Button: {
    borderWidth: 1,
    textAlign: 'center',
    backgroundColor: '#89c5d6',
    borderRadius: 10,
    marginTop: 40,
    width: 300
  },
  buttonText: {
    fontSize: 35,
    textAlign: 'center',
    backgroundColor: '#89c5d6',
    borderRadius: 10
  },
});
