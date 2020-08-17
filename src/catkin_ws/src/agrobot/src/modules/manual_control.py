#!/usr/bin/env python3

"""
Módulo que permite o controle do robô por meio do terminal.
È necessário rodar esse programa em um terminal no qual o roscore esteja definido/rodando.
"""

# ------------- #
# -> Imports <- #
# ------------- #

import sys,tty,termios,rospy
from std_msgs.msg import String

# ---------------- #
# -> Constantes <- #
# ---------------- #

const_pub_log: rospy.Publisher = rospy.Publisher('log', String, queue_size=10)
const_pub_pc: rospy.Publisher = rospy.Publisher('pc_manual', String, queue_size=10)

# ------------------- #
# -> Configurações <- #
# ------------------- #

rospy.init_node('pc_manual', anonymous=True)

# ------------- #
# -> Funções <- #
# ------------- #

## Função que envia os comandos para o robô.
def send_command(speed: str,steer: str,limit: str,pa: str,pb: str,pc: str):
        command = "0*speed$" + speed + "*steer$" + steer + "*limit$" + limit + "*powerA$" + pa + "*powerB$" + pb + "*pulverize$" + pc
        const_pub_pc.publish(command)

## Função que recebe e processa os comandos enviados pelo terminal.
def get():
        inkey = _Getch()
        speed = 0
        steer = 0
        limit = 0
        pa = 0
        pb = 0
        pc = 0
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
                send_command(str(speed),str(steer),str(limit),str(pa),str(pb),str(pc))
                exit(0)
        send_command(str(speed),str(steer),str(limit),str(pa),str(pb),str(pc))
        return speed,steer,limit

## Função que imprime as instruções na tela e roda o código.
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
        speed,steer,limit = get()
        print("speed: " + str(speed))
        print("steer: " + str(steer))
        print("limit: " + str(limit))


# ------------- #
# -> Classes <- #
# ------------- #

## Classe que gerencia a captura de teclas pelo terminal.
class _Getch:
        ## Método que captura as teclas apertadas no terminal.
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

# ------------------------- #
# -> Execução de códigos <- #
# ------------------------- #

if __name__=='__main__':
        try:
            const_pub_log.publish('startedFile$ManualControl')
            main()
        except:
            const_pub_log.publish("error$Fatal$Could not start manual_control.py.")