import { StyleSheet } from "react-native";
import { colors } from "../../styles";

export default StyleSheet.create({
  mainContainer: {
    alignItems: "stretch"
  },
  joystickView: {
    justifyContent: "center",
    alignItems: "center",
    height: "47%"
  },
  buttonContactArea: {
    width: 30,
    height: 30,
    alignItems: "center",
    justifyContent: "center"
  },

  wrapperView: {
    backgroundColor: colors.backgroundDefault
  },
  handlerView: {
    backgroundColor: colors.internalJoystick
  },
  secondaryButtonContainer: {
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
    height: 50,
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
    justifyContent: "center"
  },
  incDecText: {
    fontSize: 35
  },
  topBarSliderView: {
    flex: 1,
    flexDirection: "row",
    justifyContent: "space-around",
    alignItems: "center"
  }
});
