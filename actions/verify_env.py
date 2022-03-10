import re
import sys
import subprocess

def check_ssh_connection(CLOUDENV):
    cmd_args=["/home/stanley/.magento-cloud/bin/magento-cloud","-q","ssh", "-p",CLOUDENV, "-e", "production","2>/dev/null" ]
    ssh_check=subprocess.run(cmd_args,shell=False)
    return(ssh_check.returncode)

if __name__=="__main__":
    if len(sys.argv) < 2:
        raise ValueError("Usage: check_env.py <project_id>")

    CLOUDENV=re.findall("\([a-z0-9]*\)",sys.argv[1])[0][1:-1]

    if (not CLOUDENV):
        raise Exception("Invalid project details")
    else:
        ssh_status=check_ssh_connection(CLOUDENV)
        if (ssh_status == 0):
            print(CLOUDENV)
        else:
            raise Exception("Magento Cloud SSH failed!")
