import sys
import subprocess
import os
from datetime import datetime
import socket

HOSTNAME_FILE = "/etc/hostname"

def show_help():
	try:
		with open('help_message.txt','r') as file:
			help_message = file.readlines()
			for line in help_message:
				print(line.strip())
	except FileNotFoundError:
		print("No s'ha troabt el fitxer d'ajuda.")
	except Exception as e:
		print(f"Error al llegir l'arxiu d'ajuda: {e}")

def show_menu():
	print("Benvingut al meu menu")
	print("1.Canviar nom al host")
	print("2.Executar script en Bash")
	print("3.Fichers")
	print("4.Sortir")
	print("\n")

	opcio = input("Selecciona una opció: ")
	return opcio

def canviar_nom_host():
	nou_hostname = input("Ingresa el nou nom de host:")
	print("\n")
	try:
		socket.sethostname(nou_hostname)

		with open(HOSTNAME_FILE, 'w') as file:
			file.write(nou_hostname)
		print(f"El nom de host s'ha canviat correctament a: {nou_hostname}")
		print("\n")

		with open(HOSTNAME_FILE, 'r') as file:
			contingut = file.read()
			print(f"Contingut del arxiu {HOSTNAME_FILE}:")
			print(contingut)

		print()
	except Exception as e:
		print(f"Error al canviar el nom de host: {e}")
		print("\n")

def executar_script_bash(parametre1, parametre2, parametre3):
	try:
		subprocess.run(["./bash_script.sh", parametre1, parametre2, parametre3], check=True)
		print("El script de Bash s'ha executat correctament.")
		print("\n")
	except FileNotFoundError:
		print("No s'ha trobat el fitxer del script Bash.")
	except subprocess.CalledProcessError:
		print("Error al executar el script bash")

def operacions_amb_arxiu(parametre1, parametre2, parametre3):
	print("Realitzant operacions amb fichers...")
	arxius_txt=[f for f in os.listdir() if f.startswith('operacions') and f.endswith('.txt')]
	if arxius_txt:
		for arxiu in arxius_txt:
			with open(arxiu, 'a') as f:
				data_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				f.write(f"Nom: {parametre1}\n")
				f.write(f"Cognom: {parametre2}\n")
				f.write(f"Edat: {parametre3}\n")
				f.write(f"Data i hora d'escriptura: {data_hora_actual}")
			print(f"S'ha escrit l'informacio en el fitxer '{arxiu}'")
			print("\n")
	else:
		nom_arxiu = 'operacions.txt'
		with open(nom_arxiu ,'w') as f:
			data_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			f.write(f"Nom: {parametre1}\n")
			f.write(f"Cognom: {parametre2}\n")
			f.write(f"Edat: {parametre3}ªn")
			f.write(f"Data i hora d'escriptura: {data_hora_actual}")
		print(f"S'ha escrit l'informacio en el fitxer '{nom_arxiu}'")
		print("\n")

if __name__ == "__main__":
	if len(sys.argv) != 4 or sys.argv[1] in ['-help', '-man']:
		show_help()
		sys.exit()

	parametre1 = sys.argv[1]
	parametre2 = sys.argv[2]
	parametre3 = sys.argv[3]

	while True:
		opcio = show_menu()

		if opcio == "1":
			canviar_nom_host()
		elif opcio == "2":
			executar_script_bash(parametre1, parametre2, parametre3)
		elif opcio == "3":
			operacions_amb_arxiu(parametre1, parametre2, parametre3)
		elif opcio == "4":
			print("Sortint del programa....")
			break
		else:
			print("Opció no valida, intenta-ho un altre cop.;(")


