import sys,tty,termios,rospy
from std_msgs.msg import String

rospy.init_node('PcManual', anonymous=True)
pubPc = rospy.Publisher('PcManual', String, queue_size=10)

speed = 0
steer = 0
limit = 50
pa = 0
pb = 0
pc = 0

class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def sendCommand():
        global speed,steer,limit,pa,pb,pc
        command = "0*speed$" + str(speed) + "*steer$" + str(steer) + "*limit$" + str(limit) + "*powerA$" + str(pa) + "*powerB$" + str(pb) + "*pulverize$" + str(pc)
        pubPc.publish(command)

def get():
        global speed,steer,limit,pa,pb,pc
        pa = 0
        pb = 0
        pc = 0
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                speed = speed + 10
                print("up")
        elif k=='\x1b[B':
                speed = speed - 10
                print("down")
        elif k=='\x1b[C':
                steer = steer + 10
                print("right")
        elif k=='\x1b[D':
                steer = steer -10
                print("left")
        elif k=='aaa':
                pa = 1
                print("Enviando sinal para placa A")
        elif k=='bbb':
                pb = 1
                print("Enviando sinal para placa B")
        elif k=='ccc':
                pc = 1
                print("Enviando sinal para pulverizador/UV")
        elif k=='inc':
                limit = limit + 10
        elif k=='dec':
                limit = limit - 10
        elif k=='eee':
                pa = 0
                pb = 0
                pc = 0
                speed = 0
                steer = 0
                limit = 0
                sendCommand(0)
                exit(0)
        sendCommand()

def main():
    print("Instruções: ")
    print("aaa: Envia sinal para a placa A")
    print("bbb: Envia sinal para a placa B")
    print("ccc: Envia sinal para o pulverizador/UV")
    print("eee: Finaliza o programa")
    print("inc: Aumenta o limite")
    print("dec: Diminui o limite")
    print("Setas cima e baixo: Controlam o velocidade")
    print("Setas esq e dir: Controlam o velocidade")
    while(1):
        print("speed: " + str(speed))
        print("steer: " + str(steer))
        print("limit: " + str(limit))
        get()

if __name__=='__main__':
        main()