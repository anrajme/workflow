#!/usr/bin/env bash
CLOUDENV=${1}
if [ ! -z "$CLOUDENV" ];then
  magento-cloud environment:ssh -p $CLOUDENV -e staging "df -h"
else
  echo "Cloud Name Not Set"
  exit 1
fi