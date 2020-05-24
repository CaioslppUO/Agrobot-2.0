import rospy
from std_msgs.msg import String

log_folder = '../logs/'

started_files_path = log_folder + 'startedFiles.log'

#Limpando os arquivos
file_ = open(started_files_path, 'w')
file_.close()

def callback(msg):
    info = (msg.data).split('$')

    if(info[0] == "startedFile"):
        file_ = open(started_files_path, 'a')
        file_.write(str(info[1]) + ': Started\n')
        file_.close()

def listen():
    rospy.init_node('Log', anonymous=True)
    rospy.Subscriber('Log', String, callback)
    rospy.spin()

listen()