import os,platform

os.system('rm -rf Loader_enc.cpython-311.so Loader32.cpython-311.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
	import Loader_enc
else:
	import Loader_enc

elif bit == '32bit':
	import Loader32
else:
	import Loader32
