import { StyleSheet } from "react-native";


export default StyleSheet.create({
    container:{
        flex:1,
        backgroundColor: "#fff",
        justifyContent: 'space-around',
        alignItems: 'center',
    },
    containerButtons:{
        flex:1,
        backgroundColor: "#fff",
        justifyContent: 'center',
        width: '100%',
        alignItems: 'center',
    },
    buttonTryConnectionn:{
        backgroundColor: "#fff",
        width: '60%',
        height: "10%",
        borderRadius: 150,
        justifyContent: 'center',
        alignItems: 'center'
    },
    buttonTryConnection: {
        backgroundColor: "#3495E9",
        width: '60%',
        height: "20%",
        borderRadius: 150,
        justifyContent: 'center',
        alignItems: 'center'
    },
    buttonTryText:{
        fontWeight: "bold",
        fontSize: 20,
        color: '#fff',

    },
    containerTutorial:{
        width: '80%',
        alignItems: 'flex-start',
    },
    tutorialText:{
        fontSize: 20,
        paddingBottom: '2%',
        textAlign: 'left'
    },
    logosView: {
        flexDirection: "row",
        justifyContent: "space-around",
        alignItems: "center",
        height: 90,
        width: "100%"
    },
    logoUnioeste: {
        // height: '50%',
        height: 40,
        width: 100
        // width: '25%',
    },
    logoPti: {
        height: 45,
        width: 100
    },
    logoLabiot: {
        height: 50,
        width: 50,
        marginBottom: 10
    },
    logoItaipu: {
        height: 40,
        width: 50
    },
    versionText: {
        color: "#02535c",
        fontSize: 10,
    },
    containerLogoVersion: {
        justifyContent: "space-around",
        alignItems: "flex-end",
        flexDirection: "column",
        height: 100,
        width: '100%'
    }
});