#!/usr/bin/env bash
FLAGSTATUS=${1}
if [ ! -z "$FLAGSTATUS" ];then
  if [[ $FLAGSTATUS == "Deployment Not Running" ]];then
    exit 0
  else
    exit 1
  fi
else
  exit 2
fi
