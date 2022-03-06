#!/usr/bin/env bash
CLOUDENV=${1}
if [ ! -z "$CLOUDENV" ];then
  LASTDEPLOY=$(magento-cloud activity:list -p 6fck2obu3244c -e production --columns=Created,State,Result  --limit 1 --format=csv --no-header)
  if [ $? -eq 0 ]; then
    IFS=, read -r DEPLOYDATE DEPLOYSTATUS DEPLOYRESULT <<< $LASTDEPLOY
    if [[ $DEPLOYSTATUS == "in progress" ]]; then
      echo "Deployment is still running"
      echo "Deployment Start Time: $DEPLOYDATE"
      exit 0
    elif [[ $DEPLOYSTATUS == "complete" ]]; then
      echo "Deployment is not running."
      echo "Last Deployment: $DEPLOYDATE --> Deployment Status: $DEPLOYSTATUS --> Deployment Result:$DEPLOYRESULT"
      exit 0
    else
      echo "Deployment status check failed"
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
