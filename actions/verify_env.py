import re
import sys
import subprocess
from st2common.runners.base_action import Action

class VerifySSHConnection(Action):
    def run(self,CLOUDENV):
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
        ssh_status=VerifySSHConnection()
        ssh_return=ssh_status.run(CLOUDENV)
        if (ssh_return == 0):
            print(CLOUDENV)
        else:
            raise Exception("Magento Cloud SSH failed!")
