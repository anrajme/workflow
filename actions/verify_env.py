import re
import sys
import subprocess
import os

from st2common.runners.base_action import Action

class VerifySSHConnection(Action):
    def run(self,accountname,cloudtoken):
        cloudenv=re.findall("\([a-z0-9]*\)",accountname)[0][1:-1]
        if (not cloudenv):
            raise Exception("Invalid project details")
        else:
            os.environ['MAGENTO_CLOUD_CLI_TOKEN'] = cloudtoken

            # TODO : needs to use subprocess instead of os.system

            exec_status=os.system('/home/stanley/.magento-cloud/bin/magento-cloud auth:api-token-login -y -q; ssh-keyscan 'ssh.eu.magentosite.cloud' >> /home/stanley/.ssh/known_hosts; ssh-keyscan 'git.eu.magentosite.cloud' >> /home/stanley/.ssh/known_hosts; /usr/bin/php /home/stanley/.magento-cloud/bin/magento-cloud ssh -p %s -e production 2>&1 " "' % (cloudenv))
            if (exec_status == 0):
                print("Successfully connected to Magento Cloud Instance via SSH")
            else:
                raise Exception("SSH conection attempt failed!")
