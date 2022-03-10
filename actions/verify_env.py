import re
import sys
import subprocess
from st2common.runners.base_action import Action

class VerifySSHConnection(Action):
    def run(self,accountname):
        CLOUDENV=re.findall("\([a-z0-9]*\)",sys.argv[1])[0][1:-1]
        if (not CLOUDENV):
            raise Exception("Invalid project details")
        cmd_args=["/home/stanley/.magento-cloud/bin/magento-cloud","-q","ssh", "-p",CLOUDENV, "-e", "production","2>/dev/null" ]
        ssh_check=subprocess.run(cmd_args,shell=False)
        if (ssh_check.returncode == 0):
            print(CLOUDENV)
        else:
            raise Exception("Magento Cloud SSH failed!")
