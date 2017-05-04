# coding=utf-8
# 批量下载apk文件

import os,sys
import urllib2
import re


localname="E:/apk2/"
txt_path = "D:/tao/apkSample/testUrl.txt"
error_path="E:/error2.txt"


def download( output ):
	#读取txt文件
	f = open(txt_path,"r")  
	f2=open(error_path,"w")
	lines = f.readlines()
	for i in range( len(lines) ):
		if( i==0 ):
			continue
		else:
			app_name=lines[i].split("\t")[0]
			if( app_name.find("/") ): #包含目录符号
				p=re.compile(r'\/')
				app_name=p.sub('_',app_name)
			if( app_name.find("&") ): #名字里面包含&符号
				p=re.compile(r'&')
				app_name=p.sub('_',app_name)
			if( app_name.find(".") ): #名字里面包含.符号
				p=re.compile(r'\.')
				app_name=p.sub('_',app_name)
			basicurl=lines[i].split("\t")[4].strip('\n')
			url=lines[i].split("\t")[4]
			#print app_name+"\t"+basicurl
			try:
				print ("downloading..." + url + "  ** file is : "+ output)
				response = urllib2.urlopen(url)
				type=response.info().gettype()
				newurl=response.geturl()
				if( type.endswith(".package-archive")):		#正常的apk
					apkpath=output+app_name+".apk"
					resourceFile = open(apkpath, "wb")
					resourceFile.write(response.read())
					f2.write(app_name+"\t"+basicurl+"\t"+"normal:this is a normal apk"+"\n")
					resourceFile.close()
				elif( newurl.endswith("404.html") ):	#最终地址转向一个404页面
					#print "404"
					f2.write(app_name+"\t"+basicurl+"\t"+"404_error:from newurl endswith 404.html"+"\n")
				elif( type.endswith("text/html") ):		#无效的apk
					f2.write(app_name+"\t"+basicurl+"\t"+"contentType_error:from content type text/html"+"\n")
				else:
					f2.write(app_name+"\t"+basicurl+"\t"+"unknow_error:unknow error"+"\n")
			except:		#urlopen异常
				# print e.code,";"+e.reason 
				f2.write(app_name+"\t"+basicurl+"\t"+"exception_error:from urlopen exception"+"\n")
			
download( localname )