# Report information to help find common problems with missing PATH entries
# or virtual environment/system interpreter mismatches.
# From the Python Discord: https://pythondiscord.com/

from __future__ import print_function

import os
import subprocess
import sys

# give information on our current interpreter
ver = sys.version_info
verstr = str(ver[0]) + '.' + str(ver[1]) + '.' + str(ver[2])
exe = sys.executable
print('Script running in Python %s from %s' % (verstr, exe))

# are we in a virtual environment?
if ver[0] == 2:  # Python 2
    if hasattr(sys, 'real_prefix'):
        Print('Running in a virtual environment at %s' % sys.real_prefix)
if ver[0] == 3:  # Python 3
    print('Base prefix of the above executable is %s\n' % sys.base_prefix)

# search the PATH environment variable for relevant executables
# and store as lists of full paths to the targets
targets = {'py.exe': [],
           'python.exe': [],
           'pip.exe': [],
           }
paths = os.environ.get('PATH').split(';')
for path in paths:
    for exe in targets:
        tentative = os.path.join(path, exe)
        if os.path.exists(tentative):
            targets[exe].append(tentative)

# print the full path to each found executable, and call them to get version
for exe in targets:
    if len(targets[exe]) > 0:
        print('Found %s on PATH:' % exe)
        for full_path in targets[exe]:
            print('    %s' % full_path)
            run_str = '"%s" ' % full_path + '--version'
            run_version = subprocess.run(run_str, capture_output=True, text=True)
            print('    %s' % run_version.stdout.split('\n')[0])
