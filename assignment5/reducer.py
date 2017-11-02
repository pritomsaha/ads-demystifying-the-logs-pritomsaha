#!/usr/bin/python
import sys
unique_files = set()
for line in sys.stdin:
	file_path = line.strip()
	unique_files.add(file_path)

print "number of unique files are: "+str(len(unique_files))+"\n"
