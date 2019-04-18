#--coding:utf-8--
import urllib2
import urllib
import util
import time
import thread
import logging
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
def postURLContents(url):
	header = {
	'Content-Type': 'application/json', 
	'Accept-Language':'zh',
	'Content-Length': '2',
	'User-Agent': 'Apache-HttpClient/UNAVAILABLE (java 1.4)', 
	'Connection': 'Keep-Alive'}
	postdata = dict(param1=1,param2=2,param3=3)
	postdata2 = urllib.urlencode(postdata)
	reg = urllib2.Request(url, postdata2, headers = header)
	response = urllib2.urlopen(reg)
	doc = response.read()
	response.close()
	return doc

#scan the url 
def scanItem(hostserver,url):
	tempUrl = urlencode(url)
	doc = getURLContents(hostserver,tempUrl);
	jsonStr = json.loads(doc)
	print jsonStr


def main():
	util.log_init()
	hostSever = "the host"
	hostUrl = "the host"+"the url"
	scanItem(hostServer,hostUrl)
	util.logger.warning('main exit')

if __name__=='__main__':
    main() 
