import fnmatch
import os
import re

movienames = []
for root, dirnames, filenames in os.walk('/Users/anaelle/Desktop/In Process/Films'):
    for extension in ('*.avi', '*.mp4', '*.mkv'):
        for filename in fnmatch.filter(filenames, extension):
            movienames.append(filename)

#print '\n'.join(movienames)
print len(movienames)
for moviename in movienames:
    moviename = str(moviename).replace("."," ")
    #moviename = str(moviename).replace("avi"," ")
    moviename = moviename[:-4]
    moviename = moviename.lower()
    try:
        m1 = re.search('\(.*',moviename)
        moviename = moviename.replace(m1.group(0),'')
    except:
        None
    try:
        m1 = re.search('french.*',moviename)
        moviename = moviename.replace(m1.group(0),'')
    except:
        None
    try:
        m1 = re.search('dvdrip.*',moviename)
        moviename = moviename.replace(m1.group(0),'')
    except:
        None
    try:
        m1 = re.search('1080p.*',moviename)
        moviename = moviename.replace(m1.group(0),'')
    except:
        None
    try:
        m1 = re.search('vostfr.*',moviename)
        moviename = moviename.replace(m1.group(0),'')
    except:
        None
    try:
        m1 = re.search('\[.*]',moviename)
        moviename = moviename.replace(m1.group(0),'')
    except:
        None
    try:
        m1 = re.search('brrip.*',moviename)
        moviename = moviename.replace(m1.group(0),'')
    except:
        None
    try:
        m1 = re.search('xvid.*',moviename)
        moviename = moviename.replace(m1.group(0),'')
    except:
        None
    print moviename
#print '\n'.join(movienames)
