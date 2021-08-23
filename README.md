# SMBPerf v0.3

Simple Python based network storage benchmark

## Description
This application times the transfert of either a single file or a directory.
- Provide average speed in MB and time duration.
- Works with any kind of storage and/or mount, not only SMB ;-)

The script allow to benchmark the whole transfert flow: storage speed and network speed. It also mimics basic file transfert common to a lot application, servers, etc.

Feedbacks are welcome!

## Usage
python smbperf.py [TARGET_FILE_OR_FOLDER]

example: 
- smbperf.py /home/david/mylargezipfile.zip
- python smbperf.py /mnt/remotestorage/remotefolder
