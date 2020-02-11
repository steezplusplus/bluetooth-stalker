import time
from bluetooth import *

def findAirPods(alreadyFound, oui):
    found = discover_devices(lookup_names=True)
    for (addr, name) in found:
        if addr not in alreadyFound:
            print('[*] Found Bluetooth Device: ' + str(name))
            print('[+] Mac Address: ' + str(addr))
            alreadyFound.append(addr)

def main():
    alreadyFound = []
    airpodOUI = "50:DE:06" # Guess at what the OUI is
    airpodOUI2 = "F4:AF:E7"
    while True:
        print('[-] Scanning for Bluetooth devices')
        findAirPods(alreadyFound, )
        time.sleep(5)

if __name__ == "__main__":
    main()
