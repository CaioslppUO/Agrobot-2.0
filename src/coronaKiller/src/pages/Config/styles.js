import { StyleSheet } from "react-native";
import { colors } from "../../styles";
export default StyleSheet.create({
  textInputContainer: {
    flexDirection: "column"
  },
  sliderContainer: {
    height: "8%",
    width: "100%",
    flexDirection: "column",
    marginTop: "3%",
    justifyContent: "center",
    alignContent: "center",
    alignItems: "center"
  },
  textSlider: {
    fontSize: 15
  },
  slider: {
    width: 320,
    height: "20%"
  },
  containerButtons: {
    width: 300,
    flexDirection: "row",
    justifyContent: "space-between"
  }
});
