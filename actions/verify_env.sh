#!/usr/bin/env bash
CLOUDENVSTR=${1}
CLOUDENV=$(echo $CLOUDENVSTR | sed  's/^.*(\(.*\)).*$/\1/g')
if [ ! -z "$CLOUDENV" ];then
  SSHCHECK=$(magento-cloud ssh -p $CLOUDENV -e production echo ok 2>&1 | grep "ok")
  if [[ ! -z "$SSHCHECK" && $SSHCHECK == "ok" ]];then
    echo $CLOUDENV
    exit 0
  else
    exit 1
  fi
else
  exit 2
fi
