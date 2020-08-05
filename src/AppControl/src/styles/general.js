import { StyleSheet } from "react-native";
import colors from "./colors";

export default StyleSheet.create({
  mainContainer: {
    flex: 1,
    alignItems: "center",
    flexDirection: "column",
    justifyContent: "space-between",
    backgroundColor: colors.backgroundDefault
  },
  title: {
    fontSize: 30,
    color: colors.title,
    fontWeight: "bold"
  },
  button: {
    marginTop: "3%",
    alignContent: "center",
    width: 140,
    height: 90
  },
  textButtons: {
    fontSize: 25,
    borderWidth: 1,
    backgroundColor: colors.buttonBlue,
    textAlign: "center",
    borderRadius: 10
  },
  inputText: {
    marginTop: "3%",
    fontSize: 15,
    borderRadius: 10,
    borderWidth: 1,
    width: 310
  }
});
