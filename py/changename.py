# coding=utf-8

import os,sys
import re
		
apk_path = "E:/20170511_apk/"	#待比较的apk文件夹路径
txt_path = "Z:/apkSample/20170511.txt"		#测试文件路径
log = "Z:/apkSample/changename_log.txt"		#日志文件
equal_file = "Z:/apkSample/equal_file.txt"
error_path = "Z:/apkSample/error_path.txt"
error_path = "Z:/apkSample/error_path.txt"
test_path = "Z:/apkSample/test_path.txt"


def compare(x, y):
	stat_x = os.stat(apk_path + "/" + x)
	stat_y = os.stat(apk_path + "/" + y)
	if stat_x.st_ctime < stat_y.st_ctime:
		return -1
	elif stat_x.st_ctime > stat_y.st_ctime:
		return 1
	else:
		return 0


def check( path ):
	f = open(txt_path,"r")
	f2=open(log,"w")
	f3=open(equal_file,"w")
	f4=open(error_path,"w")
	f5=open(test_path,"w")
	apklist = os.listdir(path) # get all the names of apps
	apklist.sort(compare)
	lines = f.readlines()
	content = ""
	count = 0
	for i in range( 0,len(apklist)-1 ):
		if( i==0 ):
			continue
		else:
			basicurl=lines[i].split("\t")[3].strip('\n')
			app_name = lines[i+count].split("\t")[0].decode('UTF-8').encode('GBK', 'ignore')
			app_url_name = basicurl.split("/")[-1]
			
			APK = apklist[i-1].split(".apk")[0].split("_")[0]

			if( app_name.find("/") ): #包含目录符号
				p=re.compile(r'\/')
				app_name=p.sub('_',app_name)
			if( app_name.find("&") ): #名字里面包含&符号
				p=re.compile(r'&')
				app_name=p.sub('_',app_name)
			if( app_name.find(".") ): #名字里面包含.符号
				p=re.compile(r'\.')
				app_name=p.sub('_',app_name)
				
			# if( len( APK.split(".") ) > 1 ):
				# f2.write(APK+"\n")
				
			if( APK == app_name.split("_")[0] ):
#				os.rename(path+apklist[i-1],path+lines[i+count].split("\t")[3].strip('\n').split("/")[-1])
				f3.write(apklist[i-1]+"\t"+lines[i+count].split("\t")[3].strip('\n').split("/")[-1]+"\n")
			else:
				content += lines[i]
				count += 1
			#	new_app_name = lines[i+count].split("\t")[0].decode('UTF-8').encode('GBK', 'ignore')
			f2.write(APK+"\t"+lines[i+count].split("\t")[0].decode('UTF-8').encode('GBK', 'ignore').split("_")[0]+"\n")
			f5.write(apklist[i-1]+"\t"+lines[i+count].split("\t")[3].strip('\n').split("/")[-1]+"\n")
			os.rename(path+apklist[i-1],path+lines[i+count].split("\t")[3].strip('\n').split("/")[-1])
	f4.write(content.strip('\n'))
		
check( apk_path )