#!/bin/bash
if [ "$2" == "" ]
then 
	set "fix"
fi
git status
git add .
git commit -m $2
git push origin $1
echo "==========提交成功=========="
