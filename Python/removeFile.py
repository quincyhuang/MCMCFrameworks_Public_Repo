import os
import sys

if os.path.exists(sys.argv[1]):
    os.remove(sys.argv[1])
    print('removed file <' + sys.argv[1] +'>')
else:
    print('no such file <' + sys.argv[1] +'>')