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
    for moviename in movienames:
        moviename = moviename.replace("."," ")
        moviename = moviename.lower()
        moviename = moviename[:-4]
        try:
            m = re.search('\(.*',moviename)
            moviename = moviename.replace(m.group(0),'')
        except:
            None
        try:
            m = re.search('french.*',moviename)
            moviename = moviename.replace(m.group(0),'')
        except:
            None
        try:
            m = re.search('dvdrip.*',moviename)
            moviename = moviename.replace(m.group(0),'')
        except:
            None
        try:
            m = re.search('1080p.*',moviename)
            moviename = moviename.replace(m.group(0),'')
        except:
            None
        try:
            m = re.search('vostfr.*',moviename)
            moviename = moviename.replace(m.group(0),'')
        except:
            None
        try:
            m = re.search('\[.*]',moviename)
            moviename = moviename.replace(m.group(0),'')
        except:
            None
        try:
            m = re.search('brrip.*',moviename)
            moviename = moviename.replace(m.group(0),'')
        except:
            None
        try:
            m = re.search('xvid.*',moviename)
            moviename = moviename.replace(m.group(0),'')
        except:
            None
        print moviename

def main():
    movienames = find_movies('/Users/anaelle/Desktop/In Process/Films')
    print clean_movienames(movienames)
    #print '\n'.join(movienames)

if __name__ == "__main__":
    main()

