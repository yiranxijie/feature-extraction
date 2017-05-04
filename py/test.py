# coding=gbk

import os,sys
import urllib2
import re

# test_list = [2,"Jone",3,6,7,'hongten','hanyuan','good',"Tom"]
# for i in range(len(test_list)):
	# if( i==0 ):
		# continue
	# else:
		# print test_list[i]
		
txt_path="D:/tao/apkSample/downloadUrl(1).txt"
localname="D:/tao/apkSample/test2.apk"
basicurl="http://static.apk.hiapk.com/Download.aspx?aid=3716"


def download(url, output):

	try:
		print ("downloading..." + url + "  ** file is : "+ output)
		response = urllib2.urlopen(url)
		newurl=response.geturl()
		print response.info().gettype()
		type=response.info().gettype()
		if( type.endswith(".package-archive")):
			print("this is a normal apk")
		elif( type.endswith("text/html") ):
			print("this is a error apk")
		if( newurl.endswith("404.html") ):
			print "404"
		print newurl
		resourceFile = open(output, "wb")
		resourceFile.write(response.read())
	except urllib2.HTTPError,e:
		print e.code,";"+e.reason
	
		
download(basicurl, localname)