#!/usr/bin/python3
##########################################
# SMBPerf v0.31
# Description: https://github.com/dcampillo/smbperf
# Author: D. Campillo
# Date: 23.08.2021
##########################################

#from imp import source_from_cache
import sys
import os.path
import shutil
import datetime
import argparse


def GetBenchmarkFolder():
    return os.path.join(os.getcwd(), 'benchmark')

def ClearBenchmarkFolder():
    benchmarkDirectory = GetBenchmarkFolder()

    # Check if benchmark folder exists
    if os.path.exists(benchmarkDirectory) == False:
        #if not create the folder
        os.makedirs(benchmarkDirectory)

    print ("Cleaning benchmark folder: %s" % benchmarkDirectory)
    for path,dirs,files in os.walk(benchmarkDirectory):
        for filename in files:
            os.remove(os.path.join(benchmarkDirectory, filename))
    return

def getOuputFile(Source, BenchmarkFolder):
    __filename = os.path.basename(Source)
    __output = os.path.join(BenchmarkFolder, __filename)
    return __output

def Benchmark(Source):

    # Setup files and benchmark folder parameters
    target_file = args.Target
    #sys.argv[1]
    benchmarkDirectory = GetBenchmarkFolder()
    fileSize = 0

    # Store time at start of the copy
    start_time = datetime.datetime.now()

    # Check if a file or a folder must be copied
    if os.path.isfile(Source):
        fileSize = os.path.getsize(Source)
        print("Copying '%s' to '%s'" % (Source, benchmarkDirectory))
        #shutil.copy(Source, benchmarkDirectory)
        with open(Source, 'rb') as fda:
            cpTarget = getOuputFile(Source, benchmarkDirectory)
            print(cpTarget)
            with open(cpTarget, 'wb') as fdb:
                shutil.copyfileobj(fda, fdb, length=64*1024*1)
    elif os.path.isdir(target_file):
        for path,dirs,files in os.walk(target_file):
            for filename in files:
                currentFile = os.path.join(path,filename)
                print("Copying '%s' to '%s'" % (currentFile, benchmarkDirectory))
                fileSize += os.path.getsize(currentFile)
                shutil.copy(currentFile, benchmarkDirectory)
    else:
        print("File '" + benchmarkDirectory + "' is not a valid file or folder!")
        sys.exit(0)

    end_time = datetime.datetime.now()
    timespan = end_time - start_time

    avg_speed = fileSize/timespan.total_seconds()/1024/1024

    print("Duration: {0}".format(timespan))
    print("Data transfered: {0:.2f} MB".format(fileSize/1024/1024))
    print("Average speed: {0:.2f} Mb/s".format(avg_speed))

def parse_arguments():
    """Read arguments from a command line."""
    parser = argparse.ArgumentParser(description='Arguments get parsed via --commands')
    parser.add_argument('Target', help='File or Folder used to benchmark')
    parser.add_argument("-c", help='Keep the content of the benchmark folder after the benchmark', action='store_true')

    args = parser.parse_args()
    return args

def main():
    ClearBenchmarkFolder()
    Benchmark(args.Target)
    if args.c == True:
        print("clearing benchmark")
        ClearBenchmarkFolder()

if __name__ == '__main__':
    args = parse_arguments()
    main()
