import { StyleSheet } from 'react-native'

export default StyleSheet.create({
  menuButtonView: {
    marginLeft: '87%'
  },
  joystickView: {
    marginTop: "15%",
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
  },
  wrapperView: {
    backgroundColor: '#ffffff'
  },
  handlerView: {
    backgroundColor: '#3495EB'
  },
  mainView: {
    backgroundColor: '#ffffff',
    flex: 1,
    justifyContent: 'space-between'
  },
  powerButtonsView: {
    flexDirection: 'row',
    marginTop: '10%',
    marginBottom: '5%'
  },
  powerButtonText: {
    textAlign: 'center',
    padding: 8
  },
  uvButtonText: {
    textAlign: 'center',
    marginTop: '8%'
  },
  automaticButtonText: {
    textAlign: 'center',
    marginTop: '2%'
  },
  stopButtonText: {
    textAlign: 'center',
    marginTop: '10%'
  },
  buttonMenu: {
    height: 40,
    width: 50,
  },
  menuButtonText: {
    textAlign: 'center',
    marginTop: '7%'
  },
  sliderView: {
    width: '100%',
    height: 65,
    justifyContent: 'center',
    flexDirection: 'column',
  },
  backgroundsliderText: {
    width: 40,
    flexDirection: 'row'
  },
  slider: {
    transform: [{ scaleX: 2.0 }, { scaleY: 2.0 }],
    marginLeft: '22%',
    marginRight: '23%',
    justifyContent: 'flex-end'
  },
  changeSpeedButtonLess: {
    justifyContent: 'flex-end'
  },
  speedText: {
    fontSize: 20,
    justifyContent: 'center',
    marginLeft: '5%',
    margin: 5
  },
  lessButtonText: {
    fontSize: 35,
    height: 50,
    width: 40,
    marginLeft: 10,
    margin: -5
  },
  moreButtonText: {
    fontSize: 35,
    height: 50,
    width: 50,
    marginLeft: 10,
    margin: -3
  },
  topBarSliderView: {
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'space-between'
  },
  logosView: {
    flexDirection: 'row',
    flex: 1,
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  logoUnioeste: {
    marginLeft: 10,
  },
  logoPti: {
    height: 50,
    width: 110,
  },
  logoLabiot: {
    height: 70,
    width: 70,
    marginBottom: 10,
  },
  versionView: {
    alignContent: 'flex-end'
  },
  versionText: {
    color: '#02535c',
    fontSize: 10,
  },
  containerLogoVersion: {
    justifyContent: 'space-between',
    alignItems: 'flex-end',
    flexDirection: 'row',
    height: 110,
  }
});