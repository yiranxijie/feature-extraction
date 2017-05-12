# coding=utf-8

txt_path = "D:/tao/apkSample/20170511.txt"
error_path="E:/torrenthandle.txt"


def download( ):
    f = open(txt_path,"r")  
    f2=open(error_path,"w")
    lines = f.readlines()
    print len(lines)
    for i in range( len(lines) ):
        if( i==0 ):
            continue
        else:
            basicurl=lines[i].split("\t")[3].strip('\n')
            f2.write(basicurl+"\n")
            
download(  )