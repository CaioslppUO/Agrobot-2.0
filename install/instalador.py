#!//usr/bin/env python
#coding: utf-8
import os
import time
import subprocess

const_wifi_name = "Agrobot4"
const_wifi_password = "rapisbere"
const_repository_agrobot = "https://github.com/CaioslppUO/Agrobot-2.0"
const_repository_lidar = "https://github.com/robopeak/rplidar_ros"
const_user = "$USER"

#Flags para Log
gpio_task_check = False
i2c_task_check = False
ssh_task_check = False
lidar_task_check = False
repo_task_check = False
updt_task_check = False
ports_task_check = False
auto_start_robot = False
acces_task_check = False

#Abre um arquivo novo, ou limpa o arquivo existente
const_overwrite_file = "w"
#Insere no arquivo, ou cria um arquivo
const_append_to_file = "a"

#Classe que guarda os padrões de cores usadas nos logs
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#printa OK em verde
def print_ok(msg):
    run("clear")
    print(bcolors.OKGREEN + msg + " " + " OK " + bcolors.ENDC)
    time.sleep(1)
    run("clear")

#Executa um comando de terminal
def run(command):
    subprocess.call(command,shell=True,executable='/bin/bash')

#Abre um arquivo da insere ou reseta o msm, e fecha. 
def write_file(file_path,msg,mode):
    file = open(file_path, mode)
    file.writelines(msg)
    file.close()

#Faz a instalação do do lidar na maquina.
def install_lidar():
    print(bcolors.OKGREEN + 'Instalando a biblioteca de ROS para o RPLidar' + bcolors.ENDC)
    command = "cd ~/catkin_ws/src && sudo -u labiot git clone " + const_repository_lidar
    run(command)
    print(bcolors.WARNING +  "********************************************************************************************************************************************" + bcolors.ENDC)
    print(bcolors.WARNING +  'Para terminar a instalação entre no diretório: ~/catkin_ws e digite o comando: catkin_make -j 1 e após o comando ser executado, aperte ctrl+d' + bcolors.ENDC)
    print(bcolors.WARNING +  "********************************************************************************************************************************************" + bcolors.ENDC)
    command = "sudo -u labiot -s"
    run(command)
    run("clear")
    print_ok("Instalação do Lidar")

#Torna o raspberry em um accespoint
def create_acess_point():
    print(bcolors.OKGREEN + "Toranando o RaspBerry em um Access Point" + bcolors.ENDC)

    command = "sudo apt-get install -y dnsmasq hostapd dhcpcd5"
    run(command)
    command = "sudo systemctl stop hostapd"
    run(command)
    command = "sudo systemctl stop dnsmasq"
    run(command)

    file_content = list()

    write_file("denyinterfaces wlan0\n","/etc/dhcpcd.conf",const_append_to_file)

    file_content.append("\nallow-hotplug wlan0\n")
    file_content.append("iface wlan0 inet static\n")
    file_content.append("address 192.168.1.2\n")
    file_content.append("netmask 255.255.255.0\n")
    file_content.append("network 192.168.1.1\n")
    file_content.append("broadcast 192.168.1.255\n")
    write_file(file_content,"/etc/network/interfaces",const_overwrite_file)
    file_content.clear()
    
    file_content.append("interface=wlan0\n")
    file_content.append("driver=nl80211\n")
    file_content.append("ssid="+const_wifi_name+"\n")
    file_content.append("hw_mode=g\n")
    file_content.append("channel=6\n")
    file_content.append("macaddr_acl=0\n")
    file_content.append("auth_algs=1\n")
    file_content.append("ignore_broadcast_ssid=0\n")
    file_content.append("wpa=2\n")
    file_content.append("wpa_passphrase="+const_wifi_password+"\n")
    file_content.append("wpa_key_mgmt=WPA-PSK\n")
    file_content.append("rsn_pairwise=CCMP\n")
    write_file(file_content,"/etc/hostapd/hostapd.conf",const_overwrite_file)
    file_content.clear()

    file_content.append("\nDAEMON_CONF='/etc/hostapd/hostapd.conf'\n")
    write_file(file_content,"/etc/default/hostapd",const_append_to_file)
    file_content.clear()

    file_content.append("interface=wlan0\n")
    file_content.append("listen-address=192.168.1.2\n")
    file_content.append("bind-interfaces\n")
    file_content.append("server=8.8.8.8\n")
    file_content.append("domain-needed\n")
    file_content.append("bogus-priv\n")
    file_content.append("dhcp-range=192.168.1.120,192.168.1.254,12h\n")
    write_file(file_content,"/etc/dnsmasq.conf",const_overwrite_file)
    file_content.clear()

    file_content.append("\nnet.ipv4.ip_forward=1")
    write_file(file_content,"/etc/sysctl.conf",const_append_to_file)
    file_content.clear()

    command = "sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE"
    run(command)
    command = "sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT"
    run(command)
    command = "sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT"
    run(command)
    command = "sudo sh -c 'iptables-save > /etc/iptables.ipv4.nat'"
    run(command)

    file_content.append("\niptables-restore < /etc/iptables.ipv4.nat")
    file_content.append("\n/usr/sbin/hostapd /etc/hostapd/hostapd.conf")
    write_file(file_content,"/usr/bin/resetssh.sh",const_append_to_file)
    file_content.clear()

    command = "sudo apt-get install ponte-utils"
    run(command)
    command = "sudo brctl addbr br0"
    run(command)
    command = "sudo brctl addif br0 eth0"
    run(command)
    
    run("clear")
    print_ok("Access Point")

#da update e upgrade no S.O
def update_system():
    print(bcolors.OKGREEN + "Inicializando o update e upgrade de sistema" + bcolors.ENDC)
    command = "sudo apt update"
    run(command)
    command = "sudo apt autoremove -y && sudo apt upgrade -y"
    run(command)
    command = "sudo apt-get install vim"
    run(command)
    run("clear")
    print_ok("Update de sistema")

#Faz a instalação das libs para usar os pinos GPIO
def install_GPIO():
    print(bcolors.OKGREEN + "Instalando e configurando o GPIO" + bcolors.ENDC)
    command = "sudo apt-get install -y rpi.gpio"
    run(command)
    run("clear")
    print_ok("Instalação do GPIO")

#Ativa e configura o i2C do rasp
def install_I2c():
    print(bcolors.OKGREEN + "Instalando e configurando o I2C" + bcolors.ENDC)
    run("sudo raspi-config")
    file_content = list()
    
    file_content.append("i2c-bcm2835")
    file_content.append("i2c-dev")
    write_file(file_content,"/dev/modules",const_append_to_file)
    file_content.clear()

    write_file("dtparam=i2c1=on","/boot/config.txt",const_append_to_file)
    
    command = "sudo apt-get install -y python-smbus i2c-tools"
    run(command)
    run("clear")
    print_ok("Instalação do I2C")

#Da permissão ao usuario poder acessar as portas serial, e altera o nome das mesmas para o uso do ttl
def serial_ports_configuration():
    run("sudo usermod -a -G dialout " + const_user)
    file_content = list()
    file_content.append("SUBSYSTEM=='tty', KERNELS=='1-1.4:1.0', SYMLINK+='ttyUSB_CONVERSOR-0'\n")
    file_content.append("SUBSYSTEM=='tty', KERNELS=='1-1.5:1.0', SYMLINK+='ttyUSB_CONVERSOR-1'\n")
    write_file(file_content,"/etc/udev/rules.d/99-usb-serial.rules",const_overwrite_file)

#Instala e configura o ssh na maquina
def to_set_up_ssh():
    print(bcolors.OKGREEN + "Instalando e configurando o SSH" + bcolors.ENDC)
    command = "sudo apt-get install -y openssh*"
    run(command)

    file_content = list()

    write_file("service ssh restart","/usr/bin/resetssh.sh",const_overwrite_file)

    command = "sudo chmod +x /usr/bin/resetssh.sh"
    run(command)

    file_content.append("[Unit]\n")
    file_content.append("Description=Starts ssh\n")
    file_content.append("\n")
    file_content.append("[Service]\n")
    file_content.append("Type=simple\n")
    file_content.append("ExecStart=/bin/bash /usr/bin/resetssh.sh\n")
    file_content.append("\n")
    file_content.append("[Install]\n")
    file_content.append("WantedBy=multi-user.target\n")
    write_file(file_content,"/etc/systemd/system/restartssh.service",const_overwrite_file)
    file_content.clear()

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
    print_ok("Instalação do SSH")

#Faz a download do repositorio do projeto
def download_repository():
    print(bcolors.OKGREEN + "Iniciando o download do repositiório remoto do robô" + bcolors.ENDC)
    command = "sudo apt install git"
    run(command)
    command = "git clone " + const_repository_agrobot
    run(command)
    command = "cd Agrobot-2.0 && git checkout raspberry-ros-stable && clear"
    run(command)
    run("clear")
    print_ok("Download do repositório")

#Retorna OK em verde ou NO em vermelhor
def set_verified_color(var):
    if(var == True):
        return bcolors.OKBLUE + "OK" + bcolors.ENDC
    else:
        return bcolors.FAIL + "NO" + bcolors.ENDC

#arruma possiveis problemas de pacotes com o gerenciador de pacotes
def fix_bugs():
    command = "sudo echo 'linux-firmware-raspi2 hold' | sudo dpkg --set-selections"
    run(command)

#Cria o script que executa o programa na hora que o rasp liga
def set_auto_start_robot_core():
    print(bcolors.OKGREEN + "Configurando a inicialização automática do robô" + bcolors.ENDC)

    write_file("source /opt/ros/melodic/setup.bash && /home/labiot/Agrobot-2.0/src/raspberryRos/runnables/./run_ROBOT.sh","/usr/bin/auto_start_robotCore.sh",const_overwrite_file)
    command = "sudo chmod +x /usr/bin/auto_start_robotCore.sh"
    run(command)

    file_content = list()
    
    file_content.append("[Unit]")
    file_content.append("Description=Starts ssh")
    file_content.append("")
    file_content.append("[Service]")
    file_content.append("Type=simple")
    file_content.append("ExecStart=/bin/bash /usr/bin/auto_start_robotCore.sh")
    file_content.append("")
    file_content.append("[Install]")
    file_content.append("WantedBy=multi-user.target")
    write_file(file_content,"/usr/bin/auto_start_robotCore.sh",const_overwrite_file)
    file_content.clear()

    command = "sudo chmod 644 /etc/systemd/system/auto_start_robotCore.service"
    run(command)
    command = "sudo systemctl enable auto_start_robotCore"
    run(command)
    run("clear")
    print_ok("Configuração da inicialização automática do robô")

#Printa o log final do script
def log():
    run("clear")
    print(bcolors.OKGREEN + 'Resumo da instalação: ' + bcolors.ENDC)
    print('UpdateSystem: ' + set_verified_color(updt_task_check))
    print('SSH: ' + set_verified_color(ssh_task_check))
    print('GPIO: ' + set_verified_color(gpio_task_check))
    print('I2C: ' + set_verified_color(i2c_task_check))
    print('Repositório do GIT: ' + set_verified_color(repo_task_check))
    print('Lidar: ' + set_verified_color(lidar_task_check))
    print('AccessPoint: ' + set_verified_color(acces_task_check))
    print('UsbPortConfig: ' + set_verified_color(ports_task_check))
    print("Iniciar Automáticamente o robô: " + set_verified_color(auto_start_robot))

#Menu do script
def show_question(msg,function,errorMsg):
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
            write_file("./log",errorMsg,const_append_to_file)
            
            time.sleep(1)
            return False
    run("clear")

#Função principal, faz a chamada de todas as funções do script, e seta os flags
def main():
    run("clear")
    write_file("./log","",const_overwrite_file)
    fix_bugs()

    global gpio_task_check,i2c_task_check,ssh_task_check,lidar_task_check,repo_task_check,updt_task_check,ports_task_check,auto_start_robot,acces_task_check
    serial_ports_configuration()

    ports_task_check = True

    updt_task_check = show_question(bcolors.OKBLUE + "Fazer update no sistema?" + bcolors.ENDC, update_system,'Erro ao dar update no sistema')
    ssh_task_check = show_question(bcolors.OKBLUE + 'Instalar e configurar o ssh?' + bcolors.ENDC,to_set_up_ssh,'Erro ao instalar o SSH')
    gpio_task_check = show_question(bcolors.OKBLUE + 'Instalar e configurar o GPIO?' + bcolors.ENDC,install_GPIO,'Erro ao instalar o GPIO')
    i2c_task_check = show_question(bcolors.OKBLUE + 'Instalar e configurar o I2C?' + bcolors.ENDC,install_I2c,'Erro ao instalar o I2C')
    repo_task_check = show_question(bcolors.OKBLUE + 'Baixar o repositório do robô?' + bcolors.ENDC,download_repository,'Erro ao baixar o repositório remoto')
    acces_task_check = show_question(bcolors.OKBLUE + 'Configurar o RASP como access point?' + bcolors.ENDC,create_acess_point,'Erro ao configurar o AcessPoint')
    auto_start_robot = show_question(bcolors.OKBLUE + "Configurando a inicialização automática do robô" + bcolors.ENDC,set_auto_start_robot_core,'Erro ao Configurar a inicialização automática do robô')
    lidar_task_check = show_question(bcolors.OKBLUE + 'Instalar a biblioteca do RPLidar?***È NECESSÀRIO TER O ROS INSTALADO***' + bcolors.ENDC,install_lidar,'Erro ao configurar o AcessPoint')
    
    log()

main()
