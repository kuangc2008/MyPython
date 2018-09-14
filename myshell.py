#!/usr/bin/python
#coding:utf-8
command1="adb shell \"dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp'\""
command="当前Activity				"
command += command1;
print command


command="     				        "
command += "adb shell monkey -p com.qihoo.contents -v 20000"
print command







