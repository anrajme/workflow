import os

from st2common.runners.base_action import Action

class VerifySSHConnection(Action):
    def run(self,envname,cloudtoken):
        cloudenv=envname
        if (not cloudenv):
            raise Exception("Invalid project details")
        else:
            os.environ['MAGENTO_CLOUD_CLI_TOKEN'] = cloudtoken

            # TODO : needs to use subprocess instead of os.system

            exec_status=os.system('/home/stanley/.magento-cloud/bin/magento-cloud auth:api-token-login -y -q; mkdir -p /root/.ssh; /usr/bin/ssh-keyscan ssh.eu.magentosite.cloud >> /root/.ssh/known_hosts; /usr/bin/ssh-keyscan git.eu.magentosite.cloud >> /root/.ssh/known_hosts; /usr/bin/php /home/stanley/.magento-cloud/bin/magento-cloud ssh -p %s -e production "ls var/.maintenance.flag" 2>/dev/null' % (cloudenv))
            if (exec_status == 0):
                print("Maintenance flag is enabled")
            else:
                print("Maintenance flag not found")