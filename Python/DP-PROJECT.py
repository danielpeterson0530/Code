import os
import sys
import subprocess
import datetime

def main():
    #run_nmcli()
    #run_ping("8.8.8.8")
    #run_ping("www.yahoo.com")
    #run_traceroute("www.yahoo.com")
    #run_nslookup("www.yahoo.com")
    #run_resolvectl()
    outputinfo, outputfilename = get_prompt_response()

def create_command(cmdstr):
    return cmdstr.split(" ")

def run_subprocess(cmd):
    output = subprocess.run(cmd, capture_output=True)
    if output.returncode != 0:
        err = output.stderr.decode("utf-8")
        out = output.stdout.decode("utf-8")
        sys.exit("\n".join(("Process returned a non-zero exit status:",err,out)))
    else:
        return output
    
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
    cmd = create_command("traceroute -n " + str(location))
    rawoutput = run_subprocess(cmd)
    write_output(rawoutput)
    return

def run_nslookup(location):
    cmd = create_command("nslookup " + str(location))
    rawoutput = run_subprocess(cmd)
    write_output(rawoutput)
    return

def run_resolvectl():
    cmd = create_command("resolvectl")
    rawoutput = run_subprocess(cmd)
    write_output(rawoutput)
    return

def apn_prompt():
    return input("Please enter the APN name:\n")

def device_prompt():
    return input("Please enter the Test Device Number:\n")

def get_prompt_response():
    while True:
        apnresponse = apn_prompt()
        response = str(input("You've entered: (" + apnresponse + ") is this correct? (y/n)\n"))
        if response in ('y', 'Y', 'yes', 'YES', 'Yes'):
            break
    while True:
        devresponse = device_prompt()
        response = str(input("You've entered: (" + devresponse + ") is this correct? (y/n)\n"))
        if response in ('y', 'Y', 'yes', 'YES', 'Yes'):
            break
    return apnresponse, devresponse

def prompt_output_filename():
    apnname, devicenumber = get_prompt_response()
    outputinfo = "".join(("APN_",apnname,"_Device_",devicenumber))
    outputfilename = "".join((outputinfo, "_Test_Results.mcs",))
    return outputinfo, outputfilename

def get_datetime():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def get_full_path(file):
    return os.path.abspath(file)

def check_file_exists(file):
    return os.path.exists(file)

def save_file():
    get_full_path(file)
    check_file_exists(file)
    return

def sendmail_mailutils(outputinfo, outputfilename):
    outputfile_fullpath = get_full_path(outputfilename)
    dateandtime = get_datetime()
    subject = " ".join((outputinfo, dateandtime))
    message = "\n".join((outputfilename, outputinfo, dateandtime))
    email_address = "danielpeterson0530@gmail.com" #"dp7285@att.com"
    cmd = create_command(" ".join(("echo", message, "| mail -s", subject, email_address, "-A", outputfile_fullpath)))
    rawoutput = run_subprocess(cmd)
    return
