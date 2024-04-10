import sys
import subprocess

def check_ip_address(ip_address):
    try:
        subprocess.run(["ping", "-c", "1", ip_address], check=True)
        return True
    except:
        return False

def gobuster_scan(ip_address):
    wordlist = "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
    command = f"gobuster dir -u http://{ip_address} -w {wordlist} -t 100"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gobuster_scanner.py <IP_ADDRESS>")
        sys.exit(1)

    ip_address = sys.argv[1]

    if not check_ip_address(ip_address):
        print("Invalid IP address")
        sys.exit(1)

    gobuster_scan(ip_address)