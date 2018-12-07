#!/usr/bin/python
#coding:utf-8

# export ppp=/home/kc/Desktop/w/code/my/MyPython/myshell.py   shell中

import sys
import os

if  len(sys.argv) > 1 and 'gradle'==sys.argv[1]:
	print '1  gradle :launcher:installDebug'
	print '2  gradle :browser:installDebug'
	name = raw_input('请选择')
	if '1'==name : 
		print os.system("gradle :launcher:installDebug")
	elif '2'==name:
		print os.system("gradle :browser:installDebug")
	exit();
		
	
#else : 
#	name = raw_input('请选择');









command1="adb shell \"dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp'\""
command=""
command += command1;
print command



command=""
command += "adb shell monkey -p com.qihoo.browser -v 20000"
print command

command=""
command += "adb shell ps | grep monkey"
print command

 

command=""
command += "adb shell dumpsys meminfo com.qihoo.browser"
print command

command=""
command += "native crash:"
print command

command=""
command += "       find . | xargs grep 'crash' -in\n"
command += "       find . | xargs grep 'About message' -in\n"
command += "       find . | xargs grep ' signal ' -in\n"
command += "       find . | xargs grep 'FATAL:memory' -in\n"
print command


command=""
command += "java crash:\n"
command += "       find . | xargs grep 'find . | xargs grep 'fatal' -in -A 3 | grep browser -n' -in\n"
print command





command="ANR: \n"
command += "       find . | xargs grep 'Cmd line: com.qihoo.browser' -in\n"
command += "       find . | xargs grep 'ANR in com.qihoo.browser' -in\n"
command += "       find . | xargs grep 'WaitingPerformingGc' -in\n"
print command

command="other:"
command += "      vi file +num"
print command



