import os,sys
import urllib2
import re
import time
import random

#"https://github.com/search?l=C&q=Huffmancoding&ref=searchresults&type=Repositories&utf8=%E2%9C%93"
#"https://github.com/search?l=C&p=2&q=BinarySearch&ref=searchresults&type=Repositories&utf8=%E2%9C%93"
basicurl ="https://github.com"
surlpart1 = "/search?l=C&q="
surlpart1_1 = "/search?l=C&p="
surlpart2 = "&ref=searchresults&type=Repositories&utf8=%E2%9C%93"
suffix = "/archive/master.zip"
storagefolder = "temp"
global cnum
cnum = 0




def githubsearchpage(keyword,nflag):
    if keyword:
        if nflag == -1:
            surl = basicurl + surlpart1 + keyword + surlpart2
        else:
            surl = basicurl + surlpart1_1 + str(nflag)  + "&q=" + keyword + surlpart2
    else:
        surl = basicurl
    return surl


def basicinfo(keyword):
    url = githubsearchpage(keyword, -1)
    print(url)
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    # 2.content
    content = response.read()
    mode = "\d+\s+repository results\s+"#"ve found \d+\s+"
    strMatch = filtermode(mode,content)  
    #ts = strMatch[0][8:].strip()
    ts = re.findall(r'(\w*[0-9]+)\w*',strMatch[0])
    #print(ts)
    return int(ts[0])/10



def keycontext(url,keyword):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    # 2.content
    content = response.read()
    lst =  filtercontext(content,keyword)
    return lst



def filtercontext(context,keyword):
    lst =[]
    mode = ".*/\w*"+keyword+"\w*\""
    strMatch = filtermode(mode,context)
    size = len(strMatch)
    for i in range(0, size, 1):
        tstr = strMatch[i].strip()
        tstr = tstr[9: len(tstr)-1]
        lst.append(tstr)
    return lst


def filtermode(mode,content):
    pattern = re.compile(mode, re.I)
    strMatch = pattern.findall(content)
    return strMatch

def  getdownurl(lst):
    spath = os.getcwd() + os.sep+ storagefolder
    if not os.path.exists(spath):
        os.mkdir(spath)

    for item in lst:
        rurl = basicurl  + item + suffix
        tpname = item.replace("/","_")
        tpname = tpname +".zip"
        download(rurl, spath+os.sep+tpname)



def download(url, output):
    print ("downloading..." + url + "  ** file is : "+ output)
    response = urllib2.urlopen(url)
    resourceFile = open(output, "wb")
    resourceFile.write(response.read())
    resourceFile.close()
    global cnum
    cnum = cnum + 1
    print( "downloaded! "+ str( cnum))
    if cnum < 20:
        num = random.randint(2, 8)
    else:
        num = random.randint(8,15)
    #print("wait time begin another : " + str(num))
    #time.sleep(num)



if __name__=='__main__':
    '''
    for it in sys.argv:
        print(it)
    for i in range(1,len(sys.argv)):
        print("dd")
    '''
    keyword = "Huffmancod"
    tnum = basicinfo(keyword)

    for i in range(1, tnum + 2):
        url = githubsearchpage(keyword,i)
        print(url)
        if i >= 4:
            print("wait for 5 minutes")
            time.sleep(30)
        getdownurl(keycontext(url, keyword))
