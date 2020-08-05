import { StyleSheet } from "react-native";
import { colors } from "../../styles";
export default StyleSheet.create({
  containerButtons: {
    flex: 1,
    backgroundColor: colors.backgroundDefault,
    justifyContent: "center",
    width: "100%",
    alignItems: "center"
  },
  spacing: {
    backgroundColor: colors.backgroundDefault,
    height: "10%"
  },
  buttonTryConnection: {
    backgroundColor: colors.internalJoystick,
    width: "60%",
    height: "20%",
    borderRadius: 200,
    justifyContent: "center",
    alignItems: "center"
  },
  buttonTryText: {
    fontWeight: "bold",
    fontSize: 20,
    color: colors.backgroundDefault
  },
  containerTutorial: {
    width: "80%",
    alignItems: "flex-start"
  },
  tutorialText: {
    fontSize: 20,
    paddingBottom: "2%",
    textAlign: "left"
  }
});
