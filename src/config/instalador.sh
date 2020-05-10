#!/bin/bash

function GerarWifi(){
  echo "Enter network name: "
  read network_name
  echo "Enter password name"
  read password_name
  echo >> /etc/dhcpcd.conf "denyinterfaces wlan0"
  echo >> /etc/network/interfaces "allow-hotplug wlan0
    iface wlan0 inet static
    address 192.168.1.2
    netmask 255.255.255.0
    network 192.168.1.1
    broadcast 192.168.1.255"
  echo >> /etc/hostapd/hostapd.conf "interface=wlan0
    driver=nl80211
    ssid=$network_name
    hw_mode=g
    channel=6
    macaddr_acl=0
    auth_algs=1
    ignore_broadcast_ssid=0
    wpa=2
    wpa_passphrase=$password_name
    wpa_key_mgmt=WPA-PSK
    rsn_pairwise=CCMP"
  echo >> /etc/default/hostapd 'DAEMON_CONF="/etc/hostapd/hostapd.conf"'
  echo >> /etc/dnsmasq.conf "interface=wlan0
    listen-address=192.168.1.2
    bind-interfaces
    server=8.8.8.8
    domain-needed
    bogus-priv
    dhcp-range=192.168.1.120,192.168.1.254,12h"
  echo >> /etc/sysctl.conf "net.ipv4.ip_forward=1"

  sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
  sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
  sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT

  sh -c "iptables-save > /etc/iptables.ipv4.nat"

  echo "Raspberry turned into an Acces Point.
  Ip: 192.168.1.2
  NetWork name: $network_name
  Password name: $password_name"
}

function downloadROS(){
  sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
  apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
  curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | sudo apt-key add -
  apt-get update
  apt-get install ros-kinetic-desktop
  apt-cache search ros-kinetic
  echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
  source ~/.bashrc
  apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
  rosdep init
  rosdep update
}


echo "Digite o numero equivalento a essa distro:
1 - Ubuntu
2 - Arch
3 - Raspbian"
read NumDistro

#ATUALIZAR SISTEMA
while true; do
  if [ "$NumDistro" -eq 1 ];
  then
    clear
    gerenciadorPacotes="apt-get install"
    apt-get update && apt-get upgrade
    clear
    break;
  elif [ "$NumDistro" -eq 2 ];
  then
    clear
    gerenciadorPacotes="pacman -S"
    pacman -Syyu
    clear
    break;
  elif [ "$NumDistro" -eq 3 ];
  then
    clear
    gerenciadorPacotes="apt-get install"
    apt-get update && apt-get upgrade
    clear
    break;
  else
    echo "Distro não encontrada, favor digitar o numero novamente:"
    read NumDistro
  fi
done

# BAIXAR LIB DOS PINOS GPIO
if [ "$NumDistro" -ne 2 ];
  then
    echo "Deseja instalar a lib dos GPIO?
    1 - Sim
    2 - Não"
    read resposta
    while true;do
      if [ "$resposta" -eq 1 ];
      then
        sudo apt-get install rpi.gpio
        clear
        break;
      elif [ "$resposta" -eq 2 ]
      then
        clear
        break;
      else
        echo "Resposta inexistente, favor digitar novamente:"
        read resposta
      fi
    done

# BAIXAR FONTE DO GIT
echo "Deseja baixar o codigo fonte do Git?
    1 - Sim
    2 - Não"
    read resposta
    while true;do
      if [ "$resposta" -eq 1 ];
      then
        gerenciadorPacotes git
        git clone https://github.com/CaioslppUO/Agrobot-2.0
        cd Agrobot-2.0
        git checkout raspberry-ros
        clear
        break;
      elif [ "$resposta" -eq 2 ]
      then
        clear
        break;
      else
        echo "Resposta inexistente, favor digitar novamente:"
        read resposta
      fi
    done
    

# SUBSYSTEM=="usb", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", SYMLINK+="ttyUSB_CONVERSOR-0" MODE=="0777"

# ADICIONANDO USUARIO NO GRUPO PARA LER PORTA SERIAL
usermod -a -G dialout $USER

# BAIXANDO SSH
$gerenciadorPacotes openssh*

# CONFIGURAR SSH
touch /usr/bin/resetssh.sh 
echo >> /usr/bin/resetssh.sh "service ssh restart"
chmod +x /usr/bin/resetssh.sh
touch /lib/systemd/system/restartssh.service
echo >> /lib/systemd/system/restartssh.service "
[Unit]
Description=Example systemd service.

[Service]
Type=simple
ExecStart=/bin/bash /usr/bin/resetssh.sh

[Install]
WantedBy=multi-user.target"
chmod 644 /etc/systemd/system/resetssh.service
systemctl start resetssh
systemctl enable resetssh



# GERAR WIFI
echo "Deseja gerar um wifi com o rasp?
    1 - Sim
    2 - Não"
    read resposta
    while true;do
      if [ "$resposta" -eq 1 ];
      then
        GerarWifi
        clear
        break;
      elif [ "$resposta" -eq 2 ]
      then
        clear
        break;
      else
        echo "Resposta inexistente, favor digitar novamente:"
        read resposta
      fi
    done

echo "Deseja baixar o ROS?
    1 - Sim
    2 - Não"
    read resposta
    while true;do
      if [ "$resposta" -eq 1 ];
      then
        downloadROS()
        clear
        break;
      elif [ "$resposta" -eq 2 ]
      then
        clear
        break;
      else
        echo "Resposta inexistente, favor digitar novamente:"
        read resposta
      fi
    done
  
echo "Deseja habilitar login automatico?
    1 - Sim
    2 - Não"
    read resposta
    while true;do
      if [ "$resposta" -eq 1 ];
      then
        echo >> /etc/lightdm/lightdm.conf "[SeatDefaults]
          greeter-show-manual-login=true
          greeter-hide-users=true
          autologin-user= $USER
          autologin-user-timeout=0"
        clear
        break;
      elif [ "$resposta" -eq 2 ]
      then
        clear
        break;
      else
        echo "Resposta inexistente, favor digitar novamente:"
        read resposta
      fi
    done

echo "Deseja habilitar o i2c?
    1 - Sim
    2 - Não"
    read resposta
    while true;do
      if [ "$resposta" -eq 1 ];
      then
        echo "va em 'INTERFACING OPTIONS'"
        raspi-config
        echo >> /dev/modules "#i2c
          i2c-bcm2835 
          #disponibilizar o barramento em /dev 
          i2c-dev"
          echo >> /boot/config.txt "dtparam=i2c1=on"
          apt-get install python-smbus i2c-tools
        clear
        break;
      elif [ "$resposta" -eq 2 ]
      then
        clear
        break;
      else
        echo "Resposta inexistente, favor digitar novamente:"
        read resposta
      fi
    done

reboot
