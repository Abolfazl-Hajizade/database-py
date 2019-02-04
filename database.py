import sqlite3
import os
from dtectcolors import Style,Fore,Back,init

init() # for colors

global W    ;    W  =   Style.BRIGHT+Fore.WHITE
global GR   ;   GR  =   Style.DIM+Fore.WHITE
global G    ;    G  =   Style.BRIGHT+Fore.GREEN
global C    ;    C  =   Fore.GREEN
global R    ;   R   =   Fore.RED 
global B    ;   B   =   Fore.BLUE
global Y    ;   Y   =   Fore.YELLOW
global O    ;   O   =   Fore.MAGENTA

os.system("cls")
os.system("mode 80,40")

def About():

	print 
	print """
			--- Hello I am Abolfazl Hajizae ---
	
			--- This App For Saving Your Information ---
			
			---- gmail = zeroday1010@gmail.com ----
			
			---- telegram = @zero_d4y ----
			
	
	"""
	raw_input(C+"\n\n\t\t Press Enter To App ....\n"+W)
	
def search_database(name = '' , family = '' , phone = ''):

	list = [name , family , phone]

	list_2 = ['name' , 'family' , 'phone'] 
	
	for search in list:
			for i in list_2:	
				data = database.execute("SELECT ID,name,family,phone,email,id_messanger FROM users WHERE {}='{}'".format(i,search))	
				for row in data:
					print B+"\n---- Acount -----\n"+W
					print GR+"id = "+W+str(row[0])
					print GR+"name = "+W+str(row[1])
					print GR+"family = "+W+str(row[2])
					print GR+"phone = "+W+str(row[3])
					print GR+"email = "+W+str(row[4])
					print GR+"id_messanger = "+W+str(row[5])
					print R+"-------------------------------\n"+W
	print 


def delete_account_database(name = '' , family = '' , phone = '') :

		list = [name , family,phone]
		list_2 = ['name' , 'family' , 'phone']
		for delete in list:
			for i in list_2:
				database.execute("DELETE from users WHERE {}='{}'".format(i,delete))
				database.commit()
		print R+"\n[!]"+GR+" Deleted Account !\n"+W
	
try:
	database = sqlite3.connect("man_data.sqlite")
	print G+"\n----------------------- [+] Connect To Database Now ! -------------------------\n\n"+W
except Exception:
	print Y+"-------------- [!] Connected To Database ! ----------------\n"+W
	
try:
	database.execute("CREATE TABLE users(ID INT NOT NULL , name TEXT,family TEXT,phone TEXT , email TEXT, id_messanger TEXT)")
	#print "Create Table Now !\n"
except Exception:
	pass
	print 


def Banner():

	print R+"\t$-$-$-$-$-$-$-$-$-$-$-$-$-$"+W
	print R+"\t	 							"
	print Y+"\t    Welcome To Database 		"			
	print R+"\t								"
	print R+"\t$-$-$-$-$-$-$-$-$-$-$-$-$-$"+W
	print "\n\n"
Banner()	

while True:
	ch = raw_input(C+"1- "+W+"Add Account\n"+C+"2- "+W+"Display List\n"+C+"3- "+W+"Search\n"+C+"4-"+W+" Delete Account\n"+C+"5-"+W+" About"+C+'\n'+"6-"+W+" Exit\n\n>> ")

	if ch == "1":
		print 
		name = raw_input(R+">"+GR+"Name = "+W)
		family = raw_input(R+">"+GR+"Family = "+W)
		phone = raw_input(R+">"+GR+"phone = "+W)
		email = raw_input(R+">"+GR+"Email = "+W)
		id_messanger = raw_input(R+">"+GR+"ID_Messanger = "+W)
		id = 0
		while True:
			try:
				database.execute("INSERT INTO users(ID , name , family , phone,email,id_messanger) VALUES ({}, '{}','{}','{}','{}','{}')".format(id, name,family,phone,email,id_messanger)+"")
				database.commit()
				break
			except Exception:
				id += 1
				continue
		print G+"\n[+]"+W+" Added User Successfully !\n"

	elif ch == "2":
		data = database.execute("SELECT ID,name,family,phone,email,id_messanger FROM users")
		f = open("data.txt" , "w+")
		print Y+"\n\t---- All List ----\n"+W
		for row in data:
			f.write("id = "+str(row[0])+'\n'+"name = "+str(row[1])+"\n"+"family = "+str(row[2])+'\n'+"phone = "+str(row[3])+'\n'+"email = "+str(row[4])+'\n'+"id_messanger = "+str(row[5])+"\n----------------\n")
			print GR+"id = "+W+str(row[0])
			print GR+"name = "+W+str(row[1])
			print GR+"family = "+W+str(row[2])
			print GR+"phone = "+W+str(row[3])
			print GR+"email = "+W+str(row[4])
			print GR+"id_messanger = "+W+str(row[5])
			print R+"-------------------------------\n"+W
		f.close()
		os.system("data.txt")

	elif ch == "3":
		print 
		name = raw_input("Name ("+R+"if you unknow press enter"+W+") = ")
		
		if name == True or name != '':
			search_database(name)
			continue
		family = raw_input("Family ("+R+"if you unknow press enter"+W+") = ")
		
		if family == True or family != '':
			search_database(family)
			continue
		phone = raw_input("Phone ("+R+"if you unknow press enter"+W+") = ")
		
		if phone == True or phone != '':
			search_database(phone)
			continue
		
		search_database(name , family,phone)
		
	elif ch == "4":
		print 
		name = raw_input("Name ("+R+"if you unknow press enter"+W+") = ")
		
		if name == True or name != '':
			delete_account_database(name)
			continue
		family = raw_input("Family ("+R+"if you unknow press enter"+W+") = ")
		
		if family == True or family != '':
			delete_account_database(family)
			continue
		phone = raw_input("Phone ("+R+"if you unknow press enter"+W+") = ")
		
		if phone == True or phone != '':
			delete_account_database(phone)
			continue
		delete_account_database(name,family,phone)
		
	elif ch == "5":
			
				os.system("cls")
				About()
				os.system("cls")
				Banner()
				continue
		
	elif ch == "6":
		exit()
	else:
		if ch == "cls":
			os.system("cls")
			continue
		else:
			print R+"\n\t  ---- Value Is False ---- \n"+W
			continue



database.close()


