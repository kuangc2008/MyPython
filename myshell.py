#!/usr/bin/python
#coding:utf-8


# export ppp=/home/kc/Desktop/w/code/my/MyPython/myshell.py   shell中

import sys
import os
import commands
import commands
import re

if  len(sys.argv) > 1 and 'gradle'==sys.argv[1]:
	if  len(sys.argv) > 2 :
		if '1'==sys.argv[2]: 
			print os.system("gradle :launcher:installDebug")
		elif '2'==sys.argv[2]: 
			print os.system("gradle :browser:installDebug")

		elif '3'==sys.argv[2]: 
			print os.system("gradle :b_p_browser:installDebug")

		elif '4'==sys.argv[2]: 
			print os.system("gradle :b_launcher:installApmDebug")
		exit();
	else:
		print '1  gradle :launcher:installDebug'
		print '2  gradle :browser:installDebug'
		print '3  ./gradlew :b_p_browser:installDebug'
		print '4  ./gradlew :b_launcher:installApmDebug'
		name = raw_input('请选择')
		if '1'==name : 
			print os.system("gradle :launcher:installDebug")
		elif '2'==name:
			print os.system("gradle :browser:installDebug")
		elif '3'==name:
		
			print os.system("./gradlew :b_p_browser:installDebug")
		elif '4'==name:
			print '4444'
		#	print os.system("gradle :b_p_browser:assembleDebug")

			print os.system("./gradlew :b_p_browser:assembleDebug")
			print os.system("./gradlew :b_launcher:installDevDebug")
		exit();
		
	
#else : 
#	name = raw_input('请选择');



if  len(sys.argv) > 1 and 'log'==sys.argv[1]:
	#result, output = subprocess.getoutput("adb shell ps | grep 'com.qihoo.browser.browser'")
	#print(output)
		
	progress='com.qihoo.browser.browser'

	if  len(sys.argv) > 2 :
		if '1'==sys.argv[2]:
			progress='com.qihoo.browser'
		elif '2'==sys.argv[2]:
			progress='com.qihoo.browser.browser'
	print progress
	ret, output = commands.getstatusoutput("adb shell ps | grep " + progress)
	print output
	print '111'
	result =  output.split()
	key=""
	for index in range(len(result)):
		if (index % 9 == 1) :
			key = (result[index])
		elif (index % 9 == 8 and result[index] == progress) :
			print (result[index] + "  " + key)
			print os.system("adb logcat -v threadtime | grep " + key)

	exit();




if  len(sys.argv) > 1 and 'edit'==sys.argv[1]:
	os.system("gedit /home/kc/Desktop/w/code/my/MyPython/myshell.py")
	exit();

if  len(sys.argv) > 1 and 'go'==sys.argv[1]:
#	os.chdir(r'/home/kc/Desktop/w/code/my/MyPython/')
	print('/home/kc/Desktop/w/code/my/MyPython/')
	exit();




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



