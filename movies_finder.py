#!/usr/bin/env python

import os
import re
import fnmatch
import urllib2

# Google returns 403 error without user agent        
USER_AGENT = ("Mozilla/5.0 (Macintosh; I; Intel Mac OS X 11_7_9; de-LI; rv:1.9b4) Gecko/2012010317 Firefox/10.0a4")
        
HEADERS = { 'User-Agent': USER_AGENT }

def find_movies(folderpath):
    movienames = []
    for root, dirnames, filenames in os.walk(folderpath):
        for extension in ('*.avi', '*.mp4', '*.mkv'):
            for filename in fnmatch.filter(filenames, extension):
                movienames.append(filename)
    return movienames

def clean_movienames(movienames):
    newmovienames = []
    newmoviename = ""
    for moviename in movienames:
        newmoviename = moviename[:-4].replace("."," ").lower()
        try:
            newmoviename = re.sub('\(.*','')
        except:
            None
        try:
            newmoviename = re.sub('french.*','', newmoviename)
        except:
            None
        try:
            newmoviename = re.sub('dvdrip.*','', newmoviename)
        except:
            None
        try:
            newmoviename = re.sub('1080p.*','', newmoviename)
        except:
            None
        try:
            newmoviename = re.sub('vostfr.*','', newmoviename)
        except:
            None
        try:
            newmoviename = re.sub('\[.*]','', newmoviename)
        except:
            None
        try:
            newmoviename = re.sub('brrip.*','', newmoviename)
        except:
            None
        try:
            newmoviename = re.sub('xvid.*','', newmoviename)
        except:
            None
            
        newmovienames.append(newmoviename)
        
    return newmovienames

def getgooglesearchlink(search,searchsite=False):
    if searchsite == False:
        return 'http://www.google.com/search?q='+urllib2.quote(search)+'&oq='+ \
            urllib2.quote(search)
    else:
        return 'http://www.google.com/search?q=site:'+urllib2.quote(searchsite) \
            +'%20'+urllib2.quote(search)+'&oq=site:'+urllib2.quote(searchsite)+\
            '%20'+urllib2.quote(search)

def googlesearch(search,searchsite=False):
    # google research
    req = urllib2.Request(getgooglesearchlink(search,searchsite),None,HEADERS)
    site = urllib2.urlopen(req)
    data = site.read()
    site.close()

    # find google results
    start = data.find('<div id="res">')
    end = data.find('<div id="foot">')
    if data[start:end]=='':
    # error, no links found
        print "no links found"
        return False
    else:
        #links =[]
        data = data[start:end]
        start = 0
        end = 0        
        #while start > -1 and end > -1:
            # get only results of the provided site
            #if searchsite == False:
                #start = data.find('<a href="/url?q=')
            #else:
                #start = data.find('<a href="/url?q='+str(searchsite))
                #data = data[start+len('<a href="/url?q='):]
                #end = data.find('&amp;sa=U&amp;ei=')
            #if start > -1 and end > -1: 
                #link =  urllib2.unquote(data[0:end])
                #data = data[end:len(data)]
                #if link.find('http') == 0:
                    #links.append(link)
                    
        if searchsite == False:
            start = data.find('<a href="/url?q=')
        else:
            start = data.find('<a href="/url?q='+str(searchsite))
            data = data[start+len('<a href="/url?q='):]
            end = data.find('&amp;sa=U&amp;ei=')
                    #if start > -1 and end > -1: 
            link =  urllib2.unquote(data[0:end])
            data = data[end:len(data)]
            if link.find('http') == 0:
                return link
    return None
    
def main():
    movienames = find_movies('/Users/anaelle/Desktop/In Process/Films')
    movienames = clean_movienames(movienames)
    #print '\n'.join(movienames)
    #links = googlesearch('savages','http://www.imdb.com/')
    #for link in links:
        #print link
    imdb = 'http://www.imdb.com/'
    for moviename in movienames:
        link = googlesearch(moviename,imdb)
        print moviename
        print link
        print "-----------------------------------"
        
        
if __name__ == "__main__":
    main()
    
    
    
