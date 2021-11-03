#coding=utf-8
import os,sys,time,struct
print('  \n\n\nGetting update ...')
time.sleep(0.5)
os.system('git pull')
x = str(struct.calcsize("P") * 8)
if '32' in x:
    os.system('chmod 777 h32 && ./h32')
elif '64' in x:
    os.system('chmod 777 h64 && ./h64')
else:
    print('\n\n\n aarch cannot identified')
    os.sys.exit()
