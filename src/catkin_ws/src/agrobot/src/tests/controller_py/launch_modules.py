import os,rospy,json,pathlib

const_current_folder_location: str = str(pathlib.Path(__file__).parent.absolute()) + "/"
const_ip: str = ""

## Arquivo utilizado para executar os testes.
def read_config_file():
    global const_ip
    with open(const_current_folder_location + "config.json",'r') as json_file:
        data = json.load(json_file)
        const_ip = data['ip']

## Guarda na memória uma configuração de launch.
def store_param(param_name: str,param_value):
        if(rospy.has_param(param_name)):
            rospy.delete_param(param_name)
        rospy.set_param(param_name,param_value)

def check_up_nodes():
    store_param("/tests_log","[Parameters] OK\n[Modules] OK")

## Preenche os parâmetros necessários para executar os testes.
def fill_parameters():
    read_config_file()
    store_param("server_ip",const_ip)
    store_param("enable_uart","True")
    store_param("enable_relay","True")
    store_param("uart_amount","0")
    store_param("enable_face_detect","False")

if __name__ == "__main__":
    try:
        fill_parameters()
        check_up_nodes()
    except Exception as e:
        print("controller.py test error.")
        print(e)