#!/usr/bin/env python
# coding=utf-8
 
 
import os
import zipfile
 
 
path="D:/tao/test/apkstore" # this is apk files' store path
dex_path="D:/tao/test/dex/" # a directory  store dex files
 
 
apklist = os.listdir(path) # get all the names of apps
 
if not os.path.exists(dex_path):
    os.makedirs(dex_path)
 
for APK in apklist:
    portion = os.path.splitext(APK)
 
    if portion[1] == ".apk":
        newname = portion[0] + ".zip" # change them into zip file to extract dex files
        #print newname
        os.chdir(path)
        os.rename(APK,newname)
 
    #if APK.endswith(".zip"):
        apkname = portion[0]
 
        #zip_apk_path = os.path.join(path,APK) # get the zip files
        zip_apk_path = path+"/"+newname
        print zip_apk_path
 
        z = zipfile.ZipFile(zip_apk_path, 'r') # read zip files
 
        for filename in z.namelist():
        	#print filename
        	if filename.endswith(".dex"):
        		dexfilename = "classes" + ".dex"
        		dexfilepath = os.path.join(dex_path, dexfilename)
        		f = open(dexfilepath, 'w+') # eq: cp classes.dex dexfilepath
        		f.write(z.read(filename))
        	if filename.endswith(".xml"):
        		xmlfilename = apkname + "_AM.xml"
        		xmlfilepath = os.path.join(dex_path,xmlfilename)
        		f = open(xmlfilepath,"w+")
        		f.write(z.read(filename))
 
print "all work done!"