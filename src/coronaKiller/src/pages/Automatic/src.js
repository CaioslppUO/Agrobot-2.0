export default class Src{
    // Guarda as variáveis de configuração na memória.
    storeData = async (name, value) => {
        try {
          await AsyncStorage.setItem(name, value);
        } catch (error) {
          alert("Erro ao salvar a variável " + name + ". Erro: " + error);
        }
      };
}