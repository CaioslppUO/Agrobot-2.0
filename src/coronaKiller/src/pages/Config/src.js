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
            if(typeof parseInt(splittedIp[piece]) != "number" || Number.isNaN(parseInt(parseInt(splittedIp[piece])))){
                throw new Error("IP inválido.")
            }
            if(parseInt(splittedIp[piece]) < 0){
                throw new Error("IP inválido.")
            }
        }
    },
    checkPort: function(port){
        if(typeof parseInt(port) != "number" || Number.isNaN(parseInt(port)) ||parseInt(port) < 0 ){
            throw new Error("Porta inválida.")
        }
    },
    checkDelay: function(delay){
        if(typeof parseInt(delay) != "number" || Number.isNaN(parseInt(delay)) || parseInt(delay) < 0){
            throw new Error("Delay inválido.")
        }
    }
}