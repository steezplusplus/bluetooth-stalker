import time
from bluetooth import *

def findAirPods(alreadyFound):
    found = discover_devices(lookup_names=True)
    for (addr, name) in found:
        if addr not in alreadyFound:
            print('[*] Found Bluetooth Device: ' + str(name))
            print('[+] Mac Address: ' + str(addr))
            alreadyFound.append(addr)

def main():
    alreadyFound = []
    while True:
        print('[-] Scanning for Bluetooth devices')
        findAirPods(alreadyFound, )
        time.sleep(5)

if __name__ == "__main__":
    main()

