from core import proxyscrape
import os

if os.path.exists("proxy_list.txt") == True:
    os.remove("proxy_list.txt")

def http():
    kiri = open("proxy_list.txt","a")
    proxyscrape.http()
    for pedaret in proxyscrape.koss:
        kiri.write(pedaret + "\n")
def socks4():
    kiri = open("proxy_list.txt","a")
    proxyscrape.socks4()
    for pedaret in proxyscrape.koss:
        kiri.write(pedaret + "\n")
def socks5():
    kiri = open("proxy_list.txt","a")
    proxyscrape.socks5()
    for pedaret in proxyscrape.koss:
        kiri.write(pedaret + "\n")
