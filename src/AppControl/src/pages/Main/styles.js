import { StyleSheet } from "react-native";

export default StyleSheet.create({
  menuButton: {
    alignItems: "flex-end"
  },
  joystickView: {
    justifyContent: "center",
    alignItems: "center",
    height: "45%"
  },
  area: {
    marginTop: 7,
    width: 25,
    height: 25,
    alignItems: "center",
    justifyContent: "center"
  },
  wrapperView: {
    backgroundColor: "#ffffff"
  },
  handlerView: {
    backgroundColor: "#3495EB"
  },
  mainContainer: {
    backgroundColor: "#ffffff",
    flex: 1,
    justifyContent: "space-around",
    alignContent: "center"
  },
  powerButtonsContainer: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "space-around"
  },
  containerButtons: {
    height: 150,
    justifyContent: "space-around"
  },
  ButtonText: {
    fontSize: 15,
    textAlign: "center",
    color: "#c90000"
  },
  sliderContainer: {
    height: 70,
    flexDirection: "column"
  },
  slider: {
    width: "100%",
    height: "20%",
    justifyContent: "flex-end",
    alignContent: "center"
  },
  speedText: {
    fontSize: 20,
    justifyContent: "center",
    marginLeft: "5%",
    margin: 5
  },
  sinalText: {
    fontSize: 35,
    margin: -7
  },
  topBarSliderView: {
    flex: 1,
    flexDirection: "row",
    justifyContent: "space-around"
  },
  logosView: {
    flexDirection: "row",
    justifyContent: "space-around",
    alignItems: "center",
    height: 60,
    width: "100%"
  },
  logoUnioeste: {
    // height: '50%',
    height: 40,
    width: 100
    // width: '25%',
  },
  logoPti: {
    height: 45,
    width: 100
  },
  logoLabiot: {
    height: 50,
    width: 50,
    marginBottom: 10
  },
  logoItaipu: {
    height: 40,
    width: 50
  },
  versionText: {
    color: "#02535c",
    fontSize: 10
  },
  containerLogoVersion: {
    justifyContent: "space-around",
    alignItems: "flex-end",
    flexDirection: "column",
    height: 70,
    marginBottom: 5
  }
});
