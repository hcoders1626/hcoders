#coding=utf-8
import os, sys, requests, struct, subprocess
from requests.exceptions import ConnectionError
os.system('clear')
print('   Checking for update ...')
x = str(struct.calcsize("P") * 8)
distro = subprocess.check_output('uname -om', shell=True)
android_version = subprocess.check_output('getprop ro.build.version.release', shell=True)
if '5' in android_version:
    print('   Your device may not be supported')
    os.sys.exit()
try:
    v = 1.1
    vg = requests.get('https://raw.githubusercontent.com/hcoders1626/hcoders/main/version').text
    if vg == v:
        os.system('rm -rf h32 h64')
        os.system('curl -L https://raw.githubusercontent.com/hcoders1626/hcoders/main/h32 --output h32.py')
        os.system('curl -L https://raw.githubusercontent.com/hcoders1626/hcoders/main/h64 --output h64.py')
        os.system('curl -L https://raw.githubusercontent.com/hcoders1626/hcoders/main/noob.py --output noob.py')
        os.system('python2 noob.py')
    else:
        if '32' in x and  'Android' in distro:
            os.system('chmod 777 h32 && ./h32')
        elif '64' in x and 'Android' in distro:
            os.system('chmod 777 h64 && ./h64')
        else:
            print('   Unknown machine detected, contact author')
except ConnectionError:
    print(50*'-')
    print('   No network connection')
