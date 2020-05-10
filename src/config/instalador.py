#!//usr/bin/env python
#coding: utf-8
import os
import time

wifiName = ""
wifiPassword = ""
gitRepo = "https://github.com/CaioslppUO/Agrobot-2.0"
lidarRepo = "https://github.com/robopeak/rplidar_ros"
rosDistro = "kinetic"
libGPIO = "rpi.gpio"
libI2C = "python-smbus i2c-tools"
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

def newAccessPoint():
    print("Toranando o RaspBerry em um Access Point")
    global wifiName,wifiPassword
    command = "apt-get install -y dnsmasq hostapd"
    os.system(command)
    wifiName = input("Digite o nome da rede wifi:")
    wifiPassword = input("Digite a senha da rede wifi:")
    command = "echo >> /etc/dhcpcd.conf 'denyinterfaces wlan0' "
    os.system(command)
    command = "echo >> /etc/network/interfaces 'allow-hotplug wlan0\
    iface wlan0 inet static\
    address 192.168.1.2\
    netmask 255.255.255.0\
    network 192.168.1.1\
    broadcast 192.168.1.255'"
    os.system(command)
    command = "echo >> /etc/hostapd/hostapd.conf 'interface=wlan0\
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
    os.system(command)
    command = "echo >> /etc/default/hostapd 'DAEMON_CONF='/etc/hostapd/hostapd.conf''"
    os.system(command)
    command = "echo >> /etc/dnsmasq.conf 'interface=wlan0\
    listen-address=192.168.1.2\
    bind-interfaces\
    server=8.8.8.8\
    domain-needed\
    bogus-priv\
    dhcp-range=192.168.1.120,192.168.1.254,12h'"
    os.system(command)
    command = "echo >> /etc/sysctl.conf 'net.ipv4.ip_forward=1'"
    os.system(command)
    command = "sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE"
    os.system(command)
    command = "sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT"
    os.system(command)
    command = "sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT"
    os.system(command)
    command = "sh -c 'iptables-save > /etc/iptables.ipv4.nat'"
    os.system(command)
    os.system("clear")
    
def configureRos():
    print("Iniciando configuracao do Ros")
    command = "mkdir -p ~/catkin_ws/src"
    os.system(command)
    command = "cd ~/catkin_ws/ && catkin_make"
    os.system(command)
    command = "echo >> ~/.bashrc 'source ~/catkin_ws/devel/setup.bash'"
    os.system(command)
    os.system("clear")

def installLidar():
    global lidarRepo
    print('Instalando a biblioteca de ROS para o RPLidar')
    command = "cd ~/catkin_ws/src && git clone " + lidarRepo + " && cd .. && catkin_make"
    os.system(command)
    os.system("clear")

def installROS():
    print("Iniciando instalacao do ROS")
    command = "apt-get install -y dirmngr"
    os.system(command)
    command = "sh -c 'echo 'deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main' > /etc/apt/sources.list.d/ros-latest.list'"
    os.system(command)
    command = "apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654"
    os.system(command)
    command = "curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | sudo apt-key add -"
    os.system(command)
    command = "apt-get update"
    os.system(command)
    command = "apt-get install -y ros-kinetic-desktop"
    os.system(command)
    commando = "apt-cache search ros-kinetic"
    os.system(command)
    command = "echo 'source /opt/ros/kinetic/setup.bash' >> ~/.bashrc"
    os.system(command)
    command = "source ~/.bashrc"
    os.system(command)
    command = "apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential"
    os.system(command)
    command = "rosdep init"
    os.system(command)
    command = "rosdep update"
    os.system("clear")

def updateSystem():
    print("Inicializando o update e upgrade de sistema")
    command = "apt-get update && upgrade"
    os.system(command)
    os.system("clear")

def installGPIO():
    print("Instalando e configurando o GPIO")
    os.system("raspi-config")
    command = "apt-get install -y rpi.gpio"
    os.system(command)
    os.system("clear")

def installI2C():
    print("Instalando e configurando o I2C")
    os.system("raspi-config")
    command = "echo >> /dev/modules '\
    i2c-bcm2835 \
    i2c-dev'"
    os.system(command)
    command = "echo >> /boot/config.txt 'dtparam=i2c1=on'"
    os.system(command)
    command = "apt-get install -y python-smbus i2c-tools"
    os.system(command)
    os.system("clear")

def addUserSerialPorts():
    os.system("usermod -a -G uucp " + user)

def installandConfigureSSH():
    print("Instalando e configurando o SSH")
    command = "apt-get install -y openssh*"
    os.system(command)
    command = "touch /usr/bin/resetssh.sh"
    os.system(command)
    command = "echo >> /usr/bin/resetssh.sh 'service ssh restart'\
    chmod +x /usr/bin/resetssh.sh\
    touch /lib/systemd/system/restartssh.service"
    os.system(command)
    command = "echo >> /lib/systemd/system/restartssh.service '\
    [Unit]\
    Description=Example systemd service.\
    [Service]\
    Type=simple\
    ExecStart=/bin/bash /usr/bin/resetssh.sh\
    [Install]\
    WantedBy=multi-user.target'"
    os.system(command)
    command = "chmod 644 /etc/systemd/system/resetssh.service"
    os.system(command)
    command = "systemctl start resetssh"
    os.system(command)
    command = "systemctl enable resetssh"
    os.system(command)
    command = "ufw allow 22"
    os.system(command)
    command = "dpkg-reconfigure openssh-server"
    os.system(command)
    os.system("clear")

def downloadRepo():
    global gitRepo
    print("Iniciando o download do repositiorio remoto")
    command = "apt install git"
    os.system(command)
    command = "git clone " + gitRepo
    os.system(command)
    command = "cd Agrobot-2.0 && git checkout raspberry-ros && clear"
    os.system(command)

def log():
    global gpioOk,i2cOk,rosOk,sshOk,lidarOk,accesPOk,repoOk,updtOk,portsOk
    os.system("clear")
    print('Resumo da instalacao: ')
    print('UpdateSystem: ' + str(updtOk))
    print('SSH: ' + str(sshOk))
    print('GPIO: ' + str(gpioOk))
    print('I2C: ' + str(i2cOk))
    print('Repositorio do GIT: ' + str(repoOk))
    print('ROS: ' + str(rosOk))
    print('AccessPoint: ' + str(accesPOk))
    print('Lidar: ' + str(lidarOk))
    print('UsbPortConfig: ' + str(portsOk))

def main():
    global gpioOk,i2cOk,rosOk,sshOk,lidarOk,accesPOk,repoOk,updtOk,portsOk
    addUserSerialPorts()
    portsOk = True
    print('Fazer update e upgrade?')
    print('[0] - Sim')
    print('[1] Nao')
    answ = input("Default=0")
    if(answ != ""):
        answ = int(answ)
    else:
        answ = 0

    if(answ != 1):
        try:
            updateSystem()
            updtOk = True
        except:
            os.system("clear")
            print('Erro ao dar update no sistema')
            time.sleep(1)
    
    print('Instalar e configurar o ssh?')
    print('[0] - Sim')
    print('[1] Nao')
    answ = input("Default=0")
    if(answ != ""):
        answ = int(answ)
    else:
        answ = 0


    if(answ != 1):
        try:
            installandConfigureSSH()
            sshOk = True
        except:
            os.system("clear")
            print('Erro ao instalar o SSH')
            time.sleep(1)
    
    print('Instalar e configurar o GPIO?')
    print('[0] - Sim')
    print('[1] Nao')
    answ = input("Default=0")
    if(answ != ""):
        answ = int(answ)
    else:
        answ = 0

    if(answ != 1):
        try:
            installGPIO()
            gpioOk = True
        except:
            os.system("clear")
            print('Erro ao instalar o GPIO')
            time.sleep(1)

    print('Instalar e configurar o I2C?')
    print('[0] - Sim')
    print('[1] Nao')
    answ = input("Default=0")
    if(answ != ""):
        answ = int(answ)
    else:
        answ = 0

    if(answ != 1):
        try:
            installI2C()
            i2cOk = True
        except:
            os.system("clear")
            print('Erro ao instalar o I2C')
            time.sleep(1)

    print('Baixar o repositorio do git?')
    print('[0] - Sim')
    print('[1] Nao')
    answ = input("Default=0")
    if(answ != ""):
        answ = int(answ)
    else:
        answ = 0
    
    if(answ != 1):
        try:
            downloadRepo()
            repoOk = True
        except:
            os.system("clear")
            print('Erro ao baixar o repositorio remoto')
            time.sleep(1)

    print('Instalar e configurar o ROS?')
    print('[0] - Sim')
    print('[1] Nao')
    answ = input("Default=0")
    if(answ != ""):
        answ = int(answ)
    else:
        answ = 0
    
    if(answ != 1):
        try:
            installROS()
            rosOk = True
        except:
            os.system("clear")
            print('Erro ao instalar o ROS')
            time.sleep(1)
        
    print('Configurar o RASP como access point?')
    print('[0] - Sim')
    print('[1] Nao')
    answ = input("Default=0")
    if(answ != ""):
        answ = int(answ)
    else:
        answ = 0
    
    if(answ != 1):
        try:
            newAccessPoint()
            accesPOk = True
        except:
            os.system("clear")
            print('Erro ao configurar o AcessPoint')
            time.sleep(1)
    
    print('Instalar a biblioteca do RPLidar?')
    print('[0] - Sim')
    print('[1] Nao')
    answ = input("Default=0")
    if(answ != ""):
        answ = int(answ)
    else:
        answ = 0
    
    if(answ != 1):
        try:
            installLidar()
            lidarOk = True
        except:
            os.system("clear")
            print('Erro ao configurar o AcessPoint')
            time.sleep(1)
        
main()
log()