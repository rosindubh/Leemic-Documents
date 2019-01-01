# program to backup files
# taken from a byte of python
# phil welsby- 28 may 2018

import os
import time

source = ['/home/phil/my_python_programs']

target_dir = '/media/phil/Phil_Welsby/BACKUP'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

target = today + os.sep + now + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

print('zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successfull backup to:', target)
else:
    print('Backup FAILED!')
