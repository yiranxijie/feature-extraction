# coding=utf-8
# 批量下载apk文件

import os,sys
import urllib2
import re


localname="E:/apk/"
txt_path="D:/tao/apkSample/downloadUrl(1).txt"
error_path="E:/error.txt"


def download( output ):
	#读取txt文件
	f = open(txt_path,"r")  
	#f2=open(error_path,"w")
	lines = f.readlines() 
	for i in range( 2 ):
		if( i==0 ):
			continue
		else:
			app_name=lines[12].split("\t")[0].decode('UTF-8').encode('GBK')
			print app_name
			if( app_name.find("/") ): #名字里面包含目录符号
				p=re.compile(r'\/')
				app_name=p.sub('_',app_name)
			if( app_name.find("&") ): #名字里面包含&符号
				p=re.compile(r'&')
				app_name=p.sub('_',app_name)
			if( app_name.find(".") ): #名字里面包含.符号
				p=re.compile(r'\.')
				app_name=p.sub('_',app_name)
			basicurl=lines[12].split("\t")[4]
			url=lines[i].split("\t")[4]
			#print app_name+"\t"+basicurl
			try:
				print ("downloading..." + url + "  ** file is : "+ output)
				response = urllib2.urlopen(url)
				newurl=response.geturl()
				if( newurl.endswith("404.html") ):
					#print "404"
					f2.write(app_name+"\t"+basicurl)
				else:
					apkpath=output+app_name+".apk"

					resourceFile = open(apkpath, "wb")
					resourceFile.write(response.read())
					resourceFile.close()
			except urllib2.HTTPError,e:
				print e.code
				print e.reason  
				f2.write(app_name+"\t"+basicurl)
			
download( localname )