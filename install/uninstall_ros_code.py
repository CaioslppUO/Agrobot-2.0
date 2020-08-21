import os,json,time

print('\033[91m' + 
    "YOU NEED TO CONFIGURE THE CONFIG.JSON BEFORE EXECUTING THIS." +
    '\033[0m')
time.sleep(3)

with open("config.json", "r") as read_file:
    data = json.load(read_file)
    print(data)
    const_user_name = data['user']
    const_home_path: str = "/home/" + const_user_name + "/"

def remove_source(terminal):
    file_ = open(const_home_path + "." + terminal + "rc", 'r')
    content = file_.readlines()
    cleaned_file_content = ""

    for line in content:
        if(line.splitlines()[0] != "source " + const_home_path + "catkin_ws/devel/setup." + terminal):
            cleaned_file_content += (line.splitlines()[0] + "\n")
    file_.close()

    file_ = open(const_home_path + "." + terminal + "rc", 'w')
    file_.write(cleaned_file_content)
    file_.close()

def uninstall_script():
    command = "sudo rm /usr/bin/launch_agrobot.sh"
    os.system(command)

def uninstall_service():
    command = "sudo systemctl disable launch_agrobot.service"
    os.system(command)

    command = "sudo rm /etc/systemd/system/launch_agrobot.service"
    os.system(command)

def uninstall():
    # Removendo a pasta do projeto.
    command = "cd " + const_home_path + " && rm -r catkin_ws/"
    os.system(command)

    # Removendo os sources dos arquivos de configuração dos terminais.
    remove_source("bash")
    remove_source("zsh")

    # Removendo o serviço de auto inicialização.
    uninstall_script()
    uninstall_service()

    print("\nDone.")

uninstall()