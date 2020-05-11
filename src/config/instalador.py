#!//usr/bin/env python
#coding: utf-8
import os
import time
import subprocess

wifiName = ""
wifiPassword = ""
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

def echoToFile(filePath,msg,overWrite):
    if(overWrite == True):
        command = "sudo echo > " + filePath + " '" + msg + "'"
    else:
        command = "sudo echo >> " + filePath + " '" + msg + "'"
    run(command)

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
    global wifiName,wifiPassword

    command = "sudo apt-get install -y dnsmasq hostapd dhcpcd5"
    run(command)
    command = "sudo systemctl stop hostapd"
    run(command)
    command = "sudo systemctl stop dnsmasq"
    run(command)

    echoToFile("/etc/dhcpcd.conf","denyinterfaces wlan0",False)

    echoToFile("/etc/network/interfaces","allow-hotplug wlan0",True)
    echoToFile("/etc/network/interfaces","iface wlan0 inet static",False)
    echoToFile("/etc/network/interfaces","address 192.168.1.2",False)
    echoToFile("/etc/network/interfaces","netmask 255.255.255.0",False)
    echoToFile("/etc/network/interfaces","network 192.168.1.1",False)
    echoToFile("/etc/network/interfaces","broadcast 192.168.1.255",False)

    wifiName = input("Digite o nome da rede wifi:")
    wifiPassword = input("Digite a senha da rede wifi:")

    echoToFile("/etc/hostapd/hostapd.conf","interface=wlan0",True)
    echoToFile("/etc/hostapd/hostapd.conf","driver=nl80211",False)
    echoToFile("/etc/hostapd/hostapd.conf","ssid="+wifiName,False)
    echoToFile("/etc/hostapd/hostapd.conf","hw_mode=g",False)
    echoToFile("/etc/hostapd/hostapd.conf","channel=6",False)
    echoToFile("/etc/hostapd/hostapd.conf","macaddr_acl=0",False)
    echoToFile("/etc/hostapd/hostapd.conf","auth_algs=1",False)
    echoToFile("/etc/hostapd/hostapd.conf","ignore_broadcast_ssid=0",False)
    echoToFile("/etc/hostapd/hostapd.conf","wpa=2",False)
    echoToFile("/etc/hostapd/hostapd.conf","wpa_passphrase="+wifiPassword,False)
    echoToFile("/etc/hostapd/hostapd.conf","wpa_key_mgmt=WPA-PSK",False)
    echoToFile("/etc/hostapd/hostapd.conf","rsn_pairwise=CCMP",False)

    echoToFile("/etc/default/hostapd","DAEMON_CONF='/etc/hostapd/hostapd.conf'",False)

    echoToFile("/etc/dnsmasq.conf","interface=wlan0",True)
    echoToFile("/etc/dnsmasq.conf","listen-address=192.168.1.2",False)
    echoToFile("/etc/dnsmasq.conf","bind-interfaces",False)
    echoToFile("/etc/dnsmasq.conf","server=8.8.8.8",False)
    echoToFile("/etc/dnsmasq.conf","domain-needed",False)
    echoToFile("/etc/dnsmasq.conf","bogus-priv",False)
    echoToFile("/etc/dnsmasq.conf","dhcp-range=192.168.1.120,192.168.1.254,12h",False)

    echoToFile("/etc/sysctl.conf","net.ipv4.ip_forward=1",False)

    command = "sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE"
    run(command)
    command = "sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT"
    run(command)
    command = "sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT"
    run(command)
    command = "sudo sh -c 'iptables-save > /etc/iptables.ipv4.nat'"
    run(command)

    echoToFile("/usr/bin/resetssh.sh","iptables-restore < /etc/iptables.ipv4.nat",False)
    echoToFile("/usr/bin/resetssh.sh","/usr/sbin/hostapd /etc/hostapd/hostapd.conf",False)

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
    echoToFile("/dev/modules","i2c-bcm2835",False)
    echoToFile("/dev/modules","i2c-dev",False)
    echoToFile("/boot/config.txt","dtparam=i2c1=on",False)
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
    echoToFile("/usr/bin/resetssh.sh","service ssh restart",True)
    command = "sudo chmod +x /usr/bin/resetssh.sh"
    run(command)
    echoToFile("/etc/systemd/system/restartssh.service","[Unit]",True)
    echoToFile("/etc/systemd/system/restartssh.service","Description=Starts ssh",False)
    echoToFile("/etc/systemd/system/restartssh.service","",False)
    echoToFile("/etc/systemd/system/restartssh.service","[Service]",False)
    echoToFile("/etc/systemd/system/restartssh.service","Type=simple",False)
    echoToFile("/etc/systemd/system/restartssh.service","ExecStart=/bin/bash /usr/bin/resetssh.sh",False)
    echoToFile("/etc/systemd/system/restartssh.service","",False)
    echoToFile("/etc/systemd/system/restartssh.service","[Install]",False)
    echoToFile("/etc/systemd/system/restartssh.service","WantedBy=multi-user.target",False)
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
    command = "cd Agrobot-2.0 && git checkout raspberry-ros && clear"
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
    echoToFile("/usr/bin/autoStartRobotCore.sh","source /opt/ros/melodic/setup.bash && /home/labiot/Agrobot-2.0/src/raspberryRos/runnables/./run_ROBOT.sh",True)
    command = "sudo chmod +x /usr/bin/autoStartRobotCore.sh"
    run(command)
    echoToFile("/etc/systemd/system/autoStartRobotCore.service","[Unit]",True)
    echoToFile("/etc/systemd/system/autoStartRobotCore.service","Description=Starts ssh",False)
    echoToFile("/etc/systemd/system/autoStartRobotCore.service","",False)
    echoToFile("/etc/systemd/system/autoStartRobotCore.service","[Service]",False)
    echoToFile("/etc/systemd/system/autoStartRobotCore.service","Type=simple",False)
    echoToFile("/etc/systemd/system/autoStartRobotCore.service","ExecStart=/bin/bash /usr/bin/autoStartRobotCore.sh",False)
    echoToFile("/etc/systemd/system/autoStartRobotCore.service","",False)
    echoToFile("/etc/systemd/system/autoStartRobotCore.service","[Install]",False)
    echoToFile("/etc/systemd/system/autoStartRobotCore.service","WantedBy=multi-user.target",False)
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
    lidarOk = showQuestion(bcolors.OKBLUE + 'Instalar a biblioteca do RPLidar?***È NECESSÀRIO TER O ROS INSTALADO***' + bcolors.ENDC,installLidar,'Erro ao configurar o AcessPoint')
    autoStartRobot = showQuestion(bcolors.OKBLUE + "Configurando a inicialização automática do robô" + bcolors.ENDC,setAutoStartRobotCore,'Erro ao Configurar a inicialização automática do robô')
    accesPOk = showQuestion(bcolors.OKBLUE + 'Configurar o RASP como access point?' + bcolors.ENDC,newAccessPoint,'Erro ao configurar o AcessPoint')
    
    log()


main()