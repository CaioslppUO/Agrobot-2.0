import { StyleSheet } from "react-native";
import { colors } from "../../styles";
export default StyleSheet.create({
  mainContainer: {
    flex: 1,
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "space-between",
    backgroundColor: colors.backgroudDefault
  },
  boxesContainer: {
    flexDirection: "column",
    width: 300
  },
  boxText: {
    marginTop: "3%",
    fontSize: 15,
    borderRadius: 10,
    borderWidth: 1
  },
  saveButton: {
    marginTop: "3%",
    alignContent: "center",
    width: 200,
    height: 90
  },
  saveText: {
    fontSize: 30,
    borderWidth: 1,
    backgroundColor: colors.buttonBlue,
    textAlign: "center",
    borderRadius: 10
  },
  parameters: {
    fontSize: 30,
    color: colors.title,
    fontWeight: "bold"
  }
});
