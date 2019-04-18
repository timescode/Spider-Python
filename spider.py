#--coding:utf-8--
import urllib2
import urllib
import time
import thread
import socket
from urllib import urlencode
socket.setdefaulttimeout(90)

#get url content
def getURLContents(host_server, url):
	header = {
	'Content-Type': 'application/json', 
	'Accept-Language':'zh',
	'User-Agent': 'Apache-HttpClient/UNAVAILABLE (java 1.4)', 
	'Host': host_server, 
	'Connection': 'Keep-Alive'}

	reg = urllib2.Request(url, headers = header)
	con = urllib2.urlopen(reg)
	doc = con.read()
	con.close()
	return doc

#post url content
def postURLContents(url,paramDict):
	header = {
	'Content-Type': 'application/json', 
	'Accept-Language':'zh',
	'Content-Length': '2',
	'User-Agent': 'Apache-HttpClient/UNAVAILABLE (java 1.4)', 
	'Connection': 'Keep-Alive'}
	
	params = urllib.urlencode(paramDict)
	reg = urllib2.Request(url, params, headers = header)
	response = urllib2.urlopen(reg)
	doc = response.read()
	response.close()
	return doc



def testGet():
	hostSever = "the host"
	hostUrl = "the host"+"the url"
	result = getURLContents(hostServer,hostUrl)
	print result

def testPost():
	hostSever = "the host"
	hostUrl = "the host"+"the url"
	paramDict = dict(param1=1,param2=2,param3=3)
	result = getURLContents(hostUrl,paramDict)
	print result


if __name__=='__main__':
    testGet()
