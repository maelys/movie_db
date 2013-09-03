import fnmatch
import os

movienames = []
for root, dirnames, filenames in os.walk('/Users/anaelle/Desktop/In Process/Films'):
  for extension in ('*.avi', '*.mp4', '*.mkv'):
    for filename in fnmatch.filter(filenames, extension):
      movienames.append(filename)

#print '\n'.join(movienames)
print len(movienames)
for moviename in movienames:
   print str(moviename).replace("."," ")
