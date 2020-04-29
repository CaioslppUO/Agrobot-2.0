# Configuração necessaria em node_modules

  ##### Ir para o diretório 
  
  ```
  YOUR_PROJECT_PATH/node_modules/react-native-safe-area-view/index.js
  ```
  ##### e substituir:
  ```
  this.view._component.measureInWindow((winX, winY, winWidth, winHeight) => {
  ```  
  ##### por:
  ```
  this.view.getNode().measureInWindow((winX, winY, winWidth, winHeight) => {
  ```
