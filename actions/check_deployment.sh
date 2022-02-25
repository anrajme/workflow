#!/usr/bin/env bash
CLOUDENV=${1}
if [ ! -z "$CLOUDENV" ];then
  FLAGCHECK=$(magento-cloud environment:ssh -p $CLOUDENV -e production "ls var/.maintenance.flag" 2>&1 | grep "ls\|.maintenance.flag")
  if [ $? -eq 0 ]; then
    if [[ $FLAGCHECK == "ls: cannot access var/.maintenance.flag: No such file or directory" ]]; then
      echo "Deployment Not Running"
      exit 0
    elif [[ $FLAGCHECK == "var/.maintenance.flag" ]]; then
      echo "Deployment Running"
      exit 0
    else
      echo "Maintenance flag check failed"
      exit 1
    fi
  else
    echo "Cloud Command Failed"
    exit 2
  fi
else
  echo "Cloud Name Not Set"
  exit 3
fi
