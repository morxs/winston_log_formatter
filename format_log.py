## This script utility is to manipulate error log made by nodejs logger
## so it can be consumed and converted into CSV format, which later
## can be converted into tabulator date on Excel
##
## Currently runnable on python 2.7.3

import os
import sys
import shutil

#total = len(sys.argv)
#cmdargs = str(sys.argv)
#print cmdargs

if len(sys.argv) > 1:
	with open(sys.argv[1], 'r+b') as f:

		# go to beginning of file and read the whole file into list
		semua_file = f.readlines()
		#print semua_file

		# manipulate the list
		for index in range(len(semua_file)):
			if index == 0:
				semua_file[index] = '{[\r\n' + semua_file[index]
				semua_file[index] = semua_file[index].replace('}', '},', 1)
			elif index == len(semua_file) - 1:
				semua_file[index] = semua_file[index] + '\r\n]}'
			else:
				semua_file[index] = semua_file[index].replace('}', '},', 1)

		#print semua_file

		# go to beginning of file and rewrite the whole file
		f.seek(0,0)
		f.writelines(semua_file)
		
		# flush the file and commit the changes
		f.flush()
		os.fsync(f.fileno())
		f.close()
else:
	print '\r\n  format_log.py: a json log tidy\r\n'
	print '  Usage: python format_log.py <input_file>'
