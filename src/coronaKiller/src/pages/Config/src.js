export default Src = {
    checkIp: function(ip){
        let splittedIp = ip.split(".")
        if(ip.split(".").length != 4){
            throw new Error("IP inválido.")
        }
        if(ip === "127.0.0.1" || ip === "localhost"){
            throw new Error("IP inválido.")
        }
        for(let piece in splittedIp){
            if(splittedIp[piece].length < 1 || splittedIp[piece].length > 3){
                throw new Error("IP inválido.")
            }
        }
    },
    checkPort: function(port){
        if(typeof parseInt(port) != "number"){
            throw new Error("Porta inválida.")
        }
    },
    checkDelay: function(delay){
        if(typeof parseInt(delay) != "number"){
            throw new Error("Delay inválido.")
        }
    }
}