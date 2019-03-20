# Report information to help find common problems with missing PATH entries
# or virtual environment/system interpreter mismatches.
# From the Python Discord: https://pythondiscord.com/invite

import os
import subprocess
import sys

# give information on our current interpreter
ver = sys.version_info
verstr = str(ver[0]) + '.' + str(ver[1]) + '.' + str(ver[2])
exe = sys.executable
print('Script running in Python %s from %s' % (verstr, exe))

# if we are in a virtual environment, this will not match
print('Base prefix of the above executable is %s\n' % sys.base_prefix)

# search the PATH environment variable for relevant executables
targets = {'py.exe': [],
           'python.exe': [],
           'pip.exe': [],
           }
paths = os.environ.get('PATH').split(';')
for path in paths:
    for target in targets:
        tentative = os.path.join(path, target)
        if os.path.exists(tentative):
            targets[target].append(tentative)

# print the full path to each found executable
for target in targets:
    if len(targets[target]) > 0:
        print('Found %s on PATH:' % target)
        for entry in targets[target]:
            print('    %s' % entry)
            runstr = '"%s" ' % entry + '--version'
            complete = subprocess.run(runstr, capture_output=True, text=True)
            print('    %s' % complete.stdout.split('\n')[0])
