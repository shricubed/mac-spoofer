import subprocess
import string
import random
import re

def generate_address():
    upperhex = ''.join(set(string.hexdigits.upper()))
    addr = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                addr += random.choice('02468ACE')
            else:
                addr += random.choice(upperhex)

        addr += ":"
    return addr.strip(":")

def get_mac(iface):
    output = subprocess.check_output(f"ifconfig {iface}", shell=True).decode()
    return re.search("ether (.+) ", output).group().split()[1].strip()

def spoof(iface, addr):
    subprocess.check_output(f"ifconfig {iface} down", shell=True)
    subprocess.check_output(f"ifconfig {iface} hw ether {addr}", shell=True)
    subprocess.check_output(f"ifconfig {iface} up", shell=True)




