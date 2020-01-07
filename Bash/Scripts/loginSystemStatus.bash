#!/bin/bash
### .bashrc script to see system configuration/usage on login

clear
IFS=' ' read s n r m p o <<< $(uname -snrmpo)
echo "Hello $(whoami)!"
echo
echo "Today is: $(date)"
echo -e "Hostname: $(hostname)\tIP:($(hostname -I | cut -d ' ' -f1))"
echo
echo "System information:"
echo -e "Kernal name:\t$s"
echo -e "Node name:\t$n"
echo -e "Kernel Release:\t$r"
echo -e "Kernel Version:\t$(uname -v)"
echo -e "Machine Name:\t$m"
echo -e "Processor type:\t$p"
echo -e "Operating System:\t$o"
echo
echo "Disk Usage:"
echo "$(df -h)"
echo
echo "Top Processes:"
echo "$(ps aux | head -n 1)"
echo "$(ps aux | sort -nrk 3,3 | head -n 5)"
echo
echo "Currently logged in users:"
echo "$(w | tail -n -1)"
