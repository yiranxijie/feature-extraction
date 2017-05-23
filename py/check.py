# coding=utf-8

import os,sys
import urllib2
import re
		
apk_path = "Z:/apkSample/31584/"	#待比较的apk文件夹路径
txt_path = "Z:/apkSample/test.txt"		#测试文件路径
log = "Z:/apkSample/test_log.txt"		#日志文件


def check( path ):
	f = open(txt_path,"r")
	f2=open(log,"w")
	apklist = os.listdir(path) # get all the names of apps
	lines = f.readlines()
	content = ""
	for i in range( len(lines) ):
		basicurl=lines[i].split("\t")[3].strip('\n')
		app_url_name = basicurl.split("/")[-1]

		if ( os.path.exists(path+app_url_name) ):	##如果path路径下存在同名文件
			continue
		else:
			content += lines[i]
	f2.write(content.strip('\n'))
		
check( apk_path )