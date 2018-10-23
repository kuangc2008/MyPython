#!/usr/bin/python
#coding:utf-8

# export ppp=/home/kc/Desktop/w/code/my/MyPython/myshell.py   shell中


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
command += "       1 查看底下有About message，网上搜索\n"
command += "       2  signal \n"
command += "       3 FATAL:memory\n"
print command


command=""
command += "java crash:\n"
command += "       find . | xargs grep 'find . | xargs grep 'fatal' -in -A 3 | grep browser -n' -in\n"
print command





command="ANR: \n"
command += "       find . | xargs grep 'Cmd line: com.qihoo.browser' -in\n"
command += "       find . | xargs grep 'ANR in com.qihoo.browser' -in\n"
print command

command="other:"
command += "      vi file +num"
print command



