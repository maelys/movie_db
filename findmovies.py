#!/usr/bin/env python
import fnmatch
import os
import re

#'/Users/anaelle/Desktop/In Process/Films'
def find_movies(folderpath):
    movienames = []
    for root, dirnames, filenames in os.walk(folderpath):
        for extension in ('*.avi', '*.mp4', '*.mkv'):
            for filename in fnmatch.filter(filenames, extension):
                movienames.append(filename)
    return movienames

def clean_movienames(movienames):
    newmovienames = []
    for moviename in movienames:
        newmoviename = moviename[:-4].replace("."," ").lower()
     
        try:
            m = re.search('\(.*',moviename)
            newmoviename = moviename.replace(m.group(0),'')
        except:
            None
        try:
            m = re.search('french.*',moviename)
            newmoviename = moviename.replace(m.group(0),'')
        except:
            None
        try:
            m = re.search('dvdrip.*',moviename)
            newmoviename = moviename.replace(m.group(0),'')
        except:
            None
        try:
            m = re.search('1080p.*',moviename)
            newmoviename = moviename.replace(m.group(0),'')
        except:
            None
        try:
            m = re.search('vostfr.*',moviename)
            newmoviename = moviename.replace(m.group(0),'')
        except:
            None
        try:
            m = re.search('\[.*]',moviename)
            newmoviename = moviename.replace(m.group(0),'')
        except:
            None
        try:
            m = re.search('brrip.*',moviename)
            newmoviename = moviename.replace(m.group(0),'')
        except:
            None
        try:
            m = re.search('xvid.*',moviename)
            newmoviename = moviename.replace(m.group(0),'')
        except:
            None
        newmovienames.append(newmoviename)
        
    return newmovienames

def main():
    movienames = find_movies('/Users/anaelle/Desktop/In Process/Films')
    movienames = clean_movienames(movienames)
    print '\n'.join(movienames)

if __name__ == "__main__":
    main()

