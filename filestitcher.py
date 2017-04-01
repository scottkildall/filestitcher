# filestitcher.py
# simple utility script to stitch multiple files together
# written by Scott Kildall
# uses a specific file extension 

import os
from os import listdir
from os.path import isfile, join
	

# generate list of files
def makeFileList(mypath):
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	return onlyfiles

def processFiles(inputPath,outputPath, extension):
	fileList = makeFileList("input")

	wf = makeWriteFile(outputPath, "datafile.csv")

	for filename in fileList:
		if filename.endswith(extension):
			lines = loadLines(inputPath, filename)
			writelines(wf, lines)
    	else:
    		print "skipping: " + filename

	wf.close()


def loadLines(path, filename):
	f = open( path + "/" + filename, "r" )
	lines = []
	for line in f:
		# do additional line-processing here
		#lines.append( line.rstrip('\n') )
		lines.append(line)
	f.close()
	return lines

def writelines(f, lines):
	for line in lines:
		f.write(line)
	f.flush()

def makeWriteFile(outputPath, filename):
	f = open( outputPath + "/" + filename, "w" )
	return f

processFiles("input", "output", ".CSV")