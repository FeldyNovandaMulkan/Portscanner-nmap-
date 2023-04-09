
import nmap

scanner = nmap.PortScanner()

print("Selamat datang di mini port Scanner")
print("<----------------------------------->")

ip_address = input("Masukkan ip address yang ingin anda scan : ")
print("Ip address yang ingin anda scan : ", ip_address)

type(ip_address)


respon = input(""" \n Pilih Salah satu menu dibawah ini : 
	    1) SYN ACK Scan 
	    2) UDP Scan
	    3) Comprehensive Scan \n """)
print("menu yang anda pilih adalah : ",  respon)

if respon == '1':
	print("nmap version : ", scanner.nmap_version())
	scanner.scan(ip_address, '1-1024', '-v -sS')
	print(scanner.scaninfo())
	print("Ip status : ", scanner[ip_address].state())
	print(scanner[ip_address].all_protocols())
	print("Open Ports : ", scanner[ip_address]['tcp'].keys())
elif respon == '2':
	print("nmap version : ", scanner.nmap_version())
	scanner.scan(ip_address, '1-1024', '-v -sU')
	print(scanner.scaninfo())
	print("Ip status : ", scanner[ip_address].state())
	print(scanner[ip_address].all_protocols())
	print("Open Ports : ", scanner[ip_address]['udp'].keys())
elif respon == '3':
	print("nmap version : ", scanner.nmap_version())
	scanner.scan(ip_address, '1-1024', '-v -sS -sV -sC -A -O')
	print(scanner.scaninfo())
	print("Ip status : ", scanner[ip_address].state())
	print(scanner[ip_address].all_protocols())
	print("Open Ports : ", scanner[ip_address]['tcp'].keys())
else : 
	print("mohon masukkan pilihan menu yang benar!!!!")

