import { StyleSheet } from "react-native";
import { colors } from "../../styles";
export default StyleSheet.create({
  mainContainer: {
    flex: 1,
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "space-between",
    backgroundColor: colors.backgroundDefault
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
  containerButtons: {
    width: 300,
    flexDirection: "row",
    justifyContent: "space-between"
  },
  sliderContainer: {
    height: 50,
    width: 300,
    flexDirection: "column",
    marginTop: "3%",
    justifyContent: "center",
    alignContent: "center",
    alignItems: "center",
  },
  textSlider: {
    fontSize: 15,
  },
  slider: {
    width: 300,
    // height: "10%",
  },
  topBarSliderView: {
    flex: 1,
    flexDirection: "row",
    // justifyContent:
  },
  parameters: {
    fontSize: 30,
    color: colors.title,
    fontWeight: "bold"
  }
});
