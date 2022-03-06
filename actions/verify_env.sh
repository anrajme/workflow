#!/usr/bin/env bash
CLOUDENVSTR=${1}
CLOUDENV=$(echo $CLOUDENVSTR | sed  's/^.*(\(.*\)).*$/\1/g')
if [ ! -z "$CLOUDENV" ];then
  SSHCHECK=$(magento-cloud ssh -p $CLOUDENV -e production echo canconnect 2>&1)
  SSHCHECKOK=$(echo $SSHCHECK | grep canconnect)
  if [[ ! -z "$SSHCHECKOK" ]];then
    echo $CLOUDENV
    exit 0
  else
    echo "Cloud SSH Failed --> $SSHCHECK"
    exit 1
  fi
else
   echo "Invalid Environment name"
  exit 2
fi
