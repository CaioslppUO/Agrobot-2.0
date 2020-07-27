import { StyleSheet } from "react-native";
import { colors } from "../../styles";
export default StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.backgroundDefault,
    justifyContent: "space-around",
    alignItems: "center"
  },
  containerButtons: {
    flex: 1,
    backgroundColor: colors.backgroundDefault,
    justifyContent: "center",
    width: "100%",
    alignItems: "center"
  },
  buttonTryConnectionn: {
    backgroundColor: colors.backgroundDefault,
    width: "60%",
    height: "10%",
    borderRadius: 200,
    justifyContent: "center",
    alignItems: "center"
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
