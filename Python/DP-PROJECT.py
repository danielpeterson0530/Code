import os
import sys
import subprocess

def main():
    #run_ping("8.8.8.8")
    #run_nmcli()
    run_traceroute("www.yahoo.com")

def create_command(cmdstr):
    return cmdstr.split(" ")

def write_output(rawoutput):
    print(rawoutput)

def run_subprocess(cmd):
    output = subprocess.run(cmd, capture_output=True)
    if output.returncode != 0:
        err = output.stderr.decode("utf-8")
        out = output.stdout.decode("utf-8")
        sys.exit("\n".join(("Process returned a non-zero exit status:",err,out)))
    else:
        return output

def check_install():"
    
def run_ping(location):
    cmd = create_command("ping -c4 " + str(location))
    rawoutput = run_subprocess(cmd)
    write_output(rawoutput)
    return

def run_nmcli():
    cmd = create_command("nmcli device show")
    rawoutput = run_subprocess(cmd)
    write_output(rawoutput)
    return
    
def run_traceroute(location):
    cmd = create_command("traceroute -n" + str(location))
    rawoutput = run_subprocess(cmd)
    write_output(rawoutput)
    return
