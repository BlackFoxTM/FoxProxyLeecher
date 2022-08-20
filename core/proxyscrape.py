import requests , time , json , os
koss = []
def socks4():
    url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all"
    req = requests.get(url)
    open("koskhol.txt","a").write(req.text)
    kos = open("koskhol.txt","r")
    for koso in kos:
        amat = koso.strip("\n")
        if amat != "":
            koss.append(koso.strip("\n"))
    kos.close()
    os.remove("koskhol.txt")
def socks5():
    url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all"
    req = requests.get(url)
    open("koskhol.txt","a").write(req.text)
    kos = open("koskhol.txt","r")
    for koso in kos:
        amat = koso.strip("\n")
        if amat != "":
            koss.append(koso.strip("\n"))
    kos.close()
    os.remove("koskhol.txt")
def http():
    url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"
    req = requests.get(url)
    open("koskhol.txt","a").write(req.text)
    kos = open("koskhol.txt","r")
    for koso in kos:
        amat = koso.strip("\n")
        if amat != "":
            koss.append(koso.strip("\n"))
    kos.close()
    os.remove("koskhol.txt")

