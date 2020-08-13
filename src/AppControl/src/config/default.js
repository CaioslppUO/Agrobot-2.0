export default DefaultConfig = {
  // Controle global.
  speed: function () {
    return 0
  },
  steer: function () {
    return 0
  },
  limit: function () {
    return 50
  },
  minPulverizeSpeed: function() {
    return 20
  },
  sliderSensibility: function () {
    return 50
  },

  // Energia(liga/desliga).
  power: function () {
    return 0
  },
  pulverize: function () {
    return 0
  },

  // Comunicação.
  roscoreServerIp: function () {
    return "192.168.1.2"
  },
  lidarServerIp: function () {
    return "192.168.1.121"
  },
  roscoreServerPort: function () {
    return "8080"
  },
  lidarServerPort: function () {
    return "8082"
  },

  // Controle de comunicação.
  communicationDelay: function () {
    return 50
  },
  communicationInterval: function () {
    return 0
  },

  // Controle automático.
  speedAuto: function () {
    return -26
  },
  steerAuto: function () {
    return -2
  },
  limitAuto: function () {
    return 50
  },

  correctionMovements: function () {
    return 5
  },
  correctionFactor: function () {
    return 15
  },
  moveTime: function () {
    return 0
  },
  stopTime: function () {
    return 0
  },
  detectDistance: function () {
    return 1.5
  }
}
