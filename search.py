#!/usr/bin/env python
# taken here: http://stackoverflow.com/questions/1657570/google-search-from-a-python-app
import urllib2

# Google returns 403 error without user agent        
HEADERS = { 'User-Agent' : 'Mozilla/11.0' }

def getgooglesearchlink(search,searchsite=False):
    if searchsite == False:
        return 'http://www.google.com/search?q='+urllib2.quote(search)+'&oq='+urllib2.quote(search)
    else:
        return 'http://www.google.com/search?q=site:'+urllib2.quote(searchsite)+'%20'+urllib2.quote(search)+'&oq=site:'+urllib2.quote(searchsite)+'%20'+urllib2.quote(search)

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
      links =[]
      data = data[start:end]
      start = 0
      end = 0        
      while start > -1 and end > -1:
          # get only results of the provided site
          if searchsite == False:
            start = data.find('<a href="/url?q=')
          else:
            start = data.find('<a href="/url?q='+str(searchsite))
          data = data[start+len('<a href="/url?q='):]
          end = data.find('&amp;sa=U&amp;ei=')
          if start > -1 and end > -1: 
              link =  urllib2.unquote(data[0:end])
              data = data[end:len(data)]
              if link.find('http') == 0:
                  links.append(link)
      return links
def main():
    links = googlesearch('savages','http://www.imdb.com/')
    for link in links:
        print link

if __name__ == "__main__":
    main()
