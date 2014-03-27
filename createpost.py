#!/usr/bin/python

#creates a markdown file with the Jekyll post naming convention, puts in YAML front-matter,  and opens up vim. 

import sys
import datetime
from subprocess import call

now = datetime.datetime.now()

formatedName = ""
postTitle = ""
for arg in sys.argv[1:]:
	if (arg != sys.argv[-1]):
		formatedName += arg.lower()+"-"
		postTitle += arg + " "
	else:
		formatedName += arg.lower()
		postTitle += arg
	

postFilename = "%d-%02d-%02d-%s.markdown" % (now.year, now.month, now.day, formatedName)
print postTitle
yamlContent = '---\nlayout: post\ntitle: "%s"\ndate: %d-%02d-%02d %02d:%02d:%02d\n---' % (postTitle, now.year, now.month, now.day, now.hour, now.minute, now.second)

call('echo "%s" >> _posts/%s && vim _posts/%s +7' % (yamlContent, postFilename, postFilename), shell=True) 
