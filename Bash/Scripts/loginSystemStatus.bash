#!/bin/bash
### Bash script to check system configurations and usage on login
### (Add to bash.rc to auto run on login)

#loading text
echo "Starting system_check script..."
clear
echo

# VARIABLE ASSIGNMENT
# Show hostname:
HOST=$(hostname)
# User executing the script:
CURRENTUSER=$(whoami)
# Current date:
CURRENTDATE=$(date)
# Host IP address:
IPADDRESS=$(hostname -I | cut -d ' ' -f1)
# System information
SYSINFOk=$(uname -s) #kernal name
SYSINFOn=$(uname -n) #node name
SYSINFOr=$(uname -r) #kernal release
SYSINFOv=$(uname -v) #kernal version
SYSINFOm=$(uname -m) #machine name
SYSINFOp=$(uname -p) #processor type
SYSINFOo=$(uname -o) #operation system
# Disk usage info
DISKUSAGE=$(df -h)
# Who is logged in and uptime
WHO=$(w)
# Highest usage processes
PROS_HEADER=$(ps aux | head -n 1)
PROS=$(ps aux | sort -nrk 3,3 | head -n 5)

# SHOW MESSAGES
echo "Hello $CURRENTUSER!"
echo
echo "Today is: $CURRENTDATE"
echo "Hostname: $HOST     IP:($IPADDRESS)"
echo
echo "System information:"
echo -e "Kernal name:\t$SYSINFOk"
echo -e "Node name:\t$SYSINFOn"
echo -e "Kernel Release:\t$SYSINFOr"
echo -e "Kernel Version:\t$SYSINFOv"
echo -e "Machine Name:\t$SYSINFOm"
echo -e "Processor type:\t$SYSINFOp"
echo -e "Operating System:\t$SYSINFOo"
echo
echo "Disk Usage:"
echo "$DISKUSAGE"
echo
echo "Top Processes:"
echo "$PROS_HEADER"
echo "$PROS"
echo
echo "Currently logged in users:"
echo "$WHO" | tail -n -1
