# coding=utf-8
# 分批读取共有358086行内容的txt文件，每取1000条输出到一个文件当中

txt_path = "E:/torrenthandle.txt"
base_path="E:/torrent_distribution/"


def download( ):
    f = open(txt_path,"r")  
    lines = f.readlines()
    f2=open(base_path+"1.txt","w")
    content=""
    for i in range( 1,len(lines) ):
        if ( i%1000!=0 ):
            content+=lines[i-1]
        else:
            content+=lines[i-1]
            f2.write(content.strip('\n'))
            block_path=base_path+str(i)+".txt"
            f2=open(block_path,"w")
            content=""
    #最后的扫尾工作
    content+=lines[i]   
    f2.write(content.strip('\n'))   
    f2.close()
    f.close()
    
download(  )