import { StyleSheet } from "react-native";

export default StyleSheet.create({
  mainContainer: {
    backgroundColor: "#ffffff",
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
  containerCommunication: {},
  saveText: {
    fontSize: 35,
    borderWidth: 1,
    backgroundColor: "#89c5d6",
    textAlign: "center",
    borderRadius: 10
  },
  comunication: {
    fontSize: 30,
    color: "#596e9c",
    fontWeight: "bold"
  },
  versionContainer: {
    alignItems: "flex-end",
    width: "100%"
  },
  versionText: {
    color: "#02535c",
    fontSize: 10
  }
});
