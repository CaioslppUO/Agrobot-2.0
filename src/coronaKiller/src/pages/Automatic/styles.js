import { StyleSheet } from "react-native";

export default StyleSheet.create({
  mainContainer: {
    flex: 1,
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "space-between"
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
    backgroundColor: "#89c5d6",
    textAlign: "center",
    borderRadius: 10
  },
  parameters: {
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
