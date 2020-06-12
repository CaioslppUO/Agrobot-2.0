#!//usr/bin/env python
#coding: utf-8
import os
import time
import subprocess

wifiName = "Agrobot4"
wifiPassword = "rapisbere"
gitRepo = "https://github.com/CaioslppUO/Agrobot-2.0"
lidarRepo = "https://github.com/robopeak/rplidar_ros"
user = "$USER"

gpioOk = False
i2cOk = False
sshOk = False
lidarOk = False
repoOk = False
updtOk = False
portsOk = False
autoStartRobot = False
accesPOk = False

cleanFile = "w"
insertFile = "a"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printOk(msg):
    run("clear")
    print(bcolors.OKGREEN + msg + " " + " OK " + bcolors.ENDC)
    time.sleep(1)
    run("clear")

def run(command):
    subprocess.call(command,shell=True,executable='/bin/bash')

def writeFile(filePath,msg,overWrite):
    file = open(filePath, overWrite)
    file.writelines(msg)
    file.close()

def installLidar():
    global lidarRepo
    print(bcolors.OKGREEN + 'Instalando a biblioteca de ROS para o RPLidar' + bcolors.ENDC)
    command = "cd ~/catkin_ws/src && sudo -u labiot git clone " + lidarRepo
    run(command)
    print(bcolors.WARNING +  "********************************************************************************************************************************************" + bcolors.ENDC)
    print(bcolors.WARNING +  'Para terminar a instalação entre no diretório: ~/catkin_ws e digite o comando: catkin_make -j 1 e após o comando ser executado, aperte ctrl+d' + bcolors.ENDC)
    print(bcolors.WARNING +  "********************************************************************************************************************************************" + bcolors.ENDC)
    command = "sudo -u labiot -s"
    run(command)
    run("clear")
    printOk("Instalação do Lidar")

def newAccessPoint():
    print(bcolors.OKGREEN + "Toranando o RaspBerry em um Access Point" + bcolors.ENDC)

    command = "sudo apt-get install -y dnsmasq hostapd dhcpcd5"
    run(command)
    command = "sudo systemctl stop hostapd"
    run(command)
    command = "sudo systemctl stop dnsmasq"
    run(command)

    fileContent = list()

    writeFile("denyinterfaces wlan0\n","/etc/dhcpcd.conf",insertFile)

    fileContent.append("\nallow-hotplug wlan0\n")
    fileContent.append("iface wlan0 inet static\n")
    fileContent.append("address 192.168.1.2\n")
    fileContent.append("netmask 255.255.255.0\n")
    fileContent.append("network 192.168.1.1\n")
    fileContent.append("broadcast 192.168.1.255\n")
    writeFile(fileContent,"/etc/network/interfaces",cleanFile)
    fileContent.clear()
    
    fileContent.append("interface=wlan0\n")
    fileContent.append("driver=nl80211\n")
    fileContent.append("ssid="+wifiName+"\n")
    fileContent.append("hw_mode=g\n")
    fileContent.append("channel=6\n")
    fileContent.append("macaddr_acl=0\n")
    fileContent.append("auth_algs=1\n")
    fileContent.append("ignore_broadcast_ssid=0\n")
    fileContent.append("wpa=2\n")
    fileContent.append("wpa_passphrase="+wifiPassword+"\n")
    fileContent.append("wpa_key_mgmt=WPA-PSK\n")
    fileContent.append("rsn_pairwise=CCMP\n")
    writeFile(fileContent,"/etc/hostapd/hostapd.conf",cleanFile)
    fileContent.clear()

    fileContent.append("\nDAEMON_CONF='/etc/hostapd/hostapd.conf'\n")
    writeFile(fileContent,"/etc/default/hostapd",insertFile)
    fileContent.clear()

    fileContent.append("interface=wlan0\n")
    fileContent.append("listen-address=192.168.1.2\n")
    fileContent.append("bind-interfaces\n")
    fileContent.append("server=8.8.8.8\n")
    fileContent.append("domain-needed\n")
    fileContent.append("bogus-priv\n")
    fileContent.append("dhcp-range=192.168.1.120,192.168.1.254,12h\n")
    writeFile(fileContent,"/etc/dnsmasq.conf",cleanFile)
    fileContent.clear()

    fileContent.append("\nnet.ipv4.ip_forward=1")
    writeFile(fileContent,"/etc/sysctl.conf",insertFile)
    fileContent.clear()

    command = "sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE"
    run(command)
    command = "sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT"
    run(command)
    command = "sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT"
    run(command)
    command = "sudo sh -c 'iptables-save > /etc/iptables.ipv4.nat'"
    run(command)

    fileContent.append("\niptables-restore < /etc/iptables.ipv4.nat")
    fileContent.append("\n/usr/sbin/hostapd /etc/hostapd/hostapd.conf")
    writeFile(fileContent,"/usr/bin/resetssh.sh",insertFile)
    fileContent.clear()

    command = "sudo apt-get install ponte-utils"
    run(command)
    command = "sudo brctl addbr br0"
    run(command)
    command = "sudo brctl addif br0 eth0"
    run(command)
    
    run("clear")
    printOk("Access Point")

def updateSystem():
    print(bcolors.OKGREEN + "Inicializando o update e upgrade de sistema" + bcolors.ENDC)
    command = "sudo apt update"
    run(command)
    command = "sudo apt autoremove -y && sudo apt upgrade -y"
    run(command)
    command = "sudo apt-get install vim"
    run(command)
    run("clear")
    printOk("Update de sistema")

def installGPIO():
    print(bcolors.OKGREEN + "Instalando e configurando o GPIO" + bcolors.ENDC)
    command = "sudo apt-get install -y rpi.gpio"
    run(command)
    run("clear")
    printOk("Instalação do GPIO")

def installI2C():
    print(bcolors.OKGREEN + "Instalando e configurando o I2C" + bcolors.ENDC)
    run("sudo raspi-config")
    fileContent = list()
    
    fileContent.append("i2c-bcm2835")
    fileContent.append("i2c-dev")
    writeFile(fileContent,"/dev/modules",insertFile)
    fileContent.clear()

    writeFile("dtparam=i2c1=on","/boot/config.txt",insertFile)
    
    command = "sudo apt-get install -y python-smbus i2c-tools"
    run(command)
    run("clear")
    printOk("Instalação do I2C")

def addUserSerialPorts():
    run("sudo usermod -a -G dialout " + user)

def installandConfigureSSH():
    print(bcolors.OKGREEN + "Instalando e configurando o SSH" + bcolors.ENDC)
    command = "sudo apt-get install -y openssh*"
    run(command)

    fileContent = list()

    writeFile("service ssh restart","/usr/bin/resetssh.sh",cleanFile)

    command = "sudo chmod +x /usr/bin/resetssh.sh"
    run(command)

    fileContent.append("[Unit]\n")
    fileContent.append("Description=Starts ssh\n")
    fileContent.append("\n")
    fileContent.append("[Service]\n")
    fileContent.append("Type=simple\n")
    fileContent.append("ExecStart=/bin/bash /usr/bin/resetssh.sh\n")
    fileContent.append("\n")
    fileContent.append("[Install]\n")
    fileContent.append("WantedBy=multi-user.target\n")
    writeFile(fileContent,"/etc/systemd/system/restartssh.service",cleanFile)
    fileContent.clear()

    command = "sudo chmod 644 /etc/systemd/system/restartssh.service"
    run(command)
    command = "sudo systemctl start restartssh"
    run(command)
    command = "sudo systemctl enable restartssh"
    run(command)
    command = "sudo ufw allow 22"
    run(command)
    command = "sudo dpkg-reconfigure openssh-server"
    run(command)
    run("clear")
    printOk("Instalação do SSH")

def downloadRepo():
    global gitRepo
    print(bcolors.OKGREEN + "Iniciando o download do repositiório remoto do robô" + bcolors.ENDC)
    command = "sudo apt install git"
    run(command)
    command = "git clone " + gitRepo
    run(command)
    command = "cd Agrobot-2.0 && git checkout raspberry-ros-stable && clear"
    run(command)
    run("clear")
    printOk("Download do repositório")

def setVerifiedColor(var):
    if(var == True):
        return bcolors.OKBLUE + "OK" + bcolors.ENDC
    else:
        return bcolors.FAIL + "NO" + bcolors.ENDC

def fixBugs():
    command = "sudo echo 'linux-firmware-raspi2 hold' | sudo dpkg --set-selections"
    run(command)

def setAutoStartRobotCore():
    print(bcolors.OKGREEN + "Configurando a inicialização automática do robô" + bcolors.ENDC)

    writeFile("source /opt/ros/melodic/setup.bash && /home/labiot/Agrobot-2.0/src/raspberryRos/runnables/./run_ROBOT.sh","/usr/bin/autoStartRobotCore.sh",cleanFile)
    command = "sudo chmod +x /usr/bin/autoStartRobotCore.sh"
    run(command)

    fileContent = list()
    
    fileContent.append("[Unit]")
    fileContent.append("Description=Starts ssh")
    fileContent.append("")
    fileContent.append("[Service]")
    fileContent.append("Type=simple")
    fileContent.append("ExecStart=/bin/bash /usr/bin/autoStartRobotCore.sh")
    fileContent.append("")
    fileContent.append("[Install]")
    fileContent.append("WantedBy=multi-user.target")
    writeFile(fileContent,"/usr/bin/autoStartRobotCore.sh",cleanFile)
    fileContent.clear()

    command = "sudo chmod 644 /etc/systemd/system/autoStartRobotCore.service"
    run(command)
    command = "sudo systemctl enable autoStartRobotCore"
    run(command)
    run("clear")
    printOk("Configuração da inicialização automática do robô")

def log():
    global gpioOk,i2cOk,sshOk,lidarOk,repoOk,updtOk,portsOk,autoStartRobot,accesPOk
    run("clear")
    print(bcolors.OKGREEN + 'Resumo da instalação: ' + bcolors.ENDC)
    print('UpdateSystem: ' + setVerifiedColor(updtOk))
    print('SSH: ' + setVerifiedColor(sshOk))
    print('GPIO: ' + setVerifiedColor(gpioOk))
    print('I2C: ' + setVerifiedColor(i2cOk))
    print('Repositório do GIT: ' + setVerifiedColor(repoOk))
    print('Lidar: ' + setVerifiedColor(lidarOk))
    print('AccessPoint: ' + setVerifiedColor(accesPOk))
    print('UsbPortConfig: ' + setVerifiedColor(portsOk))
    print("Iniciar Automáticamente o robô: " + setVerifiedColor(autoStartRobot))


def showQuestion(msg,function,errorMsg):
    print(msg)
    print('[0] - Sim')
    print('[1] Não')
    try:
        answ = input("Default=0: ")
        answ = int(answ)
    except:
        answ = 0

    if(answ == 0):
        try:
            run("clear")
            function()
            return True
        except:
            run("clear")
            print(bcolors.FAIL + errorMsg + bcolors.ENDC)
            echoToFile("./log",errorMsg,False)
            time.sleep(1)
            return False
    run("clear")

def main():
    run("clear")
    echoToFile("./log","",True)
    fixBugs()

    global gpioOk,i2cOk,sshOk,lidarOk,repoOk,updtOk,portsOk,autoStartRobot
    addUserSerialPorts()
    portsOk = True

    updtOk = showQuestion(bcolors.OKBLUE + "Fazer update no sistema?" + bcolors.ENDC, updateSystem,'Erro ao dar update no sistema')
    sshOk = showQuestion(bcolors.OKBLUE + 'Instalar e configurar o ssh?' + bcolors.ENDC,installandConfigureSSH,'Erro ao instalar o SSH')
    gpioOk = showQuestion(bcolors.OKBLUE + 'Instalar e configurar o GPIO?' + bcolors.ENDC,installGPIO,'Erro ao instalar o GPIO')
    i2cOk = showQuestion(bcolors.OKBLUE + 'Instalar e configurar o I2C?' + bcolors.ENDC,installI2C,'Erro ao instalar o I2C')
    repoOk = showQuestion(bcolors.OKBLUE + 'Baixar o repositório do robô?' + bcolors.ENDC,downloadRepo,'Erro ao baixar o repositório remoto')
    autoStartRobot = showQuestion(bcolors.OKBLUE + "Configurando a inicialização automática do robô" + bcolors.ENDC,setAutoStartRobotCore,'Erro ao Configurar a inicialização automática do robô')
    accesPOk = showQuestion(bcolors.OKBLUE + 'Configurar o RASP como access point?' + bcolors.ENDC,newAccessPoint,'Erro ao configurar o AcessPoint')
    lidarOk = showQuestion(bcolors.OKBLUE + 'Instalar a biblioteca do RPLidar?***È NECESSÀRIO TER O ROS INSTALADO***' + bcolors.ENDC,installLidar,'Erro ao configurar o AcessPoint')
    
    log()

main()
