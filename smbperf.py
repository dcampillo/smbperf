#!/usr/bin/python

import sys
import os.path
#from shutil import copyfile
import shutil
import datetime

# Check for arguments
if len(sys.argv) != 2:
	print("Wrong number of arguments!")
	print("Usage: python smbperf.py [targetfile]")
	sys.exit(0) 

# Gather first parameter as target file to be copied
target_file = sys.argv[1]
benchmark_dir = os.path.join(os.getcwd(), "bench")
fileSize = 0



# Check if benchmark folder exists
if os.path.exists(benchmark_dir) == False:
	#if not create the folder
	os.makedirs(benchmark_dir)
else:
	print ("Clean Benchmark folder: %s" % benchmark_dir)
	# if yes, recursively empty content
	for path,dirs,files in os.walk(benchmark_dir):
		for filename in files:
			os.remove(os.path.join(benchmark_dir, filename))

# Store time at start of the copy
start_time = datetime.datetime.now()

# Check if a file or a folder must be copied
if os.path.isfile(target_file):
	fileSize = os.path.getsize(target_file)
	print("Copying '%s' to '%s'" % (target_file, benchmark_dir))
	shutil.copy(target_file, benchmark_dir)
elif os.path.isdir(target_file):
	for path,dirs,files in os.walk(target_file):
		for filename in files:
			currentFile = os.path.join(path,filename)
			print("Copying '%s' to '%s'" % (currentFile, benchmark_dir))
			fileSize += os.path.getsize(currentFile)
			shutil.copy(currentFile, benchmark_dir)
else:
	print("File '" + target_file + "' is not a file!")
	sys.exit(0)

end_time = datetime.datetime.now()
timespan = end_time - start_time

avg_speed = fileSize/timespan.total_seconds()/1024/1024

print("%s seconds elapsed"%timespan)
print("%s Mb/s"%avg_speed)
