import os
import sys
import subprocess
from datetime import datetime

def main():
    devicenumber = "1"
    output = run_modules()
    process_save_outputfile(output, devicenumber)
    program_exit()
    
def run_modules(): 
    def create_command(cmdstr):
        return cmdstr.split(" ")
    def run_subprocess(cmd):
        output = subprocess.run(cmd, capture_output=True)
        if output.returncode != 0:
            erroutput = "\n".join(("Process returned a non-zero exit status:",output.stdout.decode("utf-8"),output.stderr.decode("utf-8")))
            return erroutput
        else:
            return output.stdout.decode("utf-8")
    def create_header(cmds):
        return "\n".join(("\nDate:\n  "+get_date(), "\nCommands run:", *["  "+c for c in cmds], "\nCommand Outputs:\n\n"))
    def run_module(cmdstr):
        cmd = create_command(cmdstr)
        output = run_subprocess(cmd)
        processed_output = "COMMAND: \'" + cmdstr + "\'" + "\n" + "-"*20 + "START"+ "-"*20 + "\n" + output + "-"*21 + "END"+ "-"*21 + "\n\n\n"
        print(processed_output)
        return processed_output
    def prompt_ping():
        response = prompt_only("Run additional ping? (Type [ADDRESS] for Yes, 'n' for No)\n")
        if response == False:
            return False, False
        else:
            cmd = "ping -c4 " + response
            print("\n\n")
            processed_output = run_module(cmd)
            return processed_output, cmd
    cmds = ["nmcli device show eth0", 
            "ping -c4 8.8.8.8",
            "ping -c4 www.yahoo.com",
            "traceroute -n www.yahoo.com",
            "nslookup www.yahoo.com",
            "resolvectl"]
    concat_output = ""
    for cmd in cmds:
        processed_output = run_module(cmd)
        concat_output = "\n".join((concat_output, processed_output))
    while True:
        processed_output, cmd = prompt_ping()
        if processed_output == False:
            break
        else:
            cmds.append(cmd)
            concat_output = "\n".join((concat_output, processed_output))
    header = create_header(cmds)
    concat_output = header + "\n" + concat_output
    return concat_output

def process_save_outputfile(output, devicenumber):
    def check_and_make_outdirs(devicenumber):
        userhomedir = get_user_home()
        dir1 = "".join((userhomedir, "/Documents"))
        dir2 = "".join((dir1, "/Test", devicenumber, "-customer-captures/"))
        for directory in [dir1, dir2]:
            if not exists(directory):
                os.makedirs(directory)
        return dir2
    def get_user_home():
        return os.path.expanduser('~')
    def get_full_path(file):
        return os.path.abspath(file)
    def exists(item):
        return os.path.exists(item)
    def write_file(file, content):
        with open(file, "w") as f:
            f.write(content)
        f.close()
    def check_overwrite(outputfile_fullpath):
        if exists(outputfile_fullpath):
            res = prompt_only("".join(("File: (", outputfile_fullpath, ") already exists. Overwrite? (Type [ANY KEY] for Yes, 'n' for No)")))
            if res in ('n', 'N', 'no', 'NO', 'No'):
                program_exit("File not written. ")
            else:
                return
    def process_outputfilename(apnname, devicenumber, datacenter):
        outdir = check_and_make_outdirs(devicenumber)
        currentdate = get_date()
        outputinfo = "".join((currentdate,"_", datacenter, "_APN-",apnname,"_Device-",devicenumber))
        outputfilename = "".join((outputinfo, "_TestResults.mcs",))
        outputfile_fullpath = "".join((outdir, outputfilename))  
        return outputfile_fullpath
    apnname = prompt_only("\nType APN to save output to file: (Type APN (numbers-only) for Yes, 'n' for no)\n")
    if apnname == False:
        program_exit("File not written. ")
    datacenter = prompt_only("\nEnter data-center code:\n")
    output = "Data center:\n  " + datacenter + "\n" + output
    outputfile_fullpath = process_outputfilename(apnname, devicenumber, datacenter)
    check_overwrite(outputfile_fullpath)
    write_file(outputfile_fullpath, output)
    print("\n\nOutput written to: " + outputfile_fullpath)
    return

def get_date():
    return datetime.today().strftime("%Y-%m-%d")

def prompt_only(prompt_str):
    response = input(prompt_str)
    response.replace(" ", "_")
    if response in ('n', 'N', 'no', 'NO', 'No'):
        return False
    else:
        return response

def program_exit(exit_string = ""):
    print(exit_string + "Program complete.")
    quit()
