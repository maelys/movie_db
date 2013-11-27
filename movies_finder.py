#!/usr/bin/env python
# -*- coding: utf-8 -*-

# googlesearch inspiration: http://stackoverflow.com/questions/1657570/
# google-search-from-a-python-app

import os
import re
import fnmatch
import urllib2
import urllib
from bs4 import BeautifulSoup
import movie
import database_manager

# Google returns 403 error without user agent        
HEADERS = { 'User-Agent': 'Mozilla/11.0' }

IMDB = 'http://www.imdb.com/'

# retrieve avi, mkv and mp4 files in a given folder
def find_movies(folderpath):
    movienames = []
    for root, dirnames, filenames in os.walk(folderpath):
        for extension in ('*.avi', '*.mp4', '*.mkv'):
            for filename in fnmatch.filter(filenames, extension):
                movienames.append(filename)
    return movienames

# clean names by deleting frequent pattern, and create a list of movies
def clean_movienames(movienames,path):
    newmoviename = ""
    movies_list = []
    for moviename in movienames:
        newmoviename = moviename[:-4].replace("."," ").lower()
        try:
            newmoviename = re.sub('(.*','')
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
            
        m = movie.Movie(path+moviename,newmoviename)
        movies_list.append(m)
        
    return movies_list

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

# Go to imdb.com and retrieve movie information   
def get_info(movie):
    req = urllib2.Request(movie.imdb_link, None, HEADERS)
    page_content = urllib2.urlopen(req).read()
    soup = BeautifulSoup(page_content,from_encoding="utf-8")
    for tag in soup.find_all('meta'):
        if tag.get('property') == "og:title":
            movie.movie_name = tag.get('content').encode('utf-8')
           #print movie.movie_name
        if tag.get('name') == "description":
            summary = tag.get('content')
            movie.summary = ".".join(summary.split(".")[2:]).encode('utf-8')
	    
        if tag.get('property') == "og:image":
            cover_url = tag.get('content').encode('utf-8')
            site_cover = urllib2.urlopen(cover_url)
            img = site_cover.read()
            writ = open("wimg","w")
            writ.write(img)
            write.close()
            site_cover.close()
            movie.cover = "wimg"
            os.remove("wimg")
          
    #for tag in soup.find_all("p",text = True):
        #if tag.get('itemprop') == 'description':
            #movie.summary = tag.contents[0]
    #<link rel='image_src' href=
    for tag in soup.find_all('span'):
       if tag.get('itemprop') == "ratingValue":
           movie.imdb_rating = float(tag.contents[0])
    
    
def main():
    path = '/home/anaelle/Desktop/movie-db/movies'
    movienames = find_movies(path)
    movies_list = clean_movienames(movienames,path)
    #print '\n'.join(movienames)
    #links = googlesearch('savages','http://www.imdb.com/')
    #for link in links:
        #print link
    
    for movie in movies_list:
        #print repr(movie)
        link = googlesearch(movie.movie_name,IMDB)
        movie.imdb_link = link
        get_info(movie) #attention voir si ca modifie sans retourner quch
        #print movie.movie_name
        #print movie.summary
        #print movie.imdb_rating
        #print movie.seen
        print str(movie)
        db = database_manager.DatabaseManager()
        db.connect()
        insert_values = (movie.movie_name,movie.movie_path,movie.imdb_link,movie.cover,movie.summary,movie.imdb_rating,movie.anaelle_rating, movie.seen)
        db.insert(insert_values)
        db.close()
        
        
if __name__ == "__main__":
    main()
    
    
    
