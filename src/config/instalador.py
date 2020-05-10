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
rosOk = False
sshOk = False
lidarOk = False
accesPOk = False
repoOk = False
updtOk = False
portsOk = False

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

def newAccessPoint():
    print(bcolors.OKGREEN + "Toranando o RaspBerry em um Access Point" + bcolors.ENDC)
    global wifiName,wifiPassword
    command = "sudo apt-get install -y dnsmasq hostapd"
    run(command)
    wifiName = input("Digite o nome da rede wifi:")
    wifiPassword = input("Digite a senha da rede wifi:")
    command = "sudo echo >> /etc/dhcpcd.conf 'denyinterfaces wlan0' "
    run(command)
    command = "sudo echo >> /etc/network/interfaces 'allow-hotplug wlan0\
    iface wlan0 inet static\
    address 192.168.1.2\
    netmask 255.255.255.0\
    network 192.168.1.1\
    broadcast 192.168.1.255'"
    run(command)
    command = "sudo echo >> /etc/hostapd/hostapd.conf 'interface=wlan0\
    driver=nl80211\
    ssid="+ wifiName + "\
    hw_mode=g\
    channel=6\
    macaddr_acl=0\
    auth_algs=1\
    ignore_broadcast_ssid=0\
    wpa=2\
    wpa_passphrase=" + wifiPassword + "\
    wpa_key_mgmt=WPA-PSK\
    rsn_pairwise=CCMP'"
    run(command)
    command = "sudo echo >> /etc/default/hostapd 'DAEMON_CONF='/etc/hostapd/hostapd.conf''"
    run(command)
    command = "sudo echo >> /etc/dnsmasq.conf 'interface=wlan0\
    listen-address=192.168.1.2\
    bind-interfaces\
    server=8.8.8.8\
    domain-needed\
    bogus-priv\
    dhcp-range=192.168.1.120,192.168.1.254,12h'"
    run(command)
    command = "sudo echo >> /etc/sysctl.conf 'net.ipv4.ip_forward=1'"
    run(command)
    command = "sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE"
    run(command)
    command = "sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT"
    run(command)
    command = "sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT"
    run(command)
    command = "sudo sh -c 'iptables-save > /etc/iptables.ipv4.nat'"
    run(command)
    run("clear")
    printOk("Access Point")

def installLidar():
    global lidarRepo
    print(bcolors.OKGREEN + 'Instalando a biblioteca de ROS para o RPLidar' + bcolors.ENDC)
    command = "cd ~/catkin_ws/src && git clone " + lidarRepo + " && cd .. && catkin_make"
    run(command)
    run("clear")
    printOk("Instalação do Lidar")

def configROS():
    print(bcolors.OKGREEN + "Iniciando configuração do ROS melodic" + bcolors.ENDC)
    echoToFile("~/.bashrc","source /opt/ros/melodic/setup.bash",False)
    command = "source ~/.bashrc"
    run(command)
    command = "sudo apt install -y python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential"
    run(command)
    command = "sudo rosdep init"
    run(command)
    command = "sudo rosdep update"
    run(command)
    command = "mkdir -p ~/catkin_ws/src"
    run(command)
    command = "cd ~/catkin_ws && catkin_make"
    run(command)
    run("echo aaaaaaaaaaaaaaaaaaaaaaaaaa")
    time.sleep(5)
    run("clear")
    printOk("Configuração do ROS")

def installROS():
    print(bcolors.OKGREEN + "Iniciando instalacao do ROS melodic" + bcolors.ENDC)
    echoToFile("/etc/apt/sources.list.d/ros-latest.list","deb http://packages.ros.org/ros/ubuntu bionic main",True)
    command = "sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654"
    run(command)
    command = "sudo apt update && sudo apt-get upgrade -y"
    run(command)
    command = "sudo apt install -y ros-melodic-desktop"
    run(command)
    run("echo bbbbbbbbbbbbbbbbbbbb")
    time.sleep(5)
    run("clear")
    printOk("Instalação do ROS")
    configROS()

def updateSystem():
    print(bcolors.OKGREEN + "Inicializando o update e upgrade de sistema" + bcolors.ENDC)
    command = "sudo apt update"
    run(command)
    command = "sudo echo 'linux-firmware-raspi2 hold' | sudo dpkg --set-selections"
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
    run("sudo usermod -a -G uucp " + user)

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
    print(bcolors.OKGREEN + "Iniciando o download do repositiorio remoto do robô" + bcolors.ENDC)
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

def log():
    global gpioOk,i2cOk,rosOk,sshOk,lidarOk,accesPOk,repoOk,updtOk,portsOk
    run("clear")
    print(bcolors.OKGREEN + 'Resumo da instalacao: ' + bcolors.ENDC)
    print('UpdateSystem: ' + setVerifiedColor(updtOk))
    print('SSH: ' + setVerifiedColor(sshOk))
    print('GPIO: ' + setVerifiedColor(gpioOk))
    print('I2C: ' + setVerifiedColor(i2cOk))
    print('Repositorio do GIT: ' + setVerifiedColor(repoOk))
    print('ROS: ' + setVerifiedColor(rosOk))
    print('AccessPoint: ' + setVerifiedColor(accesPOk))
    print('Lidar: ' + setVerifiedColor(lidarOk))
    print('UsbPortConfig: ' + setVerifiedColor(portsOk))


def showQuestion(msg,function,errorMsg):
    print(msg)
    print('[0] - Sim')
    print('[1] Nao')
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
            time.sleep(1)
            return False
    run("clear")

def main():
    run("clear")
    global gpioOk,i2cOk,rosOk,sshOk,lidarOk,accesPOk,repoOk,updtOk,portsOk
    addUserSerialPorts()
    portsOk = True

    updtOk = showQuestion(bcolors.OKBLUE + 'Fazer update e upgrade?' + bcolors.ENDC,updateSystem,'Erro ao dar update no sistema')
    sshOk = showQuestion(bcolors.OKBLUE + 'Instalar e configurar o ssh?' + bcolors.ENDC,installandConfigureSSH,'Erro ao instalar o SSH')
    gpioOk = showQuestion(bcolors.OKBLUE + 'Instalar e configurar o GPIO?' + bcolors.ENDC,installGPIO,'Erro ao instalar o GPIO')
    i2cOk = showQuestion(bcolors.OKBLUE + 'Instalar e configurar o I2C?' + bcolors.ENDC,installI2C,'Erro ao instalar o I2C')
    repoOk = showQuestion(bcolors.OKBLUE + 'Baixar o repositorio do robô?' + bcolors.ENDC,downloadRepo,'Erro ao baixar o repositorio remoto')
    rosO = showQuestion(bcolors.OKBLUE + 'Instalar e configurar o ROS?' + bcolors.ENDC,installROS,'Erro ao instalar o ROS')
    accesPOk = showQuestion(bcolors.OKBLUE + 'Configurar o RASP como access point?' + bcolors.ENDC,newAccessPoint,'Erro ao configurar o AcessPoint')
    lidarOk = showQuestion(bcolors.OKBLUE + 'Instalar a biblioteca do RPLidar?' + bcolors.ENDC,installLidar,'Erro ao configurar o AcessPoint')

    log()


main()