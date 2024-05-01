#!/bin/bash

# enter the IP address
echo "Enter IP Address: "
read IP

# enter the wordlist
echo "Here are the wordlist choices:"
echo "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
echo "/usr/share/wordlists/dirb/common.txt"

echo "Enter wordlist: "
read wordlist

# run gobuster command
gobuster dir -u $IP -w $wordlist -t 100



