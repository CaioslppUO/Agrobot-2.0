import { StyleSheet } from "react-native";
import { colors } from "../../styles";
export default StyleSheet.create({
  mainContainer: {
    backgroundColor: colors.backgroundDefault,
    flex: 1,
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "space-between"
  },
  textInputContainer: {
    flexDirection: "column",
    alignItems: "center"
  },
  inputText: {
    alignItems: "flex-start",
    marginTop: 10,
    fontSize: 20,
    borderRadius: 10,
    borderWidth: 1,
    width: 310
  },
  saveContainer: {
    height: 90,
    width: 150
  },
  saveText: {
    fontSize: 35,
    borderWidth: 1,
    backgroundColor: colors.buttonBlue,
    textAlign: "center",
    borderRadius: 10
  },
  communication: {
    fontSize: 30,
    color: colors.title,
    fontWeight: "bold"
  }
});
