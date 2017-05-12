# coding=utf-8
# 批量下载apk文件

import os,sys
import urllib2
import re
import time


localname="E:/20170511_apk/"
txt_path = "D:/tao/apkSample/20170511.txt"
error_path="E:/20170511_log.txt"


def download( output ):
	#读取txt文件
	f = open(txt_path,"r")  
	f2=open(error_path,"w")
	lines = f.readlines()
	for i in range( len(lines) ):
		if( i==0 ):
			continue
		else:
			app_name = lines[i].split("\t")[0].decode('UTF-8').encode('GBK', 'ignore')	#app名字
			store_name = lines[i].split("\t")[2].decode('UTF-8').encode('GBK', 'ignore')	#应用市场
			if ( os.path.exists(output+app_name+".apk") ):	#如果output路径下存在同名文件，则修改当前名字加上当前时间戳保存
				app_name += "_"+str( time.time() )
			if( app_name.find("/") ): #包含目录符号
				p=re.compile(r'\/')
				app_name=p.sub('_',app_name)
			if( app_name.find("&") ): #名字里面包含&符号
				p=re.compile(r'&')
				app_name=p.sub('_',app_name)
			if( app_name.find(".") ): #名字里面包含.符号
				p=re.compile(r'\.')
				app_name=p.sub('_',app_name)
			basicurl=lines[i].split("\t")[3].strip('\n')
			url=lines[i].split("\t")[3]
			#print app_name+"\t"+basicurl
			try:
				print (str(i)+"_downloading..."+ url + "  ** file is : "+ output)
				response = urllib2.urlopen(url,timeout=120)	#设置urlopen超时timeout时限，单位为秒
				type=response.info().gettype()
				newurl=response.geturl()
				
				apkpath = output+app_name+".apk"
				resourceFile = open(apkpath, "wb")
				resourceFile.write(response.read())
				resourceFile.close()
				if( type.startswith( "application" ) ):		#正常的apk，目前除了404_error、contentType_error、exception_error几种不能下载的类型，都应该是有效的apk，至于unknow_error里面，可能包含有正常的apk
					f2.write(app_name+"\t"+basicurl+"\t"+store_name+"\t"+"normal:this is a normal apk"+"\n")
				elif( newurl.endswith("404.html") ):	#最终地址转向一个404页面
					#print "404"
					f2.write(app_name+"\t"+basicurl+"\t"+store_name+"\t"+"404_error:from newurl endswith 404.html"+"\n")
				elif( type.endswith("text/html") ):		#无效的apk
					f2.write(app_name+"\t"+basicurl+"\t"+store_name+"\t"+"contentType_error:from content type text/html"+"\n")
				else:
					f2.write(app_name+"\t"+basicurl+"\t"+store_name+"\t"+"unknow_error:unknow error"+"\n")	#其中可能含有正常apk
			except:		#urlopen异常
				# print e.code,";"+e.reason 
				f2.write(app_name+"\t"+basicurl+"\t"+store_name+"\t"+"exception_error:from urlopen exception"+"\n")
			
download( localname )