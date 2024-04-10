import sys
import subprocess
#run as sudo in /usr/share/nmap/scripts/vulscan


def check_ip_address(ip_address):
    try:
        subprocess.run(["ping", "-c", "1", ip_address], check=True)
        return True
    except:
        return False

def nmap_scan(ip_address):
    command = f"nmap -sC -sV -A -O -T4 -p- --script vuln --script vulners {ip_address}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 nmap_scanner.py <IP_ADDRESS>")
        sys.exit(1)

    ip_address = sys.argv[1]

    if not check_ip_address(ip_address):
        print("Invalid IP address")
        sys.exit(1)

    nmap_scan(ip_address)
