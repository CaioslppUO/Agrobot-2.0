import rospy
from std_msgs.msg import String

log_folder = '../logs/'

started_files_path = log_folder + 'startedFiles.log'
errors_file_path = log_folder + 'errors.log'

## Método que limpa os arquivos ao abrir o programa
def cleanFiles(files_path):
    for f in files_path:
        file_ = open(f, 'w')
        file_.close()

#Limpando os arquivos
cleanFiles([started_files_path,errors_file_path])

def writeError(error_severity,error_msg):
    file_ = open(errors_file_path, 'a')
    file_.write('[' + error_severity + '] ' + error_msg + '\n')
    file_.close()

def callback(msg):
    info = (msg.data).split('$')

    if(info[0] == "startedFile"):
        file_ = open(started_files_path, 'a')
        file_.write(str(info[1]) + ': Started\n')
        file_.close()
        
    elif(info[0] == "error"):
        writeError(str(info[1]), str(info[2]))

def listen():
    rospy.init_node('Log', anonymous=True)
    rospy.Subscriber('Log', String, callback)
    rospy.spin()

listen()