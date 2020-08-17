import os,pathlib

current_path: str = str(pathlib.Path(__file__).parent.absolute()) + "/"

os.system("sudo python3 " + current_path + "uninstall_ros_code.py && python3 " + current_path + "install_ros_code.py")