import os,pathlib,time

const_catkin_original_path: str = str(pathlib.Path(__file__).parent.absolute()) + "/"
const_catkin_original_path += "../src/catkin_ws/"
const_user_name: str = input("Digite o nome de usuário: ")
const_user_home_path: str = "/home/" + const_user_name + "/"
const_user_group: str = input("Digite o grupo do seu usuário: ")
const_project_to_install = input("Qual projeto instalar[agrobot,agrobot_lidar]?: ") + "/"

def install_catkin(project: str):
    # Copiando a pasta do projeto para o home.
    os.system("cp -r " + const_catkin_original_path + " "
     + const_user_home_path)
    os.system("chown -R" + const_user_name + ":" + const_user_group + " " +
     const_user_home_path + "catkin_ws/")

    # Excluindo a pasta do projeto que não será utilizada.
    if(project == "agrobot_lidar/"):
        os.system("cd " + const_user_home_path +
         "catkin_ws/src/ && sudo rm -r agrobot/")
    elif(project == "agrobot/"):
        os.system("cd " + const_user_home_path +
         "catkin_ws/src/ && sudo rm -r agrobot_lidar/")

    # Compilando o projeto.
    command: str = "source /opt/ros/melodic/setup.bash && "
    command += "cd " + const_user_home_path + "catkin_ws/ && "
    command += "catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3"
    os.system(command)

    os.system("clear")

    # Dando source na pasta do projeto para o zsh.
    source_path = input("Deseja dar source na pasta catkin para o zsh?(y/N): ")
    if(source_path == "y"):
        command = "echo 'source " + const_user_home_path + "catkin_ws/devel/setup.zsh' >> " + const_user_home_path + ".zshrc"
        os.system(command)
        command = "source " + const_user_home_path + ".zshrc"
        os.system(command)

    # Dando source na pasta do projeto para o bash.
    source_path = input("Deseja dar source na pasta catkin para o bash?(y/N): ")
    if(source_path == "y"):
        command = "echo 'source " + const_user_home_path + "catkin_ws/devel/setup.bash' >> " + const_user_home_path + ".bashrc"
        os.system(command)
        command = "source " + const_user_home_path + ".bashrc"
        os.system(command)

def install_script():
    scrpt_command = "source /opt/ros/melodic/setup.bash && "
    scrpt_command += "source " + const_user_home_path + "catkin_ws/devel/setup.bash && "
    scrpt_command += "roslaunch agrobot run.launch"
    
    os.system("sudo echo '" + scrpt_command + "' > /usr/bin/launch_agrobot.sh")
    os.system("sudo chmod +x /usr/bin/launch_agrobot.sh")

def install_service():
    command = "[Unit]\n"
    command += "Description=Serviço que inicializa o código fonte do robô.\n\n"

    command += "[Service]\n"
    command += "Type=simple\n"
    command += "ExecStart=/bin/bash /usr/bin/launch_agrobot.sh\n\n"

    command += "[Install]\n"
    command += "WantedBy=multi-user.target"

    os.system("sudo echo '" + command + "' > /etc/systemd/system/launch_agrobot.service")
    os.system("sudo chmod 644 /etc/systemd/system/launch_agrobot.service")

    enable_service = input("Deseja habilitar o serviço?(y/N): ")
    if(enable_service == "y"):
        os.system("sudo systemctl enable launch_agrobot.service")

def install():
    install_catkin(const_project_to_install)
    install_script()
    install_service()

    print("\nDone.")

install()