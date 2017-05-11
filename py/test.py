# coding=utf-8

import os,sys
import urllib2
import re

# test_list = [2,"Jone",3,6,7,'hongten','hanyuan','good',"Tom"]
# for i in range(len(test_list)):
	# if( i==0 ):
		# continue
	# else:
		# print test_list[i]
		

localname="D:/tao/apkSample/test.apk"
basicurl="http://shouji.360tpcdn.com/360sj/jifeng/162670_51ed3e93-a586-46e4-ad2b-c2f17a7ab26f.apk"


def download(url, output):

	try:
		print ("downloading..." + url + "  ** file is : "+ output.decode("utf-8").encode("gbk"))
		response = urllib2.urlopen(url)
		newurl=response.geturl()
		print response.info()
		print response.info().gettype()
		type=response.info().gettype() 
		if ( type.startswith( "application" ) ):
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