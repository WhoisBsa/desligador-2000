import os, time, platform
from datetime import datetime

def desligar(tempo):
    if platform.system() == 'Windows':
        comando = 'shutdown -s -t ' + str(tempo)
        return os.system(comando)
    elif platform.system() == 'Linux':
        comando = 'sudo shutdown -h ' + str(tempo)
        return os.system(comando)
    else:
        return 'Sistema Operacional desconhecido!'

def cancelar():
    if platform.system() == 'Windows':
        return os.system('shutdown /a')
    elif platform.system() == 'Linux':
        return os.system('sudo shutdown -c')
    else:
        return 'Sistema operacional desconhecido!'

def horaDesligar(hora,minuto):
    desligar = '{}:{}'.format(hora,minuto)
    hora_desligar = datetime.strptime(desligar, '%H:%M')

    atual = datetime.now()
    atual = atual.strftime('%H:%M')
    hora_atual = datetime.strptime(atual, '%H:%M')

    #hora_inicio = int(datetime.strptime(atual, '%H:%M').strftime("%H"))
    #minuto_inicio = int(datetime.strptime(atual, '%H:%M').strftime("%M"))
    #hora_atual = int(datetime.strptime(desligar, '%H:%M').strftime("%H"))
    #minuto_final = int(datetime.strptime(desligar, '%H:%M').strftime("%M"))

    if hora_atual < hora_desligar:
        segundos = abs((hora_desligar - hora_atual).seconds)
        return segundos
    else:
        return 'xxx'

'''
a = horaDesligar(17,45)

if a != 'xxx':
    desligar(a)
else:
    print('Hora menor que a atual!')
'''

#time.sleep(10)

