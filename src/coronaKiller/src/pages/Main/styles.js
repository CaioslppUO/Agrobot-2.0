import { StyleSheet } from "react-native";
import { colors } from "../../styles";

export default StyleSheet.create({
  menuButton: {
    alignItems: "flex-end"
  },
  joystickView: {
    justifyContent: "center",
    alignItems: "center",
    height: "47%"
  },
  incDecArea: {
    marginTop: 7,
    width: 35,
    height: 35,
    alignItems: "center",
    justifyContent: "center"
  },

  wrapperView: {
    backgroundColor: colors.backgroudDefault
  },
  handlerView: {
    backgroundColor: colors.internalJoystick
  },
  mainContainer: {
    backgroundColor: colors.backgroudDefault,
    flex: 1,
    justifyContent: "space-around"
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
  stopButtonText: {
    fontSize: 15,
    textAlign: "center",
    color: colors.buttonRed
  },
  stopButton: {
    borderColor: colors.buttonRed,
    borderRadius: 115,
    height: 62,
    width: 200,
    borderWidth: 3,
    alignItems: "center",
    justifyContent: "center"
  },
  picker: {
    height: 30,
    width: 150
  },
  actionButton: {
    borderRadius: 180,
    height: 70,
    borderWidth: 1,
    width: 70,
    alignItems: "center",
    justifyContent: "center"
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
  incDecText: {
    fontSize: 35,
    margin: -7
  },
  topBarSliderView: {
    flex: 1,
    flexDirection: "row",
    justifyContent: "space-around"
  }
});
