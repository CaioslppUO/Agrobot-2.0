import { StyleSheet } from 'react-native'

export default StyleSheet.create({
  menuButton: {
    alignItems:'flex-end'
  },
  joystickView: {
    alignItems: 'center',
    padding: 10,
    height: 260
  },
  area: {
    marginTop: 7,
    width: 25,
    height: 25,
    alignItems: 'center',
    justifyContent: 'center'
  },
  wrapperView: {
    backgroundColor: '#ffffff'
  },
  handlerView: {
    backgroundColor: '#3495EB'
  },
  mainContainer: {
    backgroundColor: '#ffffff',
    flex: 1,
    justifyContent: 'space-around'
  },
  powerButtonsContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-around',
  },
  containerButtons: {
    height: 120
  },
  ButtonText: {
    fontSize: 15,
    textAlign: 'center',
    color: '#c90000'
  },
  sliderContainer: {
    height: 70,
    flexDirection: 'column',
  },
  slider: {
    transform: [{ scaleX: 2.0 }, { scaleY: 2.0 }],
    marginLeft: '22%',
    marginRight: '23%',
    justifyContent: 'flex-end'
  },
  speedText: {
    fontSize: 20,
    justifyContent: 'center',
    marginLeft: '5%',
    margin: 5
  },
  sinalText: {
    fontSize: 35,
    margin: -7
  },
  topBarSliderView: {
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'space-around'
  },
  logosView: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    alignItems: 'center',
    height: 90,
    width: '100%',
  },
  logoUnioeste: {
    // height: '50%',
    height: 40,
    width: 100,
    // width: '25%',
  },
  logoPti: {
    height: 45,
    width: 100,
  },
  logoLabiot: {
    height: 50,
    width: 50,
    marginBottom: 10,
  },
  logoItaipu: {
    height: 40,
    width: 50,
  },
  versionText: {
    color: '#02535c',
    fontSize: 10,
  },
  containerLogoVersion: {
    justifyContent: 'space-around',
    alignItems: 'flex-end',
    flexDirection: 'column',
    height: 100,
  }
});