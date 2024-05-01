#!/bin/bash
# simple bash nmap scan for all ports with service discovery 
echo "Enter IP Adress: "
read IP
echo "Enter starting port: "
read SP
echo "Enter ending port: "
read EP
nmap -sC -sV -A -O -p$SP-$EP $IP




