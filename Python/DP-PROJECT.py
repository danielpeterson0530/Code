mport os
import sys
import subprocess
from datetime import datetime

def main():
    output = run_modules()
    outputinfo, outputfilename, outputfile_fullpath = process_save_outputfile(output)
    print(output)
    
def run_modules(): 
    def run_module(cmdstr):
        cmd = create_command(cmdstr)
        rawoutput = run_subprocess(cmd)
        out = rawoutput.stdout.decode("utf-8")
        output = "COMMAND: \'" + cmdstr + "\'" + "\n" + "-"*20 + "START"+ "-"*20 + "\n" + out
        return output
    cmds = ["nmcli device show", 
            "ping -c4 8.8.8.8",
            "ping -c4 www.yahoo.com",
            "traceroute -n www.yahoo.com",
            "nslookup www.yahoo.com",
            "resolvectl"]
    header = "\n".join(("\nDate:\n  "+get_date(), "\nCommands run:", *["  "+c for c in cmds], "\nCommand Outputs:\n\n")) 
    all_output = header
    for cmd in cmds:
        print("Running: " + cmd)
        output = run_module(cmd)
        all_output = "\n".join((all_output, output + "-"*21 + "END"+ "-"*21, "\n\n"))
    return all_output
    
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

def prompt_confirm(prompt_str):
    while True:
        response = input(prompt_str)
        res = str(input("You've entered: (" + response + ") is this correct? (y/n)\n"))
        if res in ('y', 'Y', 'yes', 'YES', 'Yes'):
            return response
        elif res in ('n', 'N', 'no', 'NO', 'No'): 
            continue
        else:
            print("Incorrect response. Please try again.")

def prompt_outputfilename(output):
    while True:
        res = input("\nDo you want to save output to file? (y/n)\n")
        if res in ('y', 'Y', 'yes', 'YES', 'Yes'):
            apnresponse = prompt_confirm("Please enter the APN name:\n")
            devresponse = prompt_confirm("Please enter the Test Device Number:\n")
            return apnresponse, devresponse
        elif res in ('n', 'N', 'no', 'NO', 'No'): 
            program_exit(output)
        else:
            print("Incorrect response. Please try again.")

def process_save_outputfile(output):
    apnname, devicenumber = prompt_outputfilename(output)
    outdir = check_and_make_outdirs(devicenumber)
    currentdate = get_date()
    outputinfo = "".join((currentdate,"_APN",apnname,"_Device",devicenumber))
    outputfilename = "".join((outputinfo, "_TestResults.mcs",))
    outputfile_fullpath = "".join((outdir, outputfilename))
    if exists(outputfile_fullpath):
        res = input("".join(("File: (", outputfile_fullpath, ") already exists. Overwrite? (y/n)")))
        while True:
            if res in ('y', 'Y', 'yes', 'YES', 'Yes'):
                write_file(outputfile_fullpath, output)
                print("Output written to: " + outputfile_fullpath)
                break
            elif res in ('n', 'N', 'no', 'NO', 'No'): 
                program_exit(output)
            else:
                print("Incorrect response. Please try again.")
    else:
        write_file(outputfile_fullpath, output)
        print("Output written to: " + outputfile_fullpath)
    return outputinfo, outputfilename, outputfile_fullpath

def get_user_home():
    return os.path.expanduser('~')

def check_and_make_outdirs(devicenumber):
    userhomedir = get_user_home()
    dir1 = "".join((userhomedir, "/test", devicenumber))
    dir2 = "".join((dir1, "/documents"))
    dir3 = "".join((dir2, "/test", devicenumber, "_customer-captures/"))
    for directory in [dir1, dir2, dir3]:
        if not exists(directory):
            os.makedirs(directory)
    return dir3

def get_date():
    return datetime.today().strftime("%Y-%m-%d")

def get_full_path(file):
    return os.path.abspath(file)

def exists(item):
    return os.path.exists(item)

def write_file(file, content):
    with open(file, "w") as f:
        f.write(content)
    f.close()

def program_exit(output):
    print("File not written. Program complete.")
    print("Printing output: \n\n")
    print(output)
    quit()

main()
