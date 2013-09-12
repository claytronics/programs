#!/usr/bin/python
#
# Transforms game of life files into meld files.

import sys

if len(sys.argv) != 2:
	print "usage: python transform_game_of_life.py <file>"
	sys.exit(1)

fp = open(sys.argv[1], "r")
last_line = None
whitespace = "\n"
lastid = 0
rowsize = None

lines = fp.readlines()
lines_read = 0
for line in lines:
	line = line.rstrip(whitespace).lstrip(whitespace)
	vec = line.split(' ')
	rowsize = len(vec)
	lines_read = lines_read + 1
	next_line = []
	i = 0
	for x in vec:
		total_neighbors = 0
		print "new-state(@" + str(lastid) + ", " + x + ", 0)."
		if lines_read != len(lines):
			print "!neighbor(@" + str(lastid) + ", @" + str(lastid + rowsize) + ", 7)."
			total_neighbors = total_neighbors + 1
		if i > 0:
			print "!neighbor(@" + str(lastid) + ", @" + str(lastid - 1) + ", 4)." 
			total_neighbors = total_neighbors + 1
			if lines_read > 1:
				print "!neighbor(@" + str(lastid) + ", @" + str(lastid - rowsize - 1) + ", 1)."
				total_neighbors = total_neighbors + 1
			if lines_read != len(lines):
				print "!neighbor(@" + str(lastid) + ", @" + str(lastid + rowsize - 1) + ", 6)."
				total_neighbors = total_neighbors + 1
		i = i + 1
		if i != len(vec):
			print "!neighbor(@" + str(lastid) + ", @" + str(lastid + 1) + ", 5)."
			total_neighbors = total_neighbors + 1
		 	if lines_read > 1:
		 		print "!neighbor(@" + str(lastid) + ", @" + str(lastid - rowsize + 1) + ", 3)."
				total_neighbors = total_neighbors + 1
		 	if lines_read != len(lines):
				print "!neighbor(@" + str(lastid) + ", @" + str(lastid + rowsize + 1) + ", 8)."
				total_neighbors = total_neighbors + 1
		if lines_read > 1:
		 	print "!neighbor(@" + str(lastid) + ", @" + str(lastid - rowsize) + ", 2)."
			total_neighbors = total_neighbors + 1
		print "!neighbor-count(@" + str(lastid) + ", " + str(total_neighbors) + ")."
		lastid = lastid + 1
